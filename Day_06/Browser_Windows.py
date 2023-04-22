# 1. driver.current_window_handle ---> Will capture current window ID
# 2. driver.window_handles --> Will capture window IDs of all the browser windows


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

# window_id = driver.current_window_handle
# print(window_id)        # EE36486395708E852FE9779540EBFFDE
#                         # C3AE5D18D62C7EB70E720B2314CC89B5

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
window_ids = driver.window_handles

## ONLY IF 1 or 2 BROWSER WINDOWS ARE THERE.

parent_window = window_ids[0]
child_window = window_ids[1]

print("Parent Window ID: ", parent_window)      # Parent Window ID:  3B2B5F98F2EF6415557E4497C3825B6E
print("Child Window ID: ", child_window)        # Child Window ID:  9AAE6191EA4853AFBD5539E4827934D5

driver.switch_to.window(child_window)
print("Child window title is: ", driver.title)  # Child window title is:  OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM

driver.switch_to.window(parent_window)
print("Parent window title is: ", driver.title) # Parent window title is:  OrangeHRM

## IF THERE ARE MORE THAN 2 BROWSER WINDOWS.

# for win_id in window_ids:
#     driver.switch_to.window(win_id)
#     print(driver.title)

## IF WE WANT TO CLOSE SOME PARTICULAR WINDOW.

## FOR CLOSING PARENT WINDOW

# for win_id in window_ids:
#     driver.switch_to.window(win_id)
#     if driver.title=="OrangeHRM":
#         driver.close()
# time.sleep(5)

## FOR CLOSING CHILD WINDOW --> Capture the titles and use operators to close them

for win_id in window_ids:
    driver.switch_to.window(win_id)
    if driver.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM":
        driver.close()
time.sleep(5)