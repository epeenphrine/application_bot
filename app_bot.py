## selenium imports 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
## standard library imports 
import re
import time 
## non standard and non pip install imports 
from config2 import username, password, job_search, job_urls, login_page

class AppBot:
    def __init__(self):
        ##initialize chrome webdriver 
        self.driver = webdriver.Chrome('./chromedriver/chromedriver.exe')

    def login(self):
        ##login page
        self.driver.get(login_page)
        ## google login button and click
        select_google_button = self.driver.find_element_by_xpath('//*[@id="login-google-button"]')
        select_google_button.click()
        ## browser window handle. Tell selenium which window to use in multi window scenario
        base_window = self.driver.window_handles[0]
        print(self.driver.window_handles)
        self.driver.switch_to_window(self.driver.window_handles[1])
        ## email field selection / keyboard input
        select_username = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        select_username.send_keys(username)
        select_username.send_keys(Keys.ENTER)
        ## password field selection / keyboard input
        ## need timeout so that the password field render before selecting it 
        self.driver.implicitly_wait(5) 
        select_password = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        select_password.send_keys(password)
        ## press ENTER key 
        select_password.send_keys(Keys.ENTER)
        self.driver.switch_to_window(self.driver.window_handles[0])

    def job_click(self):
        url = "https://www.indeed.com/jobs?q=data%20engineer&l=Staten%20Island%2C%20NY&ts=1581828087740&pts=1581817764046&rq=1&rsIdx=0&vjk=e82d436ff1018523&advn=9424060155461514"
        self.driver.get(url)
        self.driver.implicitly_wait(2) 
        
        jobs = self.driver.find_elements_by_class_name("jobsearch-SerpJobCard") 
        for job in jobs:
            job.click()
            print(f'clicked {job}')
            try:
                self.driver.find_element_by_class_name('indeed-apply-button').click()
                wait = WebDriverWait(self.driver, 10)
                frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
                self.driver.switch_to.frame(frame)
                time.sleep(2)
                self.driver.switch_to.frame(0)
                self.driver.find_element_by_id('form-action-cancel').click()
                self.driver.implicitly_wait(5)
            except:
               print("company site")

    def iframe_handler(self):
        pass
           

bot = AppBot()
bot.login()
bot.job_click()