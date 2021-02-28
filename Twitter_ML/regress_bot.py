# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from io import StringIO
import csv
import requests

import tweepy
import time
import re
import random
from datetime import date, datetime

import warnings
warnings.simplefilter(action = 'ignore')

# -------------------

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

username = '@RegressTrio'
companies_file = 'companies.txt'
last_id_file = 'last_mention_id.txt'
sleep_time = 10
n_tweets = 4
prevision_time_hour = 8
emojis = '👼🏻💁🙇️'

def read_file(file_to_open):
    file = open(file_to_open, 'r')
    if file_to_open == last_id_file:
        read_lines = file.readlines()[0]
        return read_lines
    elif file_to_open == companies_file:
        read_lines = [line.strip().split(',') for line in file][0]
        return read_lines
    file.close()

def write_file(file_to_open, text):
    file = open(file_to_open, 'w')
    file.writelines(text)
    file.close()
    
def get_original_df(company):
    download = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1582685557&period2=1614307957&interval=1d&events=history&includeAdjustedClose=true'
    company = company
    download_company = download.format(company)
    response = requests.get(download_company)
    file = StringIO(response.text)
    reader = csv.reader(file)
    data = list(reader)
    original_df = pd.DataFrame(data[1:], columns = data[0])
    
    return original_df

def cleaned_original_df(original_df):
    df = original_df[original_df['Open'] != 'null']
    df['Date'] = pd.to_datetime(df['Date'])
    df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].astype('float')
    df = df.drop('Adj Close', axis = 1)
    
    return df

# -------------------

while True:
    # Searches for new mentions for each 20 seconds
    time.sleep(sleep_time)
    now = str(datetime.now())
    
    # Opens the 'Mention_id.txt' file and read the id of the last mentioned tweet read
    last_read_tweet = read_file(last_id_file)
    # Read the mentions since the last mentioned tweet read and write the newest one on the file
    my_new_mentions = api.mentions_timeline(since_id = last_read_tweet, count = n_tweets)
    
    #Look for new mentions
    if len(my_new_mentions) == 0:
        print("\n{}\nYou don't have new mentions".format(now))
    else:
        print("\n{}\nYou have a new mention!".format(now))
        # Write the last mention id on the 'Mention_id.txt' file, to store the last seen tweet
        write_file(last_id_file, str(my_new_mentions[0].id))
        # Get the companies that we predict, reading the 'Companies.txt' file
        companies = read_file(companies_file)
        
        # Look for new mentions that contains with '@RegressTrio "', that means that some user wants to register a new company to predict
        new_companies = []
        for mention in my_new_mentions:
            if re.search('{} ".*"'.format(username), mention.text) != None:
                # new_company contains the registered company in uppercase
                new_company = ((re.search('".*"', mention.text).group(0))[1:-1]).upper() + '.SA'
                # Verifies if the company is in companies
                if new_company in companies:
                    print('The new mention contains a company that is already on the list ({}).'.format(new_company))
                    tweet_new_company = '@{} Já tweetamos previsões de {} :D\n\n{}'.format(mention.user.screen_name, new_company, emojis)
                    print('New tweet:\n{}'.format(tweet_new_company))
                    api.create_favorite(str(mention.id)) # Favs the mention
                    api.update_status(tweet_new_company, in_reply_to_status_id = str(mention.id)) # Reply the mention
                else:
                    print('The new mentions has a new company for our predictions ({}).'.format(new_company))
                    # Searches the company in Yahoo Finance
                    original_df = get_original_df(new_company)
                    if (len(original_df) > 0): # If the company is found
                        new_companies.append(new_company)
                        tweet_new_company = 'Nova ação para análise cadastrada por @{}:\n{} ;)\n\n{}'.format(mention.user.screen_name, new_company, emojis)
                        print('New tweet:\n{}'.format(tweet_new_company))
                        api.create_favorite(str(mention.id)) # Favs the mention
                        api.update_status(tweet_new_company) # Reply the mention
                    else: # If the company is not found
                        tweet_new_company = 'Oi @{}!\nNão encontramos essa ação: {} :(\nVocê digitou certo?\n\n{}'.format(mention.user.screen_name, new_company, emojis)
                        print('New tweet:\n{}'.format(tweet_new_company))
                        api.create_favorite(str(mention.id)) # Favs the mention
                        api.update_status(tweet_new_company, in_reply_to_status_id = str(mention.id)) # Reply the mention
            elif re.search('{} lista'.format(username), mention.text) != None:
                companies_names = ', '.join(sorted(companies)) # Get a string with the name of the companies
                tweet_companies = 'Eai @{}!\nJá tweetamos previsões dessas ações: {}\nVocê pode pedir uma nova pra gente se quiser!\n\n{}'.format(mention.user.screen_name, companies_names, emojis)
                print('New tweet:\n{}'.format(tweet_companies))
                api.create_favorite(str(mention.id)) # Favs the mention
                api.update_status(tweet_companies, in_reply_to_status_id = str(mention.id)) # Reply the mention
            else:
                api.create_favorite(str(mention.id)) # Favs the mention
            # Adds the new companies in the 'Companies.txt' file
            for new_company in new_companies:
                companies.append(new_company)
            write_file(companies_file, ','.join(companies))

    # -------------------

    # If it's time to tweet (8h00 every day, except weekends), we tweet
    if not((datetime.now().hour == prevision_time_hour) & (datetime.now().minute == 0) & (date.today().weekday() in [0, 1, 2, 3, 4])):
        print("It's not prevision time")
    else:
        companies = read_file(companies_file)
        for company in companies:
            original_df = get_original_df(company = company)
            df = cleaned_original_df(original_df  = original_df)
            
            # Adds a new variable, 'Next Day Close'
            df['Next Day Close'] = df['Close'].shift(-1)
            df = df.dropna()
            df = df.reset_index().drop(['index'], axis = 1)

            # Get the features and the label
            X1_train = df.drop(['Date', 'Next Day Close'], axis = 1)
            y1_train = df['Next Day Close']

            # The hyperparameters are selected on the .ipynb file
            # Fit and transform a scaler on the features
            from sklearn.preprocessing import StandardScaler
            scaler1 = StandardScaler()
            X1_train = scaler1.fit_transform(X1_train)

            # Fit a SGD model to the data
            from sklearn.linear_model import SGDRegressor
            sgd1 = SGDRegressor(alpha = 0.01)
            sgd1.fit(X1_train, y1_train)

            # Fit a Linear Support Vector Regressor to the data
            from sklearn.svm import LinearSVR
            svr1 = LinearSVR(C = 0.7)
            svr1.fit(X1_train, y1_train)
            
            # Fita Linear Regression to the data
            from sklearn.linear_model import LinearRegression
            lr1 = LinearRegression()
            lr1.fit(X1_train, y1_train)

            # Adds a new variable 'Next 5th Day Close'
            df['Next 5th Day Close'] = df['Close'].shift(-5)
            df = df.dropna()
            df = df.reset_index().drop(['index'], axis = 1)

            # Analogous
            X5_train = df.drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
            y5_train = df['Next 5th Day Close']

            scaler5 = StandardScaler()
            X5_train = scaler5.fit_transform(X5_train)

            sgd5 = SGDRegressor(alpha = 1.6)
            sgd5.fit(X5_train, y5_train)

            svr5 = LinearSVR(C = 0.06)
            svr5.fit(X5_train, y5_train)
            
            lr5 = LinearRegression()
            lr5.fit(X5_train, y5_train)

            # Get the 'new_df', that will be used for the predictions of today
            original_df = get_original_df(company = company)
            new_df = cleaned_original_df(original_df  = original_df).tail(1)

            # Get the variables of the predictions for the tweet
            data = new_df.drop('Date', axis = 1).iloc[0]
            fechamento_hoje = round(float(data[3]), 2)
            sgd1_p = round(sgd1.predict(scaler1.transform([data]))[0], 2)
            svr1_p = round(svr1.predict(scaler1.transform([data]))[0], 2)
            lr1_p = round(lr1.predict(scaler1.transform([data]))[0], 2)
            sgd5_p = round(sgd5.predict(scaler5.transform([data]))[0], 2)
            svr5_p = round(svr5.predict(scaler5.transform([data]))[0], 2)
            lr5_p = round(lr5.predict(scaler5.transform([data]))[0], 2)

            # Tweets the predictions
            intro_tweets = ['Sobre {}, que fechou ontem com R$ {}, a gente tem umas previsões:\n'.format(company[:-3], fechamento_hoje),
                           '{} fechou ontem em R$ {}. Trouxemos nossas previsões para alguns dias pra você :D\n'.format(company[:-3], fechamento_hoje),
                           'Se liga nas nossa previsões pra {}, que fechou ontem em R$ {}\n'.format(company[:-3], fechamento_hoje)]
            predictions_text = "{}\n{}\nFechamento de hoje\n SGD: R$ {}\n SVR: R$ {}\n LR: R$ {}\n\nFechamento daqui 5 dias\n SGD: R$ {}\n SVR: R$ {}\n LR: R$ {}\n\n{}".format(
            date.today(), random.choice(intro_tweets), sgd1_p, svr1_p, lr1_p, sgd5_p, svr5_p, lr5_p, emojis)
            print('New tweet:\n{}'.format(predictions_text))
            api.update_status(predictions_text)
        # Wait 60 seconds to don't get into a new loop in 8h00
        time.sleep(60)
