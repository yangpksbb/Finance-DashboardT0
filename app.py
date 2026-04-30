import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 Finance Dashboard")

# Daten für Microsoft und Apple laden
data_freeport = yf.download("FCX", start="2026-01-01")
data_aapl = yf.download("AAPL", start="2026-01-01")

# Kombinierter DataFrame für beide Aktien
combined = pd.DataFrame()
combined["Freeport"] = data_FCX["Close"]
combined["Apple"] = data_aapl["Close"]

# Line-Chart anzeigen
st.line_chart(combined)
