import streamlit as st
import yfinance as yf

st.title("📊 Finance Dashboard")

ticker = st.text_input("Ticker", "AAPL")

data = yf.download(ticker, start="2023-01-01")

st.line_chart(data["Close"])