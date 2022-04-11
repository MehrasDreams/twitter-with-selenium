from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from colorama import Fore
import time
import re


# TODO: Fix the last part of security
# TODO: Create function for bypass
# Read your account info
def account_info():
    with open('account_info', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
        phone = info[2]
    return email, password, phone


# Call the account info
email, password, phone = account_info()

options = Options
driver = webdriver.Chrome('/home/mrx/Desktop/twitter-with-selenium/chromedriver')

# Go to the twitter login page
driver.get("https://twitter.com/login")

# Login info Xpath
email_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
next_button_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span'
username_phone_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
next_for_username_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/span/span'
password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
login_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
last_phone_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
last_phone_button_xpaht = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/span/span'
time.sleep(5)
driver.find_element_by_xpath(email_xpath).send_keys(email)
time.sleep(5)
driver.find_element_by_xpath(next_button_path).click()

# Bypass the security check
time.sleep(7)
# driver.find_element_by_xpath(username_phone_xpath).send_keys(phone)
# driver.find_element_by_xpath(next_for_username_path).click()
# time.sleep(5)
driver.find_element_by_xpath(password_xpath).send_keys(password)
driver.find_element_by_xpath(login_button_xpath).click()
time.sleep(5)
# driver.find_element_by_xpath(last_phone_xpath).send_keys(phone)
# driver.find_element_by_xpath(last_phone_button_xpaht).click()

# Create username link

username_input = input(Fore.GREEN + "Enter your target username to get hi/she followers: ")
driver.get('https://twitter.com/{}/followers'.format(username_input))
time.sleep(4)

#
time.sleep(9)
follower_list = []
# Code to goto End of the Page
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(4)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    #get usernames element
    usernames = driver.find_elements_by_css_selector(
            ".css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l")
    print(len(usernames))
    for username in usernames:
        # username = driver.find_element_by_css_selector(".css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l").get_attribute("href")
        new_user = username.accessible_name
        if new_user not in follower_list:
            follower_list.append(new_user)
            print(new_user)
print(follower_list)
print(len(follower_list))
