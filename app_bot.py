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
## non standard and non pip install imports 
from config2 import username, password, job_search, job_urls, login_page


#EC.text_to_be_present_in_element((By.ID, "operations_monitoring_tab_current_ct_fields_no_data"), "No data to display")

class AppBot:
    def __init__(self):
        ##initialize chrome webdriver 
        self.driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
    
    initial_job  = ['https://www.indeed.com/jobs?q=data+engineer&l=Staten+Island,+NY&rbl=New+York,+NY&jlid=45f6c4ded55c00bf&explvl=entry_level']
    ## list of hrefs that contain jobs 
    hrefs = []

    ##login using credentials
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
        self.driver.get(self.initial_job[0])
        for i in range(0, 4):
            a_tags = self.driver.find_elements_by_tag_name('a')
            for a_tag in a_tags:
                href = a_tag.get_attribute('href')
                href = str(href)
                if re.match(r'^https://www.indeed.com/pagead/', href) or re.match(r'^https://www.indeed.com/rc/clk', href):
                    self.hrefs.append(href)
                    print(href)
            self.driver.find_element_by_class_name('np').click()
            ## popup that may come up when pressing next page 
            wait = WebDriverWait(self.driver, 2)
            try:
                popup = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="popover-close-link"]')))
                popup.click()
            except:
                print('no popup')
            print(len(self.hrefs))

    def iframe_handler(self):
        wait = WebDriverWait(self.driver, 2)
        try:
            frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name$=modal-iframe]')))
            self.driver.switch_to.frame(frame)
            time.sleep(2)
            self.driver.switch_to.frame(0)
        except:
            frame = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="indeedapply-modal-preload-iframe"]')))
            self.driver.switch_to.frame(frame)
            time.sleep(2)
            self.driver.switch_to.frame(0)
        textareas = self.driver.find_elements_by_xpath('//*[starts-with(@id, "q_")]/div')
        print(textareas)
        textinputs = []
        for item in textareas:
            text_item = item.text
            if text_item:
                print(text_item)
                textinputs.append(item)

    def iframe_closer(self):
        wait = WebDriverWait(self.driver, 2)
        frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        self.driver.switch_to.frame(0)
        try:
            wait = WebDriverWait(self.driver, 2)
            cancel_button = wait.until(EC.presence_of_element_located((By.ID, '//*[@id="popover-close-link"]')))
            cancel_button.click()
        except:
            pass
        try: 
            wait = WebDriverWait(self.driver, 2)
            cancel_button = wait.until(EC.presence_of_element_located((By.ID, '//*[@id="close-popup"]')))
            cancel_button.click()
        except:
            pass

    def click_job(self):
        #jobs = self.driver.find_elements_by_class_name("jobsearch-SerpJobCard")
        self.driver.get('https://www.indeed.com/viewjob?from=serp,iaBackPress,iaBackPress,iaBackPress&jk=3f2f91cc5ac41d8e&vjs=3')
        try:
            print('trying first method')
            wait = WebDriverWait(self.driver, 2)
            apply_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="indeedApplyButtonContainer"]/span/div[2]/button')))
            #jobs = self.driver.find_elements_by_class_name("jobsearch-SerpJobCard") 
            print(apply_button)
            apply_button.click()
        except:
            print('trying second method')
            wait = WebDriverWait(self.driver, 2)
            apply_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="indeedApplyButtonContainer"]/span/div[1]/button')))
            print(apply_button)
            apply_button.click()
      
    def apply_jobs(self):
        clickable_jobs = []
        for href in self.hrefs:
            print(f" trying : {href} ")
            self.driver.get(href)
            try: 
                self.click_job()
                print('\nclicked jobs')
                clickable_jobs.append(href)
                self.iframe_closer()
                print('\niframe handled')
                time.sleep(1)
            except:
                print('didnt work or takes to company site')
        with open ('clickable_jobs.json', 'w') as f:
            json.dump(clickable_jobs, f)
bot = AppBot()
bot.login()
time.sleep(4)
bot.click_job()
bot.iframe_handler()