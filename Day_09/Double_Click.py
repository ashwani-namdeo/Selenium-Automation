import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
time.sleep(1)

driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH, "//input[@id='field1']").clear()
field_1 = driver.find_element(By.XPATH, "//input[@id='field1']").send_keys("Welcome")
button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
time.sleep(1)

action = ActionChains(driver)
action.double_click(button).perform()
time.sleep(1)

field_2 = driver.find_element(By.XPATH, "//input[@id='field2']").text
print(field_2)