import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(2)
driver.switch_to.default_content()          # Switch back to main page

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH, "/html/body/main/div/section[1]/ul/li[13]/a/span").click()
time.sleep(2)
driver.switch_to.default_content()          # Switch back to main page

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()
time.sleep(3)