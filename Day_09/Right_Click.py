import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/3.x/demo.html")
driver.maximize_window()
time.sleep(1)

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

action = ActionChains(driver)

action.context_click(button).perform()
time.sleep(2)