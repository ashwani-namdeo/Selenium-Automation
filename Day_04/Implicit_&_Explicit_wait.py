# IMPLICIT WAIT
# driver.implicitly_wait() - Maximum duration the script will wait for the mentioned time (sec) within ().


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# driver.implicitly_wait(5)         # Implicit wait command
#
#
# searchbox=driver.find_element(By.NAME, "q")
# searchbox.send_keys("Flipkart")
# searchbox.submit()
# driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3").click()
# driver.quit()


# EXPLICIT_WAIT - Works on different conditions

driver=webdriver.Chrome()
wait= WebDriverWait(driver, 10)         # Explicit wait declaration
driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME, "q")
searchbox.send_keys("Flipkart")
searchbox.submit()

searchlink=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3")))
searchlink.click()

driver.quit()