Feature: Search, Add Cheapest Items, and Checkout Redirection

Background:
    Given I am on the Amazon as a new user

Scenario Outline: Search, Filter and Add cheapest product to cart 
    When I search for <product>
    And I sort the search results by price in ascending order
    And I check if there are available <product> in my country
    And I add to cart the cheapest <product>

Examples:
    | product  |
    | snickers |
    | skittles |

Scenario: Verify basket total matches, proceed to checkout and get redirected
    When I check the total of the added items
    When I go to cart
    Then The basket should display the correct total for the added items
    When I proceed to Checkout
    Then I should be redirected to the Registration page