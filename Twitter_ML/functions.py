import pandas as pd
import numpy as np

from sklearn.linear_model import SGDRegressor, Ridge
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore')

def read_file(file_to_open):
    file = open(file_to_open, 'r')
    if file_to_open == 'last_mention_id.txt':
        read_lines = file.readlines()[0]
        return read_lines
    elif file_to_open == 'companies.txt':
        read_lines = [line.strip().split(',') for line in file][0]
        return read_lines
    file.close()

def write_file(file_to_open, text):
    file = open(file_to_open, 'w')
    file.writelines(text)
    file.close()

def verify_company(company, link):
    link_company = link.format(company, company)
    try:
        pd.read_html(link_company)[0]
        return True
    except ValueError:
        return False

def get_df(company, link):
    link_company = link.format(company, company)
    df = pd.read_html(link_company)[0].drop('Adj Close**', axis = 1)
    df = df[~df['Open'].str.contains('Dividend')]
    df = df[df['Volume'] != '-'].head(50)
    df['Date'] = pd.to_datetime(df['Date'])

    today_data = df.iloc[0]
    today_data[['Open', 'High', 'Low', 'Close*', 'Volume']] = today_data[['Open', 'High', 'Low', 'Close*', 'Volume']].astype('float')
    print(today_data)

    df = df.iloc[1:]
    df[['Open', 'High', 'Low', 'Close*', 'Volume']] = df[['Open', 'High', 'Low', 'Close*', 'Volume']].astype('float')
    df['Next Day Close'] = df['Close*'].shift(1)
    df['Next 5th Day Close'] = df['Close*'].shift(5)

    return df, today_data, df['Next Day Close'], df['Next 5th Day Close']

def add_labels(df):
    df['Next Day Close'] = df['Close*'].shift(1)
    df['Next 5th Day Close'] = df['Close*'].shift(5)
    df = df.dropna()
    df = df.reset_index().drop(['index'], axis = 1)

    return df

def fit_best_model(df, split_line, model, hp, range_hp, time, X, y, today_data):
    X_train = df[:split_line].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
    X_test = df[split_line:].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    y_1_train = df[:split_line]['Next Day Close']
    y_1_test = df[split_line:]['Next Day Close']

    y_5_train = df[:split_line]['Next 5th Day Close']
    y_5_test = df[split_line:]['Next 5th Day Close']
    
    if time == 1:
        train_data = y_1_train
        test_data = y_1_test
    else:
        train_data = y_5_train
        test_data = y_5_test
    
    metric_mdl = []
    for x in range_hp:
        if model == SGDRegressor or model == Ridge:
            mdl = model(alpha = x)
        elif model == LinearSVR:
            mdl = model(C = x)
        elif model == RandomForestRegressor:
            mdl = model(max_depth = x)
            
        mdl.fit(X_train, train_data)
        pred_mdl = mdl.predict(X_test)
        
        rmse_mdl = np.sqrt(mean_squared_error(test_data, pred_mdl))
        metric_mdl.append([rmse_mdl, x])

    if model == SGDRegressor or model == Ridge:
        mdl = model(alpha = min(metric_mdl)[1])
    elif model == LinearSVR:
        mdl = model(C = min(metric_mdl)[1])
    elif model == RandomForestRegressor:
        mdl = model(max_depth = min(metric_mdl)[1])
    
    scaler = StandardScaler()
    if time == 1:
        X = X.drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1).dropna().iloc[1:]
        X = scaler.fit_transform(X)
        mdl.fit(X, y.dropna())
    else:
        df = df.drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
        df = scaler.fit_transform(df)
        mdl.fit(df, y.dropna())
    
    new_data = scaler.transform([today_data.drop('Date')])
    mdl_p = mdl.predict(new_data)[0]

    return mdl, round(mdl_p, 2)