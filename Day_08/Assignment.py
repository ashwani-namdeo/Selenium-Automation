import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='product_549']").click()
price = driver.find_element(By.XPATH, "//*[@id='checkout-products']/li[1]/span[2]/span").text
driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Ashwani")
driver.find_element(By.XPATH, "//input[@id='travlastname']").send_keys("Namdeo")
driver.find_element(By.XPATH, "//input[@id='travlastname']").click()
driver.find_element(By.XPATH, "//input[@id='dob']").click()

yr = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
yr.select_by_visible_text("1993")
if yr != "1993":
    driver.find_element(By.XPATH, "//a[@title='Prev']").click()

mon = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
mon.select_by_visible_text("Apr")
time.sleep(1)

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")
for date in dates:
    if date.text == "21":
        date.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='sex_1']").click()
driver.find_element(By.XPATH, "//input[@id='traveltype_1']").click()
driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Bangalore")
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("New Delhi")
driver.find_element(By.XPATH, "//input[@id='departon']").click()

year = driver.find_element(By.XPATH, "//select[@aria-label='Select year']").text
if year != "2024":
    driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month.select_by_visible_text("Aug")

departure_date = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for element in departure_date:
    if element.text == "20":
        element.click()
        break;

purpose = Select(driver.find_element(By.XPATH, "//select[@id='reasondummy']"))
purpose.select_by_visible_text("Prank a friend")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='deliverymethod_3']").click()
driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("7587232951")
driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("test@test.com")
time.sleep(1)

country = Select(driver.find_element(By.XPATH, "//select[@id='billing_country']"))
country.select_by_visible_text("India")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("Flat No- 404, Sukhsagar Lifestyle Apartment")
driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys("LalPur Road, Gwarighat")
driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("Jabalpur")
time.sleep(1)

state = Select(driver.find_element(By.XPATH, "//select[@id='billing_state']"))
state.select_by_visible_text("Madhya Pradesh")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("482008")
time.sleep(1)

order_total = driver.find_element(By.XPATH, "//table[@class='shop_table woocommerce-checkout-review-order-table']/tfoot/tr[2]/td").text
if order_total == price:
    print("Test Case Passed..!!")
else:
    print("Test Case Failed..!!")
time.sleep(2)