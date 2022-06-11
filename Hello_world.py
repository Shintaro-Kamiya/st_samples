import streamlit as st
import pandas as pd
import requests
import json
option = st.selectbox("地域選択",("静岡","東京"))
region = {"静岡": "220000","東京": "130000"}
id = region[option]
url = f'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{id}.json'
response = requests.get(url)
d = response.json()
t1 = "時間"+d["reportDatetime"]
t2 = d["text"]
st.write(t1)
st.write(t2)
