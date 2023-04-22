import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
time.sleep(1)

min_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Location of Sliders before moving...")
print("Minimum Slider Location: ", min_slider.location)     # {'x': 59, 'y': 250}
print("Maximum Slider Location: ", max_slider.location)     # {'x': 612, 'y': 250}

action = ActionChains(driver)

action.drag_and_drop_by_offset(min_slider, 141, 0).perform()
action.drag_and_drop_by_offset(max_slider, -112, 0).perform()

print("Location of Sliders after moving...")
print("Minimum Slider Location: ", min_slider.location)     # {'x': 203, 'y': 250}
print("Maximum Slider Location: ", max_slider.location)     # {'x': 502, 'y': 250}
time.sleep(1)
