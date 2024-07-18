import os

os.system('start locust -f locustfile.py --host=https://myfeeling.streamlit.app/')
os.system('start http://localhost:8089')