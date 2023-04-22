import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
time.sleep(2)

outer_frame = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[2]/div[2]/iframe")
driver.switch_to.frame(outer_frame)
time.sleep(1)

inner_frame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Welcome Ashwani")
time.sleep(1)

#driver.switch_to.parent_frame()         # Will switch to the parent frame

driver.quit()