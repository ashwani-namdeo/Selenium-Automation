# Application Commands
# 1. get() - to open URL
# 2. title - to capture title of the page
# 3. current_url - to capture current URL of the page
# 4. source_url - to capture source URL of the page



from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
title=driver.title
print(title)
curr_url=driver.current_url                 # to capture current URL of the page
print(curr_url)
page_source=driver.page_source              # to capture page source
print(page_source)
driver.close()                              # to close the browser
