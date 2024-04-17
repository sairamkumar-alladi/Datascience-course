from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# for cookie in driver.get_cookies():
#     if 'expiry' in cookie:
#         # If 'expiry' is present in the cookie, it's not a session cookie
#         continue
#     driver.delete_cookie(cookie['name'])

url = "https://linkedin.com/in/rukmini-katare-934155a9"
driver.get(url)
time.sleep(50)
driver.find_element('xpath','//*[@id="public_profile_contextual-sign-in"]/div/section/button/icon/svg').click()
time.sleep(6)

name = driver.find_element('xpath', '//*[@id="main-content"]/section[1]/div/section/section[1]/div/div[2]/div[1]/h1').text
time.sleep(5)
print(name)