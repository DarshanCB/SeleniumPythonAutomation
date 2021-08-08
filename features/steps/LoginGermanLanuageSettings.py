import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

URL = "https://www.amazon.de/"


@given('Launch chrome successfully')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path= '/Users/darshancb/PycharmProjects/AutomationFramework/chromedriver')

@when('Open Amazon.de home page with valid URL properly')
def openHomePage(context):
    context.driver.get(URL)
    context.driver.maximize_window()

@then('Set the german language settings')
def setEnglishLanguage(context):
    context.driver.find_element_by_xpath('//*[@id="icp-nav-flyout"]/span/span[2]').click()
    context.driver.find_element_by_xpath('//*[@id="customer-preferences"]/div/div/form/div[1]/div[1]/div[1]/div/label/i').click()
    context.driver.find_element_by_xpath('//*[@id="icp-btn-save"]/span/input').click()
    time.sleep(4)

@when('Click on the login page and login page of the Amazon portal should open with german {lingue}')
def clickLoginPage(context, lingue):
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
    try:
        signinval = context.driver.find_element_by_xpath("//*[@id='authportal-main-section']/div[2]/div/div[1]/form/div/div/div/h1").text
        assert signinval == lingue, 'Language settings is not working properly'
    except NoSuchElementException as e:
        print(e.msg)
    time.sleep(3)

@then('Input the valid user name properly {user}')
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

@then('Input the valid password properly {pwd}')
def validPassword(context, pwd):
    try:
        setpassword = context.driver.find_element_by_xpath("//*[@id='ap_password']")
        setpassword.send_keys(pwd)
    except NoSuchElementException as e:
        print(e.msg)
    context.driver.find_element_by_xpath("//*[@id='signInSubmit']").click()
    time.sleep(4)


@then('Click on the login button to validate user {username}')
def clickLoginbuttonValidateUser(context, username):
    try:
        usernamevalidation = context.driver.find_element_by_xpath("//*[@id='nav-link-accountList-nav-line-1']").text
    except:
        context.driver.close()
        assert False, "Test Failed with user name" +  str(usernamevalidation)
    assert usernamevalidation == username, "Test Passed"

@then('Close the browser properly')
def closeBrowser(context):
    context.driver.close()


