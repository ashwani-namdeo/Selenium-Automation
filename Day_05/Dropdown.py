from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# driver=webdriver.Chrome()
# driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
# driver.maximize_window()
#
# #driver.find_elements(By.XPATH, "//*[@id='navbar-collapse-header']/div/a[2]")
# driver.implicitly_wait(10)
# dropdown_element= driver.find_element(By.XPATH, "//select")
# dropdown_option= Select(dropdown_element)
#
# dropdown_option.select_by_visible_text("India")
# driver.implicitly_wait(3)

## ASSIGNMENT

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# dropdown_element= driver.find_element(By.XPATH, "//*[@id='speed']")
# dropdown_option= Select(dropdown_element)
# dropdown_option.select_by_visible_text("Faster")              # Selecting by visible text
# driver.implicitly_wait(3)

dropdown_element= driver.find_element(By.XPATH, "//*[@id='files']")
dropdown_option= Select(dropdown_element)
dropdown_option.select_by_value('2')                            # Selecting by value
driver.implicitly_wait(3)

