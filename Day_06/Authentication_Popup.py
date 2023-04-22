import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")     # By passing the username (admin) & password (admin) in the URL, we can bypass the authentication pop-up
driver.maximize_window()
time.sleep(5)