from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

# # Finding element by ID
# driver.find_element(By.ID, "small-searchterms").send_keys("Nokia Lumia 1020")
#
# # Finding element by LINKTEXT
# driver.find_element(By.LINK_TEXT, "Register").click()

# Finding element by PARTIAL LINKTEXT
# driver.find_element(By.PARTIAL_LINK_TEXT, "Regis").click()

# Finding number of links in a web page
# links=driver.find_elements(By.TAG_NAME, "a")
# print(len(links))

# Finding element by CSS_SELECTOR
# TAG & ID ---> tagname#valueofid  OR #valueofid
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("123")

# TAG & CLASS ---> tagname.valueofclass  OR ,valueofclass
# driver.find_element(By.CSS_SELECTOR, "input.email").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, ".pass").send_keys("123")

# TAG & ATTRIBUTE ---> tagname[attribute=value]  OR [attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmail.com")

# TAG, CLASS & ATTRIBUTE ---> tagname.valueofclass[attribute=value]  OR .valueofclass[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("abc@gmail.com") #--> for email textfield
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("12345")  #--> for password textfield
