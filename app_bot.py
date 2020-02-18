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
        initial_job  = 'https://www.indeed.com/jobs?q=data+engineer&l=Staten+Island,+NY&rbl=New+York,+NY&jlid=45f6c4ded55c00bf&explvl=entry_level'
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
    # stores href of all job posting in a list
    def find_jobs(self):

    def job_click(self):
        self.driver.implicitly_wait(2) 
        #jobs = self.driver.find_elements_by_class_name("jobsearch-SerpJobCard") 
        self.driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[1]/button').click()

        #for job in jobs:
            #job.click()
            #print(f'clicked {job}')
            #try:
                #self.driver.find_element_by_class_name('indeed-apply-button').click()
                #wait = WebDriverWait(self.driver, 10)
                #frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
                #self.driver.switch_to.frame(frame)
                #time.sleep(2)
                #self.driver.switch_to.frame(0)
                #self.driver.find_element_by_id('form-action-cancel').click()
                #self.driver.implicitly_wait(5)
            #except:
               #print("company site")

    def iframe_handler(self):
        wait = WebDriverWait(self.driver, 10)
        frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_id('form-action-cancel').click()
        self.driver.implicitly_wait(5)

bot = AppBot()
bot.login()
bot.job_click()