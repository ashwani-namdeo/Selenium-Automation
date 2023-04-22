from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://instructor.kafqa.com/")
driver.maximize_window()

# Absolute Xpath

# driver.find_element(By.XPATH, "/html/body/div/main/div/div/div[6]/form/div/h4").click()
# driver.find_element(By.XPATH, "/html/body/div/main/div/div/div[6]/form/div/div[1]/input").send_keys("7587232951")
# driver.find_element(By.XPATH, "/html/body/div/main/div/div/div[6]/form/div/div[2]/input").send_keys("CBZxtreme@5895")
# driver.find_element(By.XPATH, "/html/body/div/main/div/div/div[6]/form/div/button").click()
# actual_title=driver.title
# expected_title="Kafqa Instructor"
# if actual_title==expected_title:
#     print("Test case passed.")
# else:
#     print("Test case failed.")

# Relative Xpath

# driver.find_element(By.XPATH, "//*[@id='root']/main/div/div/div[6]/form/div/h4").click()
# driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("7587232951")
# driver.find_element(By.XPATH, "//*[@id='password']").send_keys("CBZxtreme@5895")
# driver.find_element(By.XPATH, "//*[@id='mui-1']").click()
# act_title=driver.title
# exp_title= "Kafqa Instructor"
# if act_title==exp_title:
#     print("Test Case Passed..")
# else:
#     print("Test Case Failed..!!")

