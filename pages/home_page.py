from locators.find_bugs_locators import HomePageLocators
from selenium import webdriver
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(*HomePageLocators.ADD_TO_CART).click()

    def view_cart_is_visible(self):
        return self.driver.find_element(*HomePageLocators.VIEW_CART).is_displayed()




