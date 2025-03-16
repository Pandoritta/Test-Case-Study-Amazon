from pages.search_page import SearchPage
from selenium.webdriver.common.by import By
import logging

class CartPage(SearchPage):

    #Locators
    SUBTOTAL = (By.XPATH, '//*[@id="sc-subtotal-amount-activecart"]/span')
    CHECKOUT = (By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span')

    def get_subtotal(self):
        try:
            subtotal = self.find_element(*self.SUBTOTAL)
            subtotal = subtotal.get_attribute("textContent")
            subtotal = float(subtotal.replace("$", ""))
        except Exception as err:
            logging.debug(f"Error getting subtotal due to: {str(err)}") 
        return subtotal
    
    def proceed_to_checkout(self):
        self.clickable(*self.CHECKOUT)
        return None
    
    def title(self):
        return self.browser.title



