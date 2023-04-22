import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(1)

### 1. Scroll the page by Pixel:

# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# time.sleep(1)
# print("Number of pixels moved: ", value)             # 3000

### 2. Scroll the page until the element is found

# india = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", india)
# value = driver.execute_script("return window.pageYOffset;")
# time.sleep(1)
# print("Number of pixels moved: ", value)             # 4974.39990234375

### 3. Scroll the page until bottom

# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "")
# value = driver.execute_script("return window.pageYOffset;")
# time.sleep(1)
# print("Number of pixels moved: ", value)              # 6040

### Scrolling to the page until top

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "")
time.sleep(1)
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)", "")
value = driver.execute_script("return window.pageYOffset;")
time.sleep(1)
print("Number of pixels moved: ", value)                 # 6040
