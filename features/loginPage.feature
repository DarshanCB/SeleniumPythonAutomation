Feature: Login to Amazon E-Commerce portal with user name and password

  Scenario: Login with valid user name and password
    Given Launch chrome browser
    When Open Amazon.de home page with valid URL
    When Click on the login page and login page of the Amazon portal should open
    Then Input the valid user name darshancbeceng@gmail.com
    Then Input the valid password **qwER1234##
    And Click on the login button to open the amazon and Validate the user Hello, Darshan
    Then Close the browser

  Scenario Outline: Login with valid user name and password
    Given Launch chrome browser
    When Open Amazon.de home page with valid URL
    When Click on the login page and login page of the Amazon portal should open
    Then Input the valid user name <username>
    Then Input the valid password <password>
    And Click on the login button to open the amazon and Validate the user <user>
    Then Close the browser

    Examples:
      | username                     | password     | user           |
      | darshancbeceng@gmail.com     | **qwER1234## | Hello, Darshan |
      | darshancbeceng1993@gmail.com | **qwER1234## | Hello, DarshanCB |

  Scenario Outline: Login with invalid user name and password
    Given Launch chrome browser
    When Open Amazon.de home page with valid URL
    When Click on the login page and login page of the Amazon portal should open
    Then Input the valid user name <invalusername>
    Then Input the valid password <invalpassword>
    And Click on the login button to open the amazon and Validate the user Hello, Darshan
    Then Close the browser

  Examples:
    | invalusername      | invalpassword |
    | admin@gmail.com    | **qwER1234##  |
    | admin123@gmail.com | **qwER1234##  |







