# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:22:10 2026

@author: ADMIN
"""

import requests
import pandas as pd
from datetime import datetime
import time

# API to monitor
API_URL = "https://jsonplaceholder.typicode.com/posts"

while True:
    try:
        start_time = time.time()

        response = requests.get(API_URL)

        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        log = {
            "Timestamp": datetime.now(),
            "API_URL": API_URL,
            "Status_Code": response.status_code,
            "Response_Time_ms": response_time
        }

        df = pd.DataFrame([log])

        df.to_csv("api_logs.csv", mode='a', header=False, index=False)

        print(f"Logged: {response.status_code} | {response_time} ms")

    except Exception as e:
        print("Error:", e)

    # wait 10 seconds before next request
    time.sleep(10)