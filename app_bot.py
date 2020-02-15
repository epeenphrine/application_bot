## selenium imports 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as EC

## standard library imports 
import time
import re

## non standard and non pip install imports 
from config2 import username, password, job_search, job_urls, login_page

class AppBot:
    def __init__(self):
        ##initialize chrome webdriver 
        self.browser = webdriver.Chrome('./chromedriver/chromedriver.exe')
    
    def login(self):
        ##login page
        self.browser.get(login_page)
        ## google login button and click
        select_google_button = self.browser.find_element_by_xpath('//*[@id="login-google-button"]')
        select_google_button.click()
        ## browser window handle
        base_window = self.browser.window_handles[0]
        print(self.browser.window_handles)
        self.browser.switch_to_window(self.browser.window_handles[1])
        ## email field selection / keyboard input
        select_username = self.browser.find_element_by_xpath('//*[@id="identifierId"]')
        select_username.send_keys(username)
        select_username.send_keys(Keys.ENTER)
        ## password field selection / keyboard input
        print(self.browser.window_handles)
        self.browser.implicitly_wait(5) ## need timeout so that the password field render before selecting it 
        select_password = self.browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        select_password.send_keys(password)
        ## press ENTER key 
        select_password.send_keys(Keys.ENTER)
    def apply(self):
        pass


bot = AppBot()
bot.login()
