import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()
time.sleep(1)

input_1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input_2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input_1.send_keys("Keyboard Actions via Automation")

action = ActionChains(driver)

action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
action.key_down(Keys.TAB).perform()
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()  
time.sleep(2)
