## There are 2 types of Web Tables:
## 1. Static Web Table
## 2. Dynamic Web Table


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1)

## COUNTING NUMBER OF ROWS & COULMNS

rows = driver.find_elements(By.XPATH, "//*[@id='HTML1']/div[1]//tr")
print(len(rows))

columns = driver.find_elements(By.XPATH, "//*[@id='HTML1']/div[1]//th")
print(len(columns))

## DISPLAYING PARTICULAR DATA FROM WEB TABLE

# data = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[5]/td[1]")
# print(data.text)

## READ ALL THE ROWS AND COLUMNS DATA

# for r in range(2, len(rows)+1):
#     for c in range(1, len(columns)+1):
#         data = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")
#         print(data.text, end="      ")
#     print()

## PRINTING DATA BASED ON CERTAIN CONDITION (List book names whose author is Mukhesh)

for r in range(2, len(rows)+1):
    author_name = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[" + str(r) + "]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[" + str(r) + "]/td[4]").text
        print(book_name,"   ", price)
driver.close()