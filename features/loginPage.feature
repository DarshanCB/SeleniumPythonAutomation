Feature: Login to Amazon E-Commerce portal with user name and password

  Scenario: Login with valid user name and password
    Given Launch chrome browser
    When Open Amazon.de home page with valid URL
    Then Set the english language
    When Click on the login page and login page of the Amazon portal should open Sign-In
    Then Input the valid user name darshancbeceng@gmail.com
    Then Input the valid password **qwER1234##
    And Click on the login button to open the amazon and Validate the user Hello, Darshan
    Then Close the browser

  Scenario Outline: Login with valid user name and password
    Given Launch chrome browser
    When Open Amazon.de home page with valid URL
    Then Set the english language
    When Click on the login page and login page of the Amazon portal should open Sign-In
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
    Then Set the english language
    When Click on the login page and login page of the Amazon portal should open Sign-In
    Then Input the invalid username <invalusername>
    Then validate the error message We cannot find an account with that e-mail address
    Then Close the browser

  Examples:
    | invalusername           |
    | admin4566778@gmail.com  |
    | admin12353636@gmail.com |

  Scenario Outline: Login with valid user name and invalid password
    Given Launch chrome browser
    When Open Amazon.de home page with valid URL
    Then Set the english language
    When Click on the login page and login page of the Amazon portal should open Sign-In
    Then Input the valid user name <valusername>
    Then Input the invalid password <invalpassword>
    And Validate password error message There was a problem
    And Validate password error Your password is incorrect
    Then Close the browser

  Examples:
    | valusername                  | invalpassword |
    | darshancbeceng@gmail.com     | 345367889     |
    | darshancbeceng1993@gmail.com | 536377889     |







