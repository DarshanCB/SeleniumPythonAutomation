Feature: Login to Amazon E-Commerce portal with invalid user name

  Scenario Outline: Login with invalid user name and valid password
    Given Launch chrome browser again
    When Open Amazon.de home page with valid URL for invalid credentials validation
    Then Set the english language option
    When Click on the login page and login page of the Amazon portal should open properly
    Then Input the invalid user name <invalusername>
    And Error message should be thrown with message There was a problem
    And Email is incorrect We cannot find an account with that e-mail address
    Then Close the chrome browser

  Examples:
    | invalusername                           |
    | admindarshandarshan@gmail.com           |
    | admin123darshan@gmail.com               |
    | darshanchickmagalurbasavaraju@gmail.com |







