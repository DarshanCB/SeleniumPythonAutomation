import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

URL = "https://www.amazon.de/"


@given('Launch chrome browser again')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path= '/Users/darshancb/PycharmProjects/AutomationFramework/chromedriver')

@when('Open Amazon.de home page with valid URL for invalid credentials validation')
def openHomePage(context):
    context.driver.get(URL)
    context.driver.maximize_window()

@then('Set the english language option')
def setEnglishLanguage(context):
    context.driver.find_element_by_xpath('//*[@id="icp-nav-flyout"]/span/span[2]').click()
    context.driver.find_element_by_xpath('//*[@id="customer-preferences"]/div/div/form/div[1]/div[1]/div[2]/div/label/i').click()
    context.driver.find_element_by_xpath('//*[@id="icp-btn-save"]/span/input').click()
    time.sleep(4)

@when('Click on the login page and login page of the Amazon portal should open properly')
def clickLoginPage(context):
    time.sleep(2)
    try:
        element_hover = context.driver.find_element_by_xpath("//*[@id='nav-link-accountList']")
    except NoSuchElementException as e:
        print(e.msg)
    hover = ActionChains(context.driver).move_to_element(element_hover)
    hover.perform()
    try:
        context.driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a/span").click()
    except NoSuchElementException as e:
        print(e.msg)
    time.sleep(3)


@then('Input the invalid user name {user}')
def invalidUserName(context, user):
    try:
        signinelement = context.driver.find_element_by_xpath("//*[@id='ap_email']")
    except NoSuchElementException as e:
        print(e.msg)
    signinelement.send_keys(user)
    try:
        context.driver.find_element_by_xpath("//*[@id='continue']").click()
    except NoSuchElementException as e:
        context.driver.close()
        assert False, "Invalid User Name"
        print(e.msg)
    time.sleep(2)

@then('Error message should be thrown with message {errormsg}')
def errorMessage(context, errormsg):
    try:
        error_message = context.driver.find_element_by_xpath("//*[@id='auth-error-message-box']/div/h4").text
        assert error_message == errormsg, 'Error message is wrong'
    except AssertionError as e:
        print(e.args)
        context.driver.close()
        assert False, "Not a valid error"
    time.sleep(2)

@then('Email is incorrect {emailerror}')
def emailError(context, emailerror):
    try:
        email_inavlid = context.driver.find_element_by_xpath('//*[@id="auth-error-message-box"]/div/div/ul/li/span').text
        assert email_inavlid == emailerror, 'Email error exception is not thrown'
    except AssertionError as e:
        context.driver.close()
        print(e.args)

@then('Close the chrome browser')
def closeBrowser(context):
    context.driver.close()


