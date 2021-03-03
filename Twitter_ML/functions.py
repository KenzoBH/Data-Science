import pandas as pd
import numpy as np
import re

from sklearn.linear_model import SGDRegressor, Ridge
from sklearn.svm import LinearSVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
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

    df[['Open', 'High', 'Low', 'Close*', 'Volume']] = df[['Open', 'High', 'Low', 'Close*', 'Volume']].astype('float')
    df['Next Day Close'] = df['Close*'].shift(1)
    df['Next 5th Day Close'] = df['Close*'].shift(5)

    return df, today_data, df['Next Day Close'], df['Next 5th Day Close']

def fit_best_model(models, ranges, df):
    split_line = 10
    time = [1, 5]
    best_models = []
 
    for time in time:
        
        if time == 1:
            best_models1 = []
            print('Training models for the next day')
            train_features = df[split_line:].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
            test_features = df[1:split_line].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
            train_label = df[split_line:]['Next Day Close']
            test_label = df[1:split_line]['Next Day Close']
        else:
            best_models5 = []
            print('Training models for the 5th next day')
            train_features = df[split_line:].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
            test_features = df[5:split_line].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
            train_label = df[split_line:]['Next 5th Day Close']
            test_label = df[5:split_line]['Next 5th Day Close']
            
        scaler = StandardScaler()
        train_features = scaler.fit_transform(train_features)
        test_features = scaler.transform(test_features)

        for model in range(len(models)): 
            rmses = []
            for hp in ranges[model]:
                
                if models[model] in [SGDRegressor, Ridge]:
                    mdl = models[model](alpha = hp)
                elif models[model] in [LinearSVR]:
                    mdl = models[model](C = hp)
                elif models[model] in [KNeighborsRegressor]:
                    mdl = models[model](n_neighbors = hp)
                elif models[model] in [DecisionTreeRegressor]:
                    mdl = models[model](max_depth = hp)
                elif models[model] in [RandomForestRegressor, AdaBoostRegressor]:
                    mdl = models[model](n_estimators = hp)
                    
                mdl.fit(train_features, train_label)
                mdl_p = mdl.predict(test_features)
                mdl_rmse = np.sqrt(mean_squared_error(test_label, mdl_p))
                rmses.append([mdl_rmse, hp, mdl])
                 
            best_rmse = min(rmses)[0]
            best_hp = min(rmses)[1]
            best_model = min(rmses)[2]
            if time == 1:
                best_models1.append([best_rmse, best_hp, best_model])
            else:
                best_models5.append([best_rmse, best_hp, best_model])
            best_models.append(best_model)
    
    best_models1 = sorted(best_models1)[:3]
    best_models1 = [[model[2], re.findall(r"(.*)\(", str(model[2]))[0]] for model in best_models1]
    best_models5 = sorted(best_models5)[:3]
    best_models5 = [[model[2], re.findall(r"(.*)\(", str(model[2]))[0]] for model in best_models5]
    
    return best_models1, best_models5

def train_best_models(best_models1, best_models5, df):
    time = [1, 5]
    predictions1 = []
    predictions5 = []
    
    prediction_features = df.iloc[0].drop(['Date', 'Next Day Close', 'Next 5th Day Close'])
    for time in time:
        
        if time == 1:
            train_features = df[1:].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
            train_label = df[1:]['Next Day Close']
            
            scaler = StandardScaler()
            train_features = scaler.fit_transform(train_features)
            prediction_features = scaler.transform([prediction_features])
            
            for model in best_models1:
                model[0].fit(train_features, train_label)
                model_p = model[0].predict(prediction_features)
                predictions1.append([model[1], round(model_p[0], 2)])
        else:
            train_features = df[5:].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
            train_label = df[5:]['Next 5th Day Close']
            
            scaler = StandardScaler()
            train_features = scaler.fit_transform(train_features)
            
            for model in best_models5:
                model[0].fit(train_features, train_label)
                model_p = model[0].predict(prediction_features)
                predictions5.append([model[1], round(model_p[0], 2)])
                
    return predictions1, predictions5

def get_predictions(predictions1, predictions5):
    
    mdl1_1 = predictions1[0][0]
    mdl1_1_p = predictions1[0][1]
    mdl1_2 = predictions1[1][0]
    mdl1_2_p = predictions1[1][1]
    mdl1_3 = predictions1[2][0]
    mdl1_3_p = predictions1[2][1]
    
    mdl5_1 = predictions5[0][0]
    mdl5_1_p = predictions5[0][1]
    mdl5_2 = predictions5[1][0]
    mdl5_2_p = predictions5[1][1]
    mdl5_3 = predictions5[2][0]
    mdl5_3_p = predictions5[2][1]
    
    return mdl1_1, mdl1_1_p, mdl1_2, mdl1_2_p, mdl1_3, mdl1_3_p, mdl5_1, mdl5_1_p, mdl5_2, mdl5_2_p, mdl5_3, mdl5_3_p

def model_map(mdl):
    
    if mdl == 'SGDRegressor':
        mdl = 'SGD'
    elif mdl == 'Ridge':
        mdl = 'Ridge'
    elif mdl == 'LinearSVR':
        mdl = 'SVR'
    elif mdl == 'KNeighborsRegressor':
        mdl = 'KNN'
    elif mdl == 'DecisionTreeRegressor':
        mdl = 'DT'
    elif mdl == 'RandomForestRegressor':
        mdl = 'RF'
    elif mdl == 'AdaBoostRegressor':
        mdl = 'Ada'

    return mdl