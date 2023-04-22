# Mouse Hover Action


import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(1)

electronics = driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']")
cell_phones = driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']")

action = ActionChains(driver)

action.move_to_element(electronics).move_to_element(cell_phones).click().perform()
time.sleep(3)
