from locators.find_bugs_locators import ProductDetailsPageLocators


class PDPPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        self.driver.find_element(*ProductDetailsPageLocators.ADD_TO_CART_PDP).click()
