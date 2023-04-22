# 1. Open Browser (Chrome)
# 2. Open URL- https://instructor.kafqa.com/
# 3. Enter Username- 7587232951
# 4. Enter Password- CBZxtreme@5895
# 5. Click on Login.
# 6. Capture title of the page.
# 7. Verify title of the page.
# 8. Close Browser.
from token import NAME

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "login-button").click()
act_title=driver.title
exp_title="Dashboard / nopCommerce administration"
if act_title==exp_title:
    print("Test case passed")
else:
    print("Test case failed")
driver.close()