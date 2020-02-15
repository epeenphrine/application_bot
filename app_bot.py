## selenium imports 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

## standard library imports 
import time
import re

## non standard and non pip install imports 
from config import username, password, job_search, job_urls, login_page

class AppBot:
    def __init__(self):
        ##initialize chrome webdriver 
        self.browser = webdriver.Chrome('./chromedriver/chromedriver.exe')
    
    def login(self):
        ##login page
        self.browser.get(login_page)
        ## email field selection / keyboard input
        select_username = self.browser.find_element_by_xpath("//*[@id='login-email-input']")
        select_username.send_keys(username)
        ## password field selection / keyboard input
        select_password = self.browser.find_element_by_xpath('//*[@id="login-password-input"]')
        select_password.send_keys(password)
        ## press ENTER key 
        select_password.send_keys(keys.ENTER)
    
    def apply(self):
        pass


bot = AppBot()
bot.login()