import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(1)

source = driver.find_element(By.ID, "box7")
target = driver.find_element(By.ID, "box107")

action = ActionChains(driver)

action.drag_and_drop(source,target).perform()
time.sleep(2)