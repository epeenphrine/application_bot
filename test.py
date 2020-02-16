
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
driver.get("https://www.indeed.com/jobs?q=data%20engineer&l=Staten%20Island%2C%20NY&ts=1581828087740&pts=1581817764046&rq=1&rsIdx=0&vjk=06e452eb47705535&advn=9655271218567678")


a_tags = driver.find_elements_by_tag_name('a')

hrefs = []
for a_tag in a_tags:
    href = a_tag.get_attribute('href')
    href = str(href)
    if re.match(r'^https://www.indeed.com/pagead/', href) or re.match(r'^https://www.indeed.com/rc/clk', href):
        hrefs.append(href)
        print(href)

print(len(hrefs))

for href in hrefs:
    driver.get(href)
#driver.find_element_by_class_name('indeed-apply-button').click()

#wait = WebDriverWait(driver, 10)
#frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
#driver.switch_to.frame(frame)
#time.sleep(3)
#driver.switch_to.frame(0)

#driver.find_element_by_id('form-action-cancel').click()
