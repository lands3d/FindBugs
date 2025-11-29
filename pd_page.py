from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://academybugs.com/store/dnk-yellow-shoes/")
add_to_cart_pdp = driver.find_element(By.XPATH, "//input[@type='submit' and @value='ADD TO CART']")
add_to_cart_pdp.click()
time.sleep(5)
assert "https://academybugs.com/my-cart/" in driver.current_url

