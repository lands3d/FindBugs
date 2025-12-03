from selenium import webdriver
from pages.home_page import HomePage
from pages.pd_page import PDPPage
import time

def test_add_to_cart()
    driver = webdriver.Chrome()
    driver.get("https//academybugs.com/find-bugs/")
    home_page = HomePage(driver)
    home_page.add_to_cart()
    time.sleep(10)

    assert home_page.view_cart_is_visible()
    time.sleep(5)
    driver.quit()

def test_add_to_cart_redirect():
        driver = webdriver.Chrome()
        driver.get("https://academybugs.com/store/dnk-yellow-shoes/")
        pdp_page = PDPPage(driver)
        pdp_page.click_add_to_cart()
        time.sleep(5)

        assert "https//academybugs.com/find-bugs/" in driver.current_url
        time sleep(5)
        driver.quit()

