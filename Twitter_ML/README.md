# **Twitter Bot for Machine Learning: Stock Predictions**

![](https://github.com/KenzoBH/Data-Science/blob/main/Images/Regress.jpg)

# Overview   

This project is about publishing (or tweeting) forecasts of 3 models on stocks in the financial market everyday.   
Technologies and packages used:
- Data Analysis: pandas, NumPy, matplotlib and seaborn
- Web Scraping: requests
- Modeling: sklearn
- Twitter Bot: Tweepy
- Deploy: pythoneverywhere

You can see the final project [here](https://twitter.com/RegressTrio) (the Twitter account of Regress).

## Methods

The models were chosen based on their RMSE (Root Mean Squared Error) over the the historical data of POMO4 company stock. The details of this selection is [here]() - `Model_Selection.ipynb` file -, where it's explained the whole proccess. Anyway, the best models were the Stochastic Gradient Descent (aka SGD and Satoshi Gaara Daisuke), Linear Support Vector Regression (aka SVR and Sophia Victoria Resende) and the Linear Regression (aka LR and Lineu Regis) :D   
They beat the other models (Ridge Regression and Random Forest) and the stipulated baseline, that predicted the average of the training data for the new days.   
The models are trained everyday with new data, that is scraped off the [Yahoo Finance website](https://finance.yahoo.com/), and their predictions are shown on the [@RegressTrio](https://twitter.com/RegressTrio) account on Twitter.

## Results
