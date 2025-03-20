from pages.amazon_home import AmazonHomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import logging
import csv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SearchPage(AmazonHomePage):

    #Locators
    PRICE_FILTER = (By.XPATH, '//*[@id="search"]/span/div/h1/div/div[4]/div/div/form/span/span/span/span')
    LOW_TO_HIGH = (By.XPATH, '//a[@id="s-result-sort-select_1"]')

    SEARCH_RESULTS = (By.XPATH, '*//div[@role="listitem"]')

    PRODUCT_TITLE = (By.XPATH, './/div/h2[1]/span')
    PRODUCT_PRICE = (By.XPATH, './/*[@class="a-price"]/span[1]')
    ADD_TO_CART = (By.XPATH, './/*[@name="submit.addToCart"]')

    CART = (By.XPATH, '//a[@id="nav-cart"]')

    def sort_product(self):
        """Sort the products by price from low to high, uses the base function clickable
        """
        self.clickable(*self.PRICE_FILTER)
        self.clickable(*self.LOW_TO_HIGH)
        return None
    
    def get_sorted_results(self):
        """Get the search results after applying all filters

        Returns:
            results: The search results
        """
        self.sort_product()
        self.wait_DOM_loaded()
        return self.find_elements( *self.SEARCH_RESULTS)

    def find_available_products(self, product, results):

        """Find the available products that match the search criteria: 
         - title matches the product that was passed as argument
         - the price is displayed
         - the add to cart button is displayed
            
        Args: 
            product: The product to search for
            results: The search results
        Returns:
            valid_results: The valid results that match the search criteria
        """
        
        valid_results = []

        for result in results:

            try:
                title_element = result.find_element(*self.PRODUCT_TITLE)
                title_text = title_element.get_attribute("textContent").lower()
            except Exception as err:            
                logging.debug(f"Skipping result due to: {str(err)}")
                continue

            if product.lower() == title_text:
                try:
                    price = result.find_element(*self.PRODUCT_PRICE)
            
                    price = price.get_attribute("textContent")
                    price = float(price.replace("$", ""))
                except Exception as err:
                    logging.debug(f"Skipping result due to: {str(err)}")
                    continue

                try:
                    add_to_cart_button = result.find_element(*self.ADD_TO_CART)

                    add_to_cart_button
                except Exception as err:
                    logging.debug(f"Skipping result due to: {str(err)}")
                    continue

                valid_results.append((price, result))
            

        logger.info("Found %s valid results", len(valid_results))

        if not valid_results:
            return False
        
        return valid_results
        
    def add_cheapest_to_cart(self, valid_results):
        """Add the cheapest product to the cart, 
        and adds the cheapest price to a csv file - total_prods.csv(created: environment.py)

        Args:
            valid_results: The valid results that match the search criteria
        Returns:
            cheapest_price: The cheapest price
        """
        valid_results.sort(key=lambda x: x[0])
        cheapest_price, result = valid_results[0]   

        wait = WebDriverWait(result, 10)
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART))
        add_to_cart_button.click()     
        with open('features/total_prods.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([cheapest_price])
        return cheapest_price
    
    def total_items(self):
        """Get the total price of all products added to the cart
        Opens the csv file total_prods.csv(created: environment.py) and sums all the prices
        
        Returns:
            total: The total price of all products added to the cart"""
        
        total = 0
        with open('features/total_prods.csv', 'r') as f:
            reader = csv.reader(f)
            total = 0
            for row in reader:
                price = float(row[0])
                total += price
        return round(total, 2)

    def go_to_cart(self):
        """Go to the cart page
        Uses the base function clickable
        """
        self.wait_DOM_loaded()
        self.scroll_to_top(*self.CART)
        self.clickable(*self.CART)
        return None
    