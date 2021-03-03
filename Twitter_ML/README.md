# **Twitter Bot for Machine Learning: Stock Predictions**   
If you're reading this in your cellphone, you can switch your viewing "to computer" in the configurations of your browser - the three dots -, to improve the visualization :D
![](https://github.com/KenzoBH/Data-Science/blob/main/Images/Regress.jpg)

# Overview   

This project is about publishing (or tweeting) forecasts of 3 models on stocks in the financial market everyday.   
Technologies and packages used:
- Web Scraping: pandas and NumPy
- Machine Learning Models: sklearn
- Twitter Bot: Tweepy
- Deploy: PythonAnywhere

You can see the final project [here](https://twitter.com/RegressTrio) (the Twitter account of Regress).

## Files

- [`regress_bot.py`](https://github.com/KenzoBH/Data-Science/blob/main/Twitter_ML/regress_bot.py) and [`functions.py`](https://github.com/KenzoBH/Data-Science/blob/main/Twitter_ML/functions.py): Python program that is running in [PythonAnywhere](https://www.pythonanywhere.com/), and contains the bot code and the models training. `functions.py` is a file that contais functions that I used in the `regress_bot.py` program.
- [`companies_txt`](https://github.com/KenzoBH/Data-Science/blob/main/Twitter_ML/companies.txt) and [`last_mention_id.txt`](https://github.com/KenzoBH/Data-Science/blob/main/Twitter_ML/last_mention_id.txt): Example of text files used by the Regress Bot to store the companies that it predicts and tweets, and the last tweet that mentioned it's account (better explained on `regress_bot.py` logic and comments).

## Methods

The models were chosen based on their RMSE (Root Mean Squared Error) over the the historical data of POMO4 company stock. The best models were the Stochastic Gradient Descent (aka SGD and Satoshi Gaara Daisuke 🙇🏼‍♂️), Linear Support Vector Regression (aka SVR and Sophia Victoria Resende 🙆🏻‍♀️) and the Random Forest (aka RF and Rannah dom Fontes 👩‍💻) :D   
They beat the other models (Ridge Regression and Linear Regression) and the stipulated baseline, that predicted the average of the training data for the new days.   

The models are trained everyday with new data, that is scraped off the [Yahoo Finance website](https://finance.yahoo.com/), and their predictions are shown on the [@RegressTrio](https://twitter.com/RegressTrio) account on Twitter.

-------------------------

My Data Science portfolio: [link](https://github.com/KenzoBH/Data-Science)   
My LinkedIn: [link](https://www.linkedin.com/in/bruno-kenzo/)
