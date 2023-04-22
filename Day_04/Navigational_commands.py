# Navigational Commands
# 1. back() - Switches back to the previous page.
# 2. forward() - Switches to the next page.
# 3. refresh() - Refreshes the current page.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

driver.get("https://www.amazon.in/")
driver.back()                               # Flipkart
driver.forward()                            # Amazon
driver.refresh()                            # Refreshes Amazon
time.sleep(5)
driver.quit()