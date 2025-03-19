from behave import given, step, when, then
from pages.cart import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


@given("I am on the Amazon as a new user")
def step_impl(context):
    context.amazon = CartPage(context.browser)
    context.amazon.open_homepage()

@when("I search for {product}")
def step_impl(context, product):
    context.amazon.search_product(product)

@step("I sort the search results by price in ascending order")
def step_impl(context):
    context.amazon.sort_product()



@step("I check if there are available {product} in my country")
def step_impl(context, product):
    results = context.amazon.get_sorted_results()
    valid_results = context.amazon.find_available_products(product, results)
    assert valid_results, f"No valid products found for {product}"
    context.valid_results = valid_results

@step("I add to cart the cheapest {product}")
def step_impl(context, product):
    context.amazon.add_cheapest_to_cart(context.valid_results)

@when("I check the total of the added items")
def step_impl(context):
    total = context.amazon.total_items()
    context.total = total
    if not context.amazon.check_cart_has_items():
        raise unittest.SkipTest("No added items, as products not available in the country")
        

@when("I go to cart")
def step_impl(context):
    context.amazon.go_to_cart()

@then("The basket should display the correct total for the added items")
def step_impl(context):
    subtotal = context.amazon.get_subtotal()
    assert context.total == subtotal, f"Expected: {context.total}, Actual: {subtotal}"


@when("I proceed to Checkout")
def step_impl(context):
    context.amazon.proceed_to_checkout()

@then("I should be redirected to the Registration page")
def step_impl(context, expected_title = 'Amazon Sign-In'):
    WebDriverWait(context.browser, 10).until(EC.title_is(expected_title))
    title = context.browser.title
    assert title == expected_title, f"Expected: {expected_title}, Actual: {title}"



