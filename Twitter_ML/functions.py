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

from skopt import gp_minimize

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

# Web Scraping and cleaning
def get_data_from_web(company, link):
    
    link_company = link.format(company, company)
    df = pd.read_html(link_company)[0].drop('Adj Close**', axis = 1)
    df = df[~df['Open'].str.contains('Dividend')]
    df = df[df['Volume'] != '-'].head(50)
    df['Date'] = pd.to_datetime(df['Date'])

    df[['Open', 'High', 'Low', 'Close*', 'Volume']] = df[['Open', 'High', 'Low', 'Close*', 'Volume']].astype('float')
    df['Next Day Close'] = df['Close*'].shift(1)
    df['Next 5th Day Close'] = df['Close*'].shift(5)

    today_data = df.drop(['Next Day Close', 'Next 5th Day Close'], axis = 1).iloc[0]
    last_close = round(float(list(today_data)[4]), 2)
    
    return df, last_close

def get_data(df, split_line, time):

    train_features = df[split_line:].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
    test_features = df[time:split_line].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
   
    if time == 1:
        train_label = df[split_line:]['Next Day Close']
        test_label = df[1:split_line]['Next Day Close']
    else:
        train_label = df[split_line:]['Next 5th Day Close']
        test_label = df[5:split_line]['Next 5th Day Close']
        
        
    scaler = StandardScaler()
    train_features = scaler.fit_transform(train_features)
    test_features = scaler.transform(test_features)
    X1 = df.iloc[1:].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
    new_X1 = scaler.fit_transform(X1)
    X5 = df.iloc[5:].drop(['Date', 'Next Day Close', 'Next 5th Day Close'], axis = 1)
    new_X5 = scaler.fit_transform(X5)
    y1 = df.iloc[1:]['Next Day Close']
    y5 = df.iloc[5:]['Next 5th Day Close']
    
    last_data = df.iloc[0].drop(['Date', 'Next Day Close', 'Next 5th Day Close'])
    last_data_transformed = scaler.transform([last_data])
    
    return train_features, test_features, train_label, test_label, new_X1, y1, new_X5, y5, last_data_transformed

# This function fit a model to the training set and returns its RMSE
def get_rmse(mdl, train_features, train_label, test_features, test_label):
    mdl.fit(train_features, train_label)
    mdl_p = mdl.predict(test_features)
    rmse = np.sqrt(mean_squared_error(test_label, mdl_p))
    return rmse
        
# The following functions creates a model and returns its RMSE
params_sgd = [['squared_loss', 'huber', 'epsilon_insensitive', 'squared_epsilon_insensitive'],
              ['l1', 'l2', 'elasticnet'], (0.00001, 5), ['constant', 'optimal', 'invscaling', 'adaptive']]
              # loss, penalty, alpha, learning_rate
def train_sgd(params, train_features, train_label, test_features, test_label):
    mdl = SGDRegressor(loss = params[0], penalty = params[1], alpha = params[2], learning_rate = params[3])
    return get_rmse(mdl, train_features, train_label, test_features, test_label)

params_r = [(0.0001, 10), [True, False], [True, False],
            ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga']]
            # alpha, fit_intercept, normalize, solver
def train_r(params, train_features, train_label, test_features, test_label):
    mdl = Ridge(alpha = params[0], fit_intercept = params[1], normalize = params[2], solver = params[3])
    return get_rmse(mdl, train_features, train_label, test_features, test_label)

params_svr = [(0, 1), (0.00001, 50)]
              # epsilon, C
def train_svr(params, train_features, train_label, test_features, test_label):
    mdl = LinearSVR(epsilon = params[0], C = params[1])
    return get_rmse(mdl, train_features, train_label, test_features, test_label)

params_knn = [(1, 20), ['uniform', 'distance'], ['auto', 'ball_tree', 'kd_tree', 'brute']]
              # n_neighbors, weights, algorithm
def train_knn(params, train_features, train_label, test_features, test_label):
    mdl = KNeighborsRegressor(n_neighbors = params[0], weights = params[1], algorithm = params[2])
    return get_rmse(mdl, train_features, train_label, test_features, test_label)

params_dt = [['mse', 'friedman_mse', 'mae', 'poisson'], ['best', 'random'], (1, 500), (2, 300), (1, 300), (1, 5)]
             # criterion, splitter, max_depth, min_samples_split, min_samples_leaf, max_features
def train_dt(params, train_features, train_label, test_features, test_label):
    mdl = DecisionTreeRegressor(criterion = params[0], splitter = params[1], max_depth = params[2],
                                min_samples_split = params[3], min_samples_leaf = params[4], max_features = params[5])
    return get_rmse(mdl, train_features, train_label, test_features, test_label)
    
params_rf = [(10, 200), ['mse', 'mae'], (1, 500), (0.001, 0.5), (0.001, 0.5), (1, 5)]
             # n_estimators, criterion, max_depth, min_samples_split, min_samples_leaf, max_features
def train_rf(params, train_features, train_label, test_features, test_label):
    mdl = RandomForestRegressor(n_estimators = params[0], criterion = params[1], max_depth = params[2],
                                 min_samples_split = params[3], min_samples_leaf = params[4], max_features = params[5])
    return get_rmse(mdl, train_features, train_label, test_features, test_label)

params_ada = [(10, 200), (0.5, 5), ['linear', 'square', 'exponential']]
              # n_estimators, learning_rate, loss
def train_ada(params, train_features, train_label, test_features, test_label):
    mdl = AdaBoostRegressor(n_estimators = params[0], learning_rate = params[1], loss = params[2])
    return get_rmse(mdl, train_features, train_label, test_features, test_label)

def best_rmses(train_models):
    final_list = []
    for train_model in train_models:
        # para cada tupla do tipo (treinar_modelo, parâmetros), iremos otimizar o modelo desejado, retornando seus
        # melhores hiperarâmetros e o RMSE de cada um
        mdl_gp = gp_minimize(train_model[0], train_model[1], n_calls = 30, n_random_starts = 10)
        mdl_rmse = train_model[0](mdl_gp.x)
        final_list.append([mdl_rmse, train_model[2], mdl_gp.x])
        print('{} RMSE: R$ {}'.format(train_model[2], round(mdl_rmse, 4)))
    return final_list

def get_best_3_models(models_list):
    best_for_1_day = sorted(models_list[0])[:3]
    best_for_5_days = sorted(models_list[1])[:3]
    
    return best_for_1_day, best_for_5_days

def predict_today(df, model, params, time, X1, y1, X5, y5, last_data):
    if model == 'SGD':
        mdl = SGDRegressor(loss = params[0], penalty = params[1], alpha = params[2], learning_rate = params[3])
    elif model == 'Ridge':
        mdl = Ridge(alpha = params[0], fit_intercept = params[1], normalize = params[2], solver = params[3])
    elif model == 'SVR':
        mdl = LinearSVR(epsilon = params[0], C = params[1])
    elif model == 'KNN':
        mdl = KNeighborsRegressor(n_neighbors = params[0], weights = params[1], algorithm = params[2])
    elif model == 'DT':
        mdl = DecisionTreeRegressor(criterion = params[0], splitter = params[1], max_depth = params[2],
                                min_samples_split = params[3], min_samples_leaf = params[4], max_features = params[5])
    elif model == 'RF':
        mdl = RandomForestRegressor(n_estimators = params[0], criterion = params[1], max_depth = params[2],
                                 min_samples_split = params[3], min_samples_leaf = params[4], max_features = params[5])
    elif model == 'Ada':
        mdl = AdaBoostRegressor(n_estimators = params[0], learning_rate = params[1], loss = params[2])
    
    if time == 1:
        mdl.fit(X1, y1)
    else:
        mdl.fit(X5, y5)
        
    mdl_p = mdl.predict(last_data)[0]
    return mdl_p

def get_predictions_for_today(best_for_1_day, best_for_5_days, df, X1, y1, X5, y5, last_data):
    p_1_day = []
    for model in best_for_1_day:
        p_1_day.append([model[1], round(predict_today(df, model[1], model[2], 1, X1, y1, X5, y5, last_data), 2)])

    p_5_days = []
    for model in best_for_5_days:
        p_5_days.append([model[1], round(predict_today(df, model[1], model[2], 5, X1, y1, X5, y5, last_data), 2)])
        
    return p_1_day, p_5_days
