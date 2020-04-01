from app_bot import AppBot
import time 
from multiprocessing import Pool

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config2 import job_urls
import re

#bot = AppBot()

def run():
    bot.find_jobs()
    bot.filter_jobs()
    bot.login()

def apply():
    bot.manual_apply()

