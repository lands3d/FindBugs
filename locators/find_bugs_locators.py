from selenium.webdriver.common.by import By

class HomePageLocators:
    ADD_TO_CART = (By.ID, "ec_add_to_cart_5")
    VIEW_CART = (By.XPATH, "/html/body/div[3]/div/div/div/main/article/div/section/div[2]/a")

class ProductDetailsPageLocators:
    ADD_TO_CART_PDP = (By.XPATH, "//input[@type='submit' and @value='ADD TO CART']")
