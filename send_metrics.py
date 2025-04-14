# metrics-generator/send_metrics.py

import time
import random
import requests

INFLUXDB_URL = "http://influxdb:8086/write?db=metrics"

while True:
    cpu = random.uniform(20, 90)
    mem = random.uniform(30, 95)
    disk = random.uniform(10, 80)
    data = f"system_metrics,host=demo-server cpu={cpu:.2f},memory={mem:.2f},disk={disk:.2f}"
    try:
        response = requests.post(INFLUXDB_URL, data=data)
        print("Sent:", data)
        print("Status:", response.status_code)
    except Exception as e:
        print("Error:", e)
    time.sleep(5)

