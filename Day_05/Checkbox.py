import click
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
driver.implicitly_wait(10)


## Selecting 1 checkbox
#driver.find_element(By.XPATH, "//*[@id='monday']").click()

# Selecting multiple checkbox
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains (@id,'day')]")
print(len(checkboxes))

## Approach-1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

## Approach-2
# for checkbox in checkboxes:
#     checkbox.click()

# Selecting multiple checkboxes by choice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='tuedsay':
#         checkbox.click()

# Selecting last 2 checkboxes
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()

# Selecting 1st two checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

# Un-selecting all the checkboxes
for checkbox in checkboxes:
    checkbox.click()
for checkbox in checkboxes:
     if checkbox.is_selected():
          checkbox.click()
print(checkbox.is_selected())