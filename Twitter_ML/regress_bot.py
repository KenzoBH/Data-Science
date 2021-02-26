import pandas as pd
import numpy as np

from io import StringIO
import csv
import requests

import tweepy
import os
from os import environ
import time
import re
import random
from datetime import date, datetime

import warnings
warnings.simplefilter(action='ignore')

# -------------------

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

username = 'RegressTrio'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# -------------------
while True:
    # Searches for new mentions for each 20 seconds
    time.sleep(20)
    
    # Collect the last tweets of our account and the last tweets that mentions @TrioRegress
    my_tweets = api.user_timeline(user_id = username, exclude_replies = True, count = 5)
    my_mentions = api.mentions_timeline(count = 5)

    # Opens the 'Mentions_id.txt' file and read the id of the last mentioned tweet read
    file = open('Mentions_id.txt', 'r')
    last_read_tweet = file.readlines()[0]
    file.close()

    # Read the mentions since the last mentioned tweet read and write the newest one on the file
    my_new_mentions = api.mentions_timeline(since_id = last_read_tweet, count = 5)
    if len(my_new_mentions) == 0:
        print("You don't have new mentions")
    else:
        print("You have a new mention!")
        file = open('Mentions_id.txt', 'w')
        file.writelines(str(my_new_mentions[0].id))
        file.close()

        # Get the companies that we predict, reading the 'Companies.txt' file
        companies_txt = open('Companies.txt', 'r')
        companies = [line.strip().split(',') for line in companies_txt][0]
        companies_txt.close()

        # Look for new mentions that contains with '@RegressTrio "', that means that some user registered a new company to predict
        new_companies = []
        for mention in my_new_mentions:
            if ('@' + username + ' "') in mention.text:
                new_company = (re.search('"(.*)"', mention.text).group(0))
                if (str(new_company[1:-1]).upper() + '.SA') in companies:
                    print('The new mention contains a company that is already on the list.')
                    tweet_new_company = '{}\nJá tweetamos previsões de {} :D'.format(date.today(), str(new_company[1:-1]).upper())
                    print(tweet_new_company)
                    print()
                    api.update_status(tweet_new_company)
                else:
                    print('The new mentions has a new company for our predictions.')
                    download = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1582685557&period2=1614307957&interval=1d&events=history&includeAdjustedClose=true'
                    company = str(new_company[1:-1]).upper() + '.SA'
                    download_company = download.format(company)
                    response = requests.get(download_company)
                    file = StringIO(response.text)
                    reader = csv.reader(file)
                    data = list(reader)
                    original_df = pd.DataFrame(data[1:], columns = data[0])
                    if (len(original_df) > 0):
                        new_companies.append(str(new_company[1:-1]).upper() + '.SA')
                        tweet_new_company = '{}\nNova ação para análise cadastrada: {} ;)'.format(date.today(), str(new_company[1:-1]).upper())
                        print(tweet_new_company)
                        print()
                        api.update_status(tweet_new_company)
                    else:
                        tweet_new_company = '{}\nNão encontramos essa ação: {} :(\nVeja se você digitou corretamente.'.format(date.today(), str(new_company[1:-1]).upper())
                        print(tweet_new_company)
                        print()
                        api.update_status(tweet_new_company)

        # Adds the new companies in the 'Companies.txt' file
        for new_company in new_companies:
            companies.append(new_company)
        file = open('Companies.txt', 'w')
        file.writelines(','.join(companies))
        file.close()

    # -------------------

    # If we already tweeted today, the code ends, else, we continue the app
    if not((datetime.now().hour == 8) & (datetime.now().minute == 0) & (date.today().weekday() in [0, 1, 2, 3, 4])):
        print("It's not tweet time or it's weekend")
    else:
        companies_txt = open('Companies.txt', 'r')
        companies = [line.strip().split(',') for line in companies_txt][0]
        companies_txt.close()

        # Get the link of the download of the data, with a mask that will be filled with the company
        download = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1582685557&period2=1614307957&interval=1d&events=history&includeAdjustedClose=true'
        for company in companies:
            # Update the downlad link for the company and get the data, saving in the 'original_df' variable
            download_company = download.format(company)
            response = requests.get(download_company)
            file = StringIO(response.text)
            reader = csv.reader(file)
            data = list(reader)
            original_df = pd.DataFrame(data[1:], columns = data[0])

            # 'df' is the cleaned 'original_df'
            df = original_df[original_df['Open'] != 'null']
            df['Date'] = pd.to_datetime(df['Date'])
            df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].astype('float')
            df = df.drop('Adj Close', axis = 1)

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

            # Fit a Linear Regression (Lineu Regis) to the data
            from sklearn.linear_model import LinearRegression
            lr1 = LinearRegression()
            lr1.fit(X1_train, y1_train)

            # Fit a Linear Support Vector Regressor (Samuel Victor Resende) to the data
            from sklearn.svm import LinearSVR
            best_svr1 = LinearSVR(C = 1.9849999999999997)
            best_svr1.fit(X1_train, y1_train)

            # Fit a Random Forest Regressor (Rannah dom Fontes) to the data
            from sklearn.ensemble import RandomForestRegressor
            best_rfr1 = RandomForestRegressor(n_estimators = 1000, max_depth = 50)
            best_rfr1.fit(X1_train, y1_train)

            # Adds a new variable 'Next 5th Day Close'
            df['Next 5th Day Close'] = df['Close'].shift(-5)
            df = df.dropna()
            df = df.reset_index().drop(['index'], axis = 1)

            # Analogous
            X5_train = df.drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
            y5_train = df['Next 5th Day Close']

            scaler5 = StandardScaler()
            X5_train = scaler5.fit_transform(X5_train)

            lr5 = LinearRegression()
            lr5.fit(X5_train, y5_train)

            best_svr5 = LinearSVR(C = 16.26)
            best_svr5.fit(X5_train, y5_train)

            best_rfr5 = RandomForestRegressor(n_estimators = 1000, max_depth = 10)
            best_rfr5.fit(X5_train, y5_train)

            # Get the 'new_df', that will be used for the predictions of today
            new_df = original_df[original_df['Open'] != 'null']
            new_df['Date'] = pd.to_datetime(new_df['Date'])
            new_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = new_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].astype('float')
            new_df = new_df.drop('Adj Close', axis = 1)
            new_df = new_df.tail(1)

            # Get the variables of the predictions for the tweet
            data = new_df.drop('Date', axis = 1).iloc[0]
            fechamento_hoje = round(float(data[3]), 3)
            lr1_p = round(lr1.predict(scaler1.transform([data]))[0], 3)
            svr1_p = round(best_svr1.predict(scaler1.transform([data]))[0], 3)
            rfr1_p = round(best_rfr1.predict(scaler1.transform([data]))[0], 3)
            lr5_p = round(lr5.predict(scaler5.transform([data]))[0], 3)
            svr5_p = round(best_svr5.predict(scaler5.transform([data]))[0], 3)
            rfr5_p = round(best_rfr5.predict(scaler5.transform([data]))[0], 3)

            # Tweets the predictions
            intro_tweets = [f'Sobre {company[:-3]}, que fechou ontem com R$ {fechamento_hoje}, a gente tem umas previsões:\n',
                           f'{company[:-3]} fechou ontem em R$ {fechamento_hoje}. Trouxemos nossas previsões para alguns dias pra você :D\n',
                           f'Se liga nas nossa previsões pra {company[:-3]}, que fechou ontem em R$ {fechamento_hoje}\n']
            tweet_text = f"{date.today()}\n{random.choice(intro_tweets)}\nHoje\n LR: R$ {lr1_p}\n SVR: R$ {svr1_p}\n RandomF: R$ {rfr1_p}\n\nDaqui 5 dias\n LR: R$ {lr5_p}\n SVR: R$ {svr5_p}\n RandomF: R$ {rfr5_p}"
            print(tweet_text)
            print()
            api.update_status(tweet_text)
        # Wait 60 seconds to don't get into a new loop in 8h00
        time.sleep(60)
