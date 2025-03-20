Feature: Search, Add Cheapest Items, and Checkout Redirection

Background:
    Given I am on the Amazon as a new user

Scenario:
When I search for "snickers"
And I add the cheapest "snickers" to cart
And I search for "skittles"
And I add the cheapest "skittles" to cart
And I go to cart
Then The basket should display the correct total for the added items
When I proceed to Checkout
Then I am redirected to Registration 