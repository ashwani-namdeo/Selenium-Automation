import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(2)

alert = driver.switch_to.alert

print(alert.text)
alert.send_keys("Welcome to Selenium")

#alert.accept()         # To click on OK
alert.dismiss()         # To click on CANCEL
time.sleep(2)