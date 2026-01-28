# importing libraries

import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datatime

st.set_page_config(page_title = "CAPM",
                   page_icon = "chart_with_upwards_trend",
                   layout = "wide")

st.title("Capital Asset Pricing Model")

# getting input from user

col1, col2 = st.columns([1,1])
with col1:
    stocks_list = st.multiselect("Choose 4 stocks", ('TSLA','AAPL','NFLX','MSFT','MGM','AMZN','NVDA','GOOGL'),['TSLA','AAPL','AMZN','GOOGL'])
with col2:
    year = st.number_input("Number of years",1,10)

# Downloading the data for S&P500

end = datetime.date.today()
start = datetime.date(datetime.date.today().year-year, datetime.date.today().month, datetime.date.today().day)
SP500 = web.DataReader(['sp500'],'fred',start,end)
print(SP500.head())


