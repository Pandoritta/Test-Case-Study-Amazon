from pages.base import BasePage
from selenium.webdriver.common.by import By


class AmazonHomePage(BasePage):

    SEARCH_BOX = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='nav-search-bar-form']/div[3]")

    def search_product(self, product):
        """Search for a product on Amazon
        Uses base function to send keys and click on the button
        
        Args:
            product: The product to search for
        Returns:
            product: The product searched for
        """
        self.send_keys(*self.SEARCH_BOX, product)
        self.clickable(*self.SEARCH_BUTTON)
        return product
    
