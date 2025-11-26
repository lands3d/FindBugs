from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://academybugs.com/find-bugs/")
add_to_cart = driver.find_element(By.ID, "ec_add_to_cart_5")
add_to_cart.click()
view_cart = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/main/article/div/section/div[2]/a")
time.sleep(5)
assert view_cart.is_displayed()
time.sleep(10)

