import os
import csv
from dotenv import load_dotenv
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

load_dotenv()

def before_all(context):
    """Setup the environment for the tests
    1. Set the browser  to be used
    2. Set the driver path based on the OS (Windows, Linux, MacOS)    
    3. Creates a csv that will hold the cheapest price for each product

    Args:   
        context: Behave context object
    Returns:
        None
    """
    os_type = platform.system().lower()
    base_path = os.path.join(os.path.dirname(__file__), '..', 'drivers')
    
    if 'windows' in os_type:
        driver_path = os.path.join(base_path, 'windows', 'chromedriver-win32')
    elif 'linux' in os_type:
        driver_path = os.path.join(base_path, 'linux', 'chromedriver-linux64')
    elif 'darwin' in os_type:  
        driver_path = os.path.join(base_path, 'macos', 'chromedriver-mac-arm64', 'chromedriver')
    else:
        raise Exception("Unknown OS")
    

    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at: {driver_path}") 

    service = Service(executable_path=driver_path)

    options = webdriver.ChromeOptions()
    context.browser = webdriver.Chrome(service=service, options=options)
    context.browser.maximize_window()

    if not os.path.exists('features/total_prods.csv'):
        with open('features/total_prods.csv', 'w') as f:
            pass

def after_all(context):
    """Tear down the environment after the tests
    1. Close the browser
    2. Delete the csv file

    Args:
        context: Behave context object
    Returns:
        None
    """
    context.browser.quit()
    if os.path.exists('features/total_prods.csv'):
        os.remove('features/total_prods.csv')
