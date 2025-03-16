from pages.amazon_home import AmazonHomePage
from selenium.webdriver.common.by import By
import logging
import csv



class SearchPage(AmazonHomePage):

    #Locators
    PRICE_FILTER = (By.XPATH, '//*[@id="search"]/span/div/h1/div/div[4]/div/div/form/span/span/span/span')
    LOW_TO_HIGH = (By.XPATH, '//a[@id="s-result-sort-select_1"]')

    DEPARTMENT = (By.XPATH, '//*[@id="departments"]/ul/span[1]/span[1]/li[1]')
    BRAND_SNICKERS = (By.XPATH, '//*[@id="p_123/256198"]/span/a/span')
    BRAND_SKITTLES = (By.XPATH, '//*[@id="p_123/265191"]/span/a/span')

    SEARCH_RESULTS = (By.XPATH, '//div[@role="listitem"]')
    PRODUCT_TITLE = (By.XPATH, './/div/h2[1]/span')
    PRODUCT_PRICE = (By.XPATH, './/*[@class="a-price"]/span[1]')
    ADD_TO_CART = (By.XPATH, './/*[@name="submit.addToCart"]')

    CART = (By.XPATH, '//a[@id="nav-cart"]')

    #Sorts the price from low to high
    def sort_product(self):
        self.clickable(*self.PRICE_FILTER)
        self.clickable(*self.LOW_TO_HIGH)
        return None

    #Returns the search results after applying all filters
    def get_sorted_results(self):
        results = self.find_elements(*self.SEARCH_RESULTS)
        return results
    
    def find_available_products(self, product, results):

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

        if not valid_results:
            return False
        
        return valid_results
        
    def add_cheapest_to_cart(self, valid_results):
        valid_results.sort(key=lambda x: x[0])
        cheapest_price, result = valid_results[0]   

        add_to_cart_button = result.find_element(*self.ADD_TO_CART)
        add_to_cart_button.click()     
        with open('features/total_prods.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([cheapest_price])
        return cheapest_price
    
    def total_items(self):
        total = 0
        with open('features/total_prods.csv', 'r') as f:
            reader = csv.reader(f)
            total = 0
            for row in reader:
                price = float(row[0])
                total += price
        return total

    def go_to_cart(self):
        self.clickable(*self.CART)
        return None

    
    


    
