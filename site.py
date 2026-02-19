import streamlit as st
#titles
st.title("Crypto Risks")
st.write("Project starting...")

import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Crypto Risks", layout="wide")

st.title("Crypto Risks 📉")

btc = yf.download("BTC-USD", period="6mo")

st.line_chart(btc["Close"])
st.write("Version 0.4")