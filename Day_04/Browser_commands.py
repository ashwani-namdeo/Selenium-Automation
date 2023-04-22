# Browser Commands
# 1. close() - Closes single browser window. (Where the driver is focused.)
# 2. quit() - Closes the browser no matter how many tabs are opened. (Kills the process)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[2]/div[2]/a").click()
time.sleep(5)               # Waiting command

#driver.close()
driver.quit()