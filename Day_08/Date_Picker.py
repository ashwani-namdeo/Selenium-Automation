import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)   # Switch to frame
# driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("04/21/1993")

date = "21"
month = "April"
year = "2021"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "(//span[@class='ui-datepicker-year'])").text
    if mon == month and yr == year:
        break;
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()     # Previous arrow

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")
for i in dates:
    if i.text == date:
        i.click()
        break
time.sleep(2)