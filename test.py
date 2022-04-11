from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from colorama import Fore
import time



driver = webdriver.Chrome('/home/mrx/Desktop/twitter-with-selenium/chromedriver')



driver.get('https://instagram.com/')
time.sleep(12)
email_xpath = '._2hvTZ.pexuQ.zyHYP'
driver.find_element_by_css_selector(email_xpath).send_keys('mehrasliunux@gmail.com')



