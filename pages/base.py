from dotenv import load_dotenv
import os
import logging
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver, timeout=20):
        """"Initialize the BasePage, 
            Adds default wait time for the webdriver

            Args:
            driver: The selenium webdriver (environment.py)
            timeout: The wait time for the webdriver            
        """
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        logger.info("Initialized BasePage with timeout: %s seconds", timeout)

    def wait_DOM_loaded(self):
        time.sleep(5)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def open_homepage(self):
        """Open the homepage of the application"""
        try:
            url = os.getenv('BASE_URL')
            logger.info("Opening homepage: %s", url)
            self.driver.get(url)
        except Exception as e:
            logger.error("Failed to open homepage: %s", str(e))
            raise

    def find_element(self, by, value):
        """Find a single element on the page
        Args:
            by: The locator type
            value: The locator value 
        Returns:
            element: The element found
        Raises:
            TimeoutException: If the element is not found
        """
        try:
            logger.info("Finding element: %s = %s", by, value)
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            return element
        except TimeoutException:
            logger.error("Element not found: %s = %s", by, value)
            raise

    def find_elements(self, by, value):
        """Find multiple elements on the page
        Args:
            by: The locator type
            value: The locator value
        Returns:
            elements: The elements found
        Raises:
            TimeoutException: If the elements are not found
        """
        try:
            logger.info("Finding elements: %s = %s", by, value)
            elements = self.wait.until(EC.visibility_of_all_elements_located((by, value)))
            logger.info("Found %d elements", len(elements))
            return elements
        except TimeoutException:
            logger.error("Elements not found: %s = %s", by, value)
            raise

    def clickable(self, by, value):
        """Check if an element is clickable and click it
        Args:
            by: The locator type
            value: The locator value
        Returns:
            None"""
        try:
            logger.info("Clicking element: %s = %s", by, value)
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            logger.info("Element clicked successfully")
        except TimeoutException:
            logger.error("Element not clickable: %s = %s", by, value)
            raise

    def send_keys(self, by, value, text):
        """
        Finds elemnet, clears it and sends keys.

        Args:
            by: The locator type
            value: The locator value
            text: The text to send
        Returns:
            None
        """
        try:
            logger.info("Sending keys to element: %s = %s", by, value)
            element = self.find_element(by, value)
            element.clear()
            element.send_keys(text)
            logger.info("Text entered successfully: %s", text)
        except Exception as e:
            logger.error("Failed to send keys: %s", str(e))
            raise

    def wait_for_element_visible(self, by, value):
        """Wait for an element to be visible
        Args:
            by: The locator type
            value: The locator value
        """
        try:
            logger.info("Waiting for element to be visible: %s = %s", by, value)
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            logger.info("Element is now visible")
            return element
        except TimeoutException:
            logger.error("Element not visible: %s = %s", by, value)
            raise

