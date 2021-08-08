Feature: Login to Amazon E-Commerce portal with valid user name and password to test german language

  Scenario: Login with valid user name and password to test german language
    Given Launch chrome successfully
    When Open Amazon.de home page with valid URL properly
    Then Set the german language settings
    When Click on the login page and login page of the Amazon portal should open with german Anmelden
    Then Input the valid user name properly darshancbeceng@gmail.com
    Then Input the valid password properly **qwER1234##
    Then Click on the login button to validate user Hallo, Darshan
    Then Close the browser properly