# Conditional Commands
# 1. is_displayed() - to check if the element is displayed or not
# 2. is_enabled() -to check if the element is enabled or not
# 3. is_selected() - to check if the element is selected or not

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# is_displayed() & is_enabled()
searchbox=driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
print("Display Status:", searchbox.is_displayed())
print("Enabled Status:", searchbox.is_enabled())

# is_selected()
rd_male=driver.find_element(By.XPATH, "//*[@id='gender-male']")
rd_female=driver.find_element(By.XPATH, "//*[@id='gender-female']")
print("Default Radio Button Status-")
print("Male Radio Button:", rd_male.is_selected())          # False
print("Female Radio Button:", rd_female.is_selected())      # False

rd_male.click()
print("After Selecting Male Radio Button-")
print("Male Radio Button:", rd_male.is_selected())
print("Female Radio Button:", rd_female.is_selected()) # False

rd_female.click()
print("After Selecting Female Radio Button-")
print("Male Radio Button:", rd_male.is_selected())
print("Female Radio Button:", rd_female.is_selected())       # True
driver.close()