## selenium imports 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
## standard library imports 
import re
import time 
import json
from datetime import datetime
from datetime import timedelta
import winsound
import webbrowser
import os
import random
from multiprocessing import Pool
## non standard and non pip install imports 
from config2 import username, password, job_search, job_urls, login_page, pay, address, state, postal, linkedin, opportunity






## list of hrefs that contain jobs 
hrefs = []
##login using credentials
def login():
## setup to modify navigator.webdriver to prevent capcha from popping up
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    ##initialize chrome webdriver 
    driver = webdriver.Chrome(options=options, executable_path=r'./chromedriver/chromedriver.exe')
## list of hrefs that contain jobs 
    ##login page
    driver.get("https://bumble.com/get-started")
    ## google login button and click
    wait = WebDriverWait(driver, 10)
    
    sign_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div/span/span')))
    print(sign_button)
    sign_button.click()
    ## browser window handle. Tell selenium which window to use in multi window scenario
    base_window = driver.window_handles[0]
    print(driver.window_handles)
    driver.switch_to_window(driver.window_handles[1])
    ## email field selection / keyboard input

    select_email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
    select_email.send_keys("HELLO THIS IS WORKING")


login()