# Handling Broken Links (Need to install requests package from python interpretor)

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links= driver.find_elements(By.TAG_NAME, 'a')
count=0

for link in all_links:
    url=link.get_attribute('href')
    try:
        response=requests.head(url)
    except:
        None
    if response.status_code>=400:
        print(url, " is a broken URL.")
        count+=1
    else:
        print(url, " is a valid link")
print("Total number of valid links", count)