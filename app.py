import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 Finance Dashboard")

# Daten für Microsoft und Apple laden
data_msft = yf.download("MSFT", start="2023-01-01")
data_aapl = yf.download("AAPL", start="2023-01-01")

# Kombinierter DataFrame für beide Aktien
combined = pd.concat([data_msft["Close"], data_aapl["Close"]], axis=1, keys=["Microsoft", "Apple"])

# Line-Chart anzeigen
st.line_chart(combined)