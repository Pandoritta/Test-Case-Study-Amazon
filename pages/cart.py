from pages.search_page import SearchPage
from selenium.webdriver.common.by import By
import logging
import csv
import os

class CartPage(SearchPage):

    #Locators
    SUBTOTAL = (By.XPATH, '//*[@id="sc-subtotal-amount-activecart"]/span')
    CHECKOUT = (By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span')

    def check_cart_has_items(self):
        """Check if the cart has items
        Opens the total_prods.csv file and checks if it has any rows

        Returns:
            bool: True if the cart has items, False otherwise
        """

        with open('features/total_prods.csv', 'r') as f:
            reader = csv.reader(f)
            if os.path.getsize('features/total_prods.csv') == 0:
                return False
            if sum(1 for row in reader if row) > 0:
                return True
    
    def get_subtotal(self):
        """Get the subtotal of the cart
        Get the subtotal of the cart and return it as a float
            
        Returns:    
            float: Subtotal of the cart"""
        try:
            subtotal = self.find_element(*self.SUBTOTAL)
            subtotal = subtotal.get_attribute("textContent")
            subtotal = float(subtotal.replace("$", ""))
        except Exception as err:
            logging.debug(f"Error getting subtotal due to: {str(err)}") 
        return subtotal
    
    def proceed_to_checkout(self):
        """Proceed to checkout
        Uses base function clickable to click on the checkout button"""
        self.clickable(*self.CHECKOUT)
        return None
    
    def title(self):
        """Get the title of the page
        Get the title of the page and return it as a string
                
        Returns:
            str: Title of the page
        """
        return self.browser.title



