import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib
from urllib import request
from requests import request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

URL = "https://www.amazon.de/"


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path= '/Users/darshancb/PycharmProjects/AutomationFramework/chromedriver')

@when('Open Amazon.de home page with valid URL')
def openHomePage(context):
    context.driver.get(URL)
    context.driver.maximize_window()

@when('Click on the login page and login page of the Amazon portal should open')
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

@then('Input the valid user name {user}')
def validUserName(context, user):
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

@then('Input the valid password {pwd}')
def validPassword(context, pwd):
    try:
        setpassword = context.driver.find_element_by_xpath("//*[@id='ap_password']")
        setpassword.send_keys(pwd)
    except NoSuchElementException as e:
        print(e.msg)
    context.driver.find_element_by_xpath("//*[@id='signInSubmit']").click()
    time.sleep(2)


@then('Click on the login button to open the amazon and Validate the user {username}')
def clickLoginbuttonValidateUser(context, username):
    try:
        usernamevalidation = context.driver.find_element_by_xpath("//*[@id='nav-link-accountList-nav-line-1']").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    assert usernamevalidation == username, "Test Passed"

@then('Close the browser')
def closeBrowser(context):
    context.driver.close()


