import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from io import StringIO
import csv
import requests

import tweepy
import random
from datetime import date

import warnings
warnings.simplefilter(action='ignore')

CONSUMER_KEY = '0uyHpCxS1I8SKdNCgYLf2PS4G'
CONSUMER_SECRET = 'Dw0gsC1WBw9jSDfkHvm4h2aqehdU5UFytUcb4Vp9yAyPABYnNc'
ACCESS_KEY = '1365099323864862723-2w9OWWFhkCTNC7TKGapDTed8R7KU5S'
ACCESS_SECRET = 'TVNUa1gtQGjD0dMuwnyahAINMyvsdrUKUxJUDqhoKTQpm'

username = 'Zenkomes'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

my_tweets = api.user_timeline(user_id = username, exclude_replies = True)
my_mentions = api.mentions_timeline()

file = open('Mentions_id.txt', 'r')
last_read_tweet = file.readlines()[0]
file.close()

my_new_mentions = api.mentions_timeline(since_id = last_read_tweet)
if len(my_new_mentions) > 0:
    file = open('Mentions_id.txt', 'w')
    file.writelines(str(my_new_mentions[0].id))
    file.close()
    
new_companies = []
for mention in my_new_mentions:
    if '@Zenkomes "' in mention.text:
        new_company = (re.search('"(.*)"', mention.text).group(0))
        new_companies.append(str(new_company[1:-1]).upper() + '.SA')
        tweet_new_company = 'Nova ação para análise cadastrada: {} ;)'.format(str(new_company[1:-1]).upper())
        print(tweet_new_company)
        api.update_status(tweet_new_company)

companies_txt = open('Companies.txt', 'r')
companies = [line.strip().split(',') for line in companies_txt][0]
companies_txt.close() 

for new_company in new_companies:
    companies.append(new_company)
    
file = open('Companies.txt', 'w')
file.writelines(','.join(companies))
file.close()

if (str(date.today()) in my_tweets[0].text):
    print('Fim de código, já foram tweetadas as previsões de hoje.')
else:
    download = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1582685557&period2=1614307957&interval=1d&events=history&includeAdjustedClose=true'
    for company in companies:
        download_company = download.format(company)
        response = requests.get(download_company)

        file = StringIO(response.text)
        reader = csv.reader(file)
        data = list(reader)
        original_df = pd.DataFrame(data[1:], columns = data[0])
        
        df = original_df[original_df['Open'] != 'null']
        df['Date'] = pd.to_datetime(df['Date'])
        df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].astype('float')
        df = df.drop('Adj Close', axis = 1)

        if df.iloc[-1][1] == 0:
            
            sad_tweets = ['O Yahoo Finance (de onde a gente coleta os dados) ainda não atualizou eles pra nós :(',
                         'Pô, Yahoo, acelera e manda esses dados pra nós logo :(',
                         'Sem dados, sem previsões, hum. Estamos esperando os dados do Yahoo, gente.',
                         'Decepcionados com o Yahoo que demora. Apenas.',
                         'Não dependam do Yahoo Finance. Eles demorar demais pra carregar os dados pra nós. Quando eles atualizarem, a gente manda as previsões :D']
            
            tweet_text = random.choice(sad_tweets)
            print(tweet_text)
            api.update_status(tweet_text)
            break
        else:
            df['Next Day Close'] = df['Close'].shift(-1)

            df = df.dropna()
            df = df.reset_index().drop(['index'], axis = 1)

            #df

            X1_train = df.drop(['Date', 'Next Day Close'], axis = 1)
            y1_train = df['Next Day Close']

            from sklearn.preprocessing import StandardScaler

            scaler1 = StandardScaler()
            X1_train = scaler1.fit_transform(X1_train)

            from sklearn.linear_model import LinearRegression

            lr1 = LinearRegression()
            lr1.fit(X1_train, y1_train)

            from sklearn.svm import LinearSVR

            best_svr1 = LinearSVR(C = 1.9849999999999997)
            best_svr1.fit(X1_train, y1_train)

            from sklearn.ensemble import RandomForestRegressor

            best_rfr1 = RandomForestRegressor(n_estimators = 1000, max_depth = 50)
            best_rfr1.fit(X1_train, y1_train)

            df['Next 5th Day Close'] = df['Close'].shift(-5)

            df = df.dropna()
            df = df.reset_index().drop(['index'], axis = 1)

            #df

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

            new_df = original_df[original_df['Open'] != 'null']
            new_df['Date'] = pd.to_datetime(new_df['Date'])
            new_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = new_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].astype('float')
            new_df = new_df.drop('Adj Close', axis = 1)

            new_df = new_df.tail(1)
            #new_df

            data = new_df.drop('Date', axis = 1).iloc[0]
            fechamento_hoje = data[3]
            lr1_p = round(lr1.predict(scaler1.transform([data]))[0], 3)
            svr1_p = round(best_svr1.predict(scaler1.transform([data]))[0], 3)
            rfr1_p = round(best_rfr1.predict(scaler1.transform([data]))[0], 3)
            lr5_p = round(lr5.predict(scaler5.transform([data]))[0], 3)
            svr5_p = round(best_svr5.predict(scaler5.transform([data]))[0], 3)
            rfr5_p = round(best_rfr5.predict(scaler5.transform([data]))[0], 3)

            intro_tweets = [f'Sobre {company[:-3]}, que fechou com R$ {fechamento_hoje}, a gente tem umas previsões:',
                           f'{company[:-3]} fechou hoje em R$ {fechamento_hoje}. Trouxemos nossas previsões para alguns dias pra você :D',
                           f'Se liga nas nossa previsões pra {company[:-3]}, que fechou hoje em R$ {fechamento_hoje}']
            
            tweet_text = f"{date.today()}\n{random.choice(intro_tweets)}\n\nAmanhã\n Linear Regression: R$ {lr1_p}\n SVR: R$ {svr1_p}\n Random Forest: R$ {rfr1_p}\n\nDaqui 5 dias\n Linear Regression: R$ {lr5_p}\n SVR: R$ {svr5_p}\n Random Forest: R$ {rfr5_p}"

            print(tweet_text)
            api.update_status(tweet_text)