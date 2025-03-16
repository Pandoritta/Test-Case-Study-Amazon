from pages.base import BasePage
from selenium.webdriver.common.by import By


class AmazonHomePage(BasePage):

    #Locators
    SEARCH_BOX = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='nav-search-bar-form']/div[3]")

    def search_product(self, product):
        self.send_keys(*self.SEARCH_BOX, product)
        self.clickable(*self.SEARCH_BUTTON)
        return product
    
