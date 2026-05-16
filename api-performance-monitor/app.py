# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:21:40 2026

@author: ADMIN
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=10000, key="datarefresh")

st.title("API Performance Monitoring Dashboard")

# Load CSV data
df = pd.read_csv("api_logs.csv")

# Show data
st.subheader("API Logs")
st.dataframe(df)

# Average Response Time
avg_time = df["Response_Time_ms"].mean()

st.metric("Average Response Time (ms)", round(avg_time, 2))

# Plot response times
st.subheader("Response Time Chart")

fig, ax = plt.subplots()

ax.plot(df["Response_Time_ms"])

ax.set_xlabel("Requests")
ax.set_ylabel("Response Time (ms)")

st.pyplot(fig)

# Status code count
st.subheader("Status Code Distribution")

status_counts = df["Status_Code"].value_counts()

st.bar_chart(status_counts)