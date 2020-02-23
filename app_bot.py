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
## non standard and non pip install imports 
from config2 import username, password, job_search, job_urls, login_page, pay, address, state, postal, linkedin, opportunity

#EC.text_to_be_present_in_element((By.ID, "operations_monitoring_tab_current_ct_fields_no_data"), "No data to display")

class AppBot:
    def __init__(self):
        ## setup to modify navigator.webdriver to prevent capcha from popping up
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        ##initialize chrome webdriver 
        self.driver = webdriver.Chrome(options=self.options, executable_path=r'./chromedriver/chromedriver.exe')
    
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
        for url in job_urls:
            self.driver.get(url)
            for i in range(0, 4):
                a_tags = self.driver.find_elements_by_tag_name('a')
                for a_tag in a_tags:
                    href = a_tag.get_attribute('href')
                    href = str(href)
                    if re.match(r'^https://www.indeed.com/pagead/', href) or re.match(r'^https://www.indeed.com/rc/clk', href):
                        if href not in self.hrefs:
                            self.hrefs.append(href)
                            print(href)
                        else:
                            print('href in hrefs')
                next_button =self.driver.find_elements_by_class_name('np')
                if next_button:
                    next_button[0].click() 
                ## popup that may come up when pressing next page 
                wait = WebDriverWait(self.driver, 2)
                try:
                    popup = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="popover-close-link"]')))
                    popup.click()
                except:
                    print('no popup')
                print(len(self.hrefs))
    ## question handling
    def question_handler(self):
        time.sleep(1)
        cont_button = self.driver.find_elements_by_xpath('//*[@id="form-action-continue"]')
        print(f' cont button :  {cont_button}')
        if cont_button:
            textareas = self.driver.find_elements_by_xpath('//*[starts-with(@id, "q_")]/div')
            if textareas:
                print(f' printing textareas : {textareas}')
                textinputs = []
                questions = []
                for item in textareas:
                    text_item = item.text
                    if text_item:
                        questions.append(text_item.lower())
                        xpath_textarea = item.find_elements_by_xpath('.//textarea')
                        if xpath_textarea:
                            textinputs.append(xpath_textarea[0])
                        xpath_inputarea = item.find_elements_by_xpath('.//input')
                        if xpath_inputarea:
                            textinputs.append(xpath_inputarea[0])

            print(questions)
            print(textinputs)
            print(len(textinputs))
            for i in range(0, len(questions)):
                try:
                    a = questions[i]
                    b = textinputs[i]
                except:
                    pass
                if 'pay' in a:
                    b.send_keys(pay)
                if 'address' in a:
                    b.send_keys(address)
                if 'city' in a:
                    b.send_keys('')
                if 'state' in a:
                    b.send_keys(state)
                if 'postal' in a:
                    b.send_keys(postal)
                if 'linkedin' in a:
                    b.send_keys(linkedin)
                if 'available' in a:
                    available = datetime.now() + timedelta(days=5) 
                    available = available.strftime('%m/%d/%Y')
                    b.send_keys(f'{str(available)}')
                if 'learn about this opportunity' in a:
                    b.send_keys('found it on job board')
                if 'country' in a:
                    xpath_select = self.driver.find_elements_by_xpath('//*[@id="select-0"]')
                    xpath_select[0].click()
                    print('selected drop down menu')
                    time.sleep(1)
                    xpath_select = self.driver.find_elements_by_xpath('//*[@id="select-0"]/option[2]')
                    xpath_select[0].click()
                    print('selected country in drop down menu')
            if not questions:
                xpath_select = self.driver.find_elements_by_xpath('//*[@id="resumeTypeSelector"]')
                xpath_select[0].click()
                print(f'drop down menu clicked')
                time.sleep(1)
                xpath_select = self.driver.find_elements_by_xpath('//*[@id="resumeTypeSelector"]/option[4]')
                xpath_select[0].click()
                print(f'options clicked !')
            cont_button[0].click()
            return self.question_handler()
        else:
            print('no more cont button ')
            capcha = self.driver.find_elements_by_xpath('//*[@id="rc-anchor-container"]')
            if capcha:
                winsound.Beep(2500, 2000)
                print('capcha present need to handle it')
            else:
                apply_button = self.driver.find_elements_by_xpath('//*[@id="form-action-submit"]')
                apply_button[0].click()



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
                    

    def iframe_closer(self):
        wait = WebDriverWait(self.driver, 2)
        frame = wait.until(EC.presence_of_element_located((By.css_selector, "iframe[name$=modal-iframe]")))
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
        with open('clickable_jobs.json') as f:
            clickable_jobs_check = json.load(f)
        for href in self.hrefs:
            print(f" trying : {href} ")
            self.driver.get(href)
            try: 
                self.click_job()
                print('\nclicked jobs')
                if href in clickable_jobs_check:
                    clickable_jobs.append(href)
                self.iframe_handler()
                self.question_handler()
                print('\niframe handled')
                time.sleep(1)
            except:
                print('didnt work or takes to company site')
        with open ('clickable_jobs.json', 'w') as f:
            json.dump(clickable_jobs, f)

    def filter_jobs(self):
        if os.path.exists('decent_jobs.json'):
            with open('decent_jobs.json') as f:
                decent_jobs = json.load(f)
        else:
            decent_jobs = []
        for href in self.hrefs:
            if href not in decent_jobs:
                print(f'bringing up : {href} ')
                self.driver.get(href)
                applied_button2 = self.driver.find_elements_by_xpath('//*[@id="saveJobButtonContainer"]/div/div/div/div[2]/button')
                print(f'applied button 2 : {applied_button2}')
                company_site = self.driver.find_elements_by_xpath('//*[@id="viewJobButtonLinkContainer"]/div/div[2]/a') 
                print(f'company_site : {company_site}')
                if applied_button2:
                    text = applied_button2[0].text
                    print(text)
                    if 'applied' in text.lower():
                        print('applied')
                    elif company_site:
                        print('takes to company site')
                    else:
                        self.click_job()
                        decent_jobs.append(href)
            else:
                print(f'{href} in json \nskipping this url')
        with open ('decent_jobs.json', 'w') as f:
            json.dump(decent_jobs, f)

    def manual_apply(self):
        with open ('decent_jobs.json') as f:
            decent_jobs = json.load(f)
        for job in decent_jobs:
            webbrowser.open(job)