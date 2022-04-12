
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from colorama import Fore
import time


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


# Function for the security problem

def first_phone():
    driver.find_element_by_xpath(username_phone_xpath).send_keys(phone)
    driver.find_element_by_xpath(next_for_username_path).click()


def last_phone():
    driver.find_element_by_xpath(last_phone_xpath).send_keys(phone)
    driver.find_element_by_xpath(last_phone_button_xpaht).click()


first_by_pass_input = input(Fore.GREEN + "Are you getting first problem?")
if first_by_pass_input == 'yes':
    first_phone()



# Bypass the security check

time.sleep(3)
driver.find_element_by_xpath(password_xpath).send_keys(password)
driver.find_element_by_xpath(login_button_xpath).click()
time.sleep(5)

secend_by_pass_input = input(Fore.YELLOW + "Are you getting second problem? ")

if secend_by_pass_input == 'yes':
    last_phone()


# Create username link

username_input = input(Fore.BLUE + "Enter your target username to get hi/she followers: ")
# Write your follower list
open_location_text = open(f'{username_input}.txt', 'w')

# Go to the username followers
driver.get('https://twitter.com/{}/followers'.format(username_input))
time.sleep(4)
temp = []
time.sleep(9)
follower_list = []
# Code to goto End of the Page
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    time.sleep(5)
    # Scroll down to bottom
    print(Fore.RED+"Scrolling.....")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(4)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break

    last_height = new_height
    time.sleep(9)
    # get usernames element
    usernames = driver.find_elements_by_css_selector(
        ".css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l")
    print(len(usernames))
    temp.append(usernames)
    print(Fore.BLUE + "Processing... ")
    for username in usernames:
        new_user = username.accessible_name
        if new_user not in follower_list:
            write_file = open_location_text.writelines(new_user + '\n')
            follower_list.append(new_user)
            print(new_user)
print(temp)
print(follower_list)
print(len(follower_list))



print(Fore.WHITE+f"Saved on {username_input}")
print(Fore.RED + "The process is finish \nThis robot Created by itteam link of website [itteam.ir]")
