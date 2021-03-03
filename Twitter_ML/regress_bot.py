# -*- coding: utf-8 -*-

from functions import read_file, write_file, verify_company, get_df, fit_best_model, train_best_models, get_predictions, model_map

import pandas as pd
import numpy as np

import tweepy
import time
import re
import random
from datetime import date, datetime

from sklearn.linear_model import SGDRegressor, Ridge
from sklearn.svm import LinearSVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore')

# VARIABLES AND TWEETER KEYS --------------------

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

username = '@RegressML'
companies_file = 'companies.txt'
last_id_file = 'last_mention_id.txt'
sleep_time = 20
n_tweets = 4
prevision_time_hour = 8
prevision_time_minute = 0
emojis = 'Regress'
link = 'https://finance.yahoo.com/quote/{}/history?p={}'

# SEARCHING FOR MENTIONS ---------------------------

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
        
        # Look for new mentions that contains with '@RegressML "', that means that some user wants to register a new company to predict
        new_companies = []
        for mention in my_new_mentions:
            if re.search('{} ".*"'.format(username), mention.text) != None:
                # new_company contains the registered company in uppercase
                new_company = ((re.search('".*"', mention.text).group(0))[1:-1]).upper() + '.SA'
                # Verifies if the company is in companies
                if new_company in companies:
                    print('The new mention contains a company that is already on the list ({}).'.format(new_company))
                    tweet_new_company = '@{} Já tweetamos previsões de {} :D\n\n{}'.format(mention.user.screen_name, new_company, emojis)
                    print('\n-----\nNew tweet:\n{}\n-----\n'.format(tweet_new_company))
                    api.create_favorite(str(mention.id)) # Favs the mention
                    api.update_status(tweet_new_company, in_reply_to_status_id = str(mention.id)) # Reply the mention
                else:
                    print('The new mentions has a new company for our predictions ({}).'.format(new_company))
                    # Searches the company in Yahoo Finance
                    exists = verify_company(new_company, link)
                    if exists: # If the company is found
                        new_companies.append(new_company)
                        tweet_new_company = 'Nova ação para análise cadastrada por @{}:\n{} ;)\n\n{}'.format(mention.user.screen_name, new_company, emojis)
                        print('\n-----\nNew tweet:\n{}\n-----\n'.format(tweet_new_company))
                        api.create_favorite(str(mention.id)) # Favs the mention
                        api.update_status(tweet_new_company) # Reply the mention
                    else: # If the company is not found
                        tweet_new_company = 'Oi @{}!\nNão encontramos essa ação: {} :(\nVocê digitou certo?\n\n{}'.format(mention.user.screen_name, new_company, emojis)
                        print('\n-----\nNew tweet:\n{}\n-----\n'.format(tweet_new_company))
                        api.create_favorite(str(mention.id)) # Favs the mention
                        api.update_status(tweet_new_company, in_reply_to_status_id = str(mention.id)) # Reply the mention
            elif re.search('{} lista'.format(username), mention.text) != None:
                companies_names = ', '.join(sorted(companies)) # Get a string with the name of the companies
                tweet_companies = 'Eai @{}!\nJá tweetamos previsões dessas ações: {}\n\n{}'.format(mention.user.screen_name, companies_names, emojis)
                print('\n-----\nNew tweet:\n{}\n-----\n'.format(tweet_companies))
                api.create_favorite(str(mention.id)) # Favs the mention
                api.update_status(tweet_companies, in_reply_to_status_id = str(mention.id)) # Reply the mention
            else:
                api.create_favorite(str(mention.id)) # Favs the mention
            # Adds the new companies in the 'Companies.txt' file
            for new_company in new_companies:
                companies.append(new_company)
            write_file(companies_file, ','.join(companies))

    # MODELS AND PREDICTIONS TWEETS --------------------

    # If it's time to tweet (8h00 every day, except weekends), we tweet
    if not((datetime.now().hour == prevision_time_hour) & (datetime.now().minute == prevision_time_minute) & (date.today().weekday() in [0, 1, 2, 3, 4])):
        print("It's not prevision time")
    else:
        print("It's prevision time")
        companies = read_file(companies_file)
        for company in sorted(companies):
            # Get the data from the link
            print('Getting the data from web ({})...'.format(company))
            df, today_data, y1, y5 = get_df(company, link)
            today_close = round(float(list(today_data)[4]), 2)

            print('Training models...')
            # Calling a function that trains the models and get the best hyperparameters of each one - and returns the best 3 models
            best_models1, best_models5 = fit_best_model([
                SGDRegressor, Ridge, LinearSVR, DecisionTreeRegressor, RandomForestRegressor, AdaBoostRegressor, KNeighborsRegressor],
                [np.arange(0.00001, 50, 0.05), np.arange(0.00002, 5, 0.05), np.arange(0.03, 15, 0.005),
                np.arange(1, 1000, 10), np.arange(2, 100, 10), np.arange(3, 100, 10), np.arange(1, 20, 1)],
                df)
            
            # Gettin their predictions
            predictions1, predictions5 = train_best_models(best_models1, best_models5, df)
            mdl1_1, mdl1_1_p, mdl1_2, mdl1_2_p, mdl1_3, mdl1_3_p, mdl5_1, mdl5_1_p, mdl5_2, mdl5_2_p, mdl5_3, mdl5_3_p = get_predictions(predictions1, predictions5)
            
            ps = [mdl1_1_p, mdl1_2_p, mdl1_3_p, mdl5_1_p, mdl5_2_p, mdl5_3_p]
            mdls_names = [mdl1_1, mdl1_2, mdl1_3, mdl5_1, mdl5_2, mdl5_3]
            mdls = []
            for model in mdls_names:
                mdls.append(model_map(model))

            # Tweeting our predictions
            intro_tweets = ['Sobre {}, que fechou ontem com R$ {}, a gente tem umas previsões:\n'.format(company[:-3], today_close),
                   '{} fechou ontem em R$ {}. Trouxemos nossas previsões para alguns dias pra você :D\n'.format(company[:-3], today_close),
                   'Se liga nas nossa previsões pra {}, que fechou ontem em R$ {}\n'.format(company[:-3], today_close)]
            predictions_text = "{}\n{}\nFechamento de hoje\n {}: R$ {}\n {}: R$ {}\n {}: R$ {}\nFechamento daqui 5 dias\n {}: R$ {}\n {}: R$ {}\n {}: R$ {}".format(date.today(), random.choice(intro_tweets), mdls[0], ps[0], mdls[1], ps[1], mdls[2], ps[2], mdls[3], ps[3], mdls[4], ps[4], mdls[5], ps[5])
            print('\n-----\nNew tweet:\n{}\n-----\n'.format(predictions_text))
            api.update_status(predictions_text)

        # Wait 60 seconds to don't get into a new loop in 8h00
        time.sleep(60)
