# There are 3 types of links-
# 1. Internal links
# 2. External Links
# 3. Broken Links

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Clicking a link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()

# Finding total number of links and printing them
#links= driver.find_elements(By.TAG_NAME, "a")
# links= driver.find_elements(By.XPATH, '//a')
# print("Total Number Of Links: ", len(links))

# Printing links
# for link in links:
#     print(link.text)