
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import os 
import json

if os.path.exists('jobs.json'):
    print('it exists')
    with open('jobs.json') as f:
        jobs = json.load(f)

for item in jobs:
    print(item)