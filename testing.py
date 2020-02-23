from datetime import datetime
from datetime import timedelta
import time
import winsound
import webbrowser
import json

with open ('decent_jobs.json') as f:
    decent_jobs = json.load(f)

print(len(decent_jobs))
for job in decent_jobs:
    webbrowser.open(job)
    wait = input('press a key to go next')