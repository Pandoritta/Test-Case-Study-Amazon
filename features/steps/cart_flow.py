from behave import given, step, when, then
from pages.cart import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@given('I am on the Amazon as a new user')
def step_impl(context):
    context.amazon = CartPage(context.browser)

@when('I search for "snickers"')
def step_impl(context, product='snickers'):
    context.amazon.search_product(product)

@step('I add the cheapest "snickers" to cart')
def step_impl(context, product = 'snickers'):
    items_on_page = context.amazon.get_sorted_results()
    products_availability = context.amazon.find_available_products(product, items_on_page)
    assert products_availability, f'No available options to add for {product} in the country'
    context.amazon.add_cheapest_to_cart(products_availability)

@step('I search for "skittles"')
def step_impl(context, product='skittles'):
    context.amazon.search_product(product)

@step('I add the cheapest "skittles" to cart')
def step_impl(context, product = 'skittles'):
    items_on_page = context.amazon.get_sorted_results()
    products_availability = context.amazon.find_available_products(product, items_on_page)
    assert products_availability, f'No available options to add for {product} in the country'
    context.amazon.add_cheapest_to_cart(products_availability)

@step('I go to cart')
def step_impl(context):
    context.amazon.go_to_cart()

@then('The basket should display the correct total for the added items')
def step_impl(context):
    total = context.amazon.total_items()
    subtotal = context.amazon.get_subtotal()
    assert total == subtotal, f'Expected total: {total}, Actual total: {subtotal}'

@when('I proceed to Checkout')
def step_impl(context):
    context.amazon.proceed_to_checkout()

@then('I am redirected to Registration')
def step_impl(context, expected_title = 'Amazon Sign-In'):
    WebDriverWait(context.browser, 10).until(EC.title_is(expected_title))
    title = context.browser.title
    assert title == expected_title, f"Expected: {expected_title}, Actual: {title}"

