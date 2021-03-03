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

The program train 7 models everyday. They are: Stochastic Gradient Descent, Ridge Regression, Linear Suppor Vector Regressor, K-Nearest Neighbors, Decision Tree, Random Forest and Ada Boost. The models are trained with the last 50 days, and tested with the last 5 - the best ones are chosen (based on their RMSE, Root Mean Squared Error) to tweet the predictions. As I observed, Linear SVR and SGD are the best ones.

The details of the models training and selection is in `regress_bot.py`and `functions.py` files. They are trained everyday with new data, that is scraped off the [Yahoo Finance website](https://finance.yahoo.com/), and their predictions are shown on the [@RegressML](https://twitter.com/RegressML) account on Twitter.

-------------------------

My Data Science portfolio: [link](https://github.com/KenzoBH/Data-Science)   
My LinkedIn: [link](https://www.linkedin.com/in/bruno-kenzo/)
