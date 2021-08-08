import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

URL = "https://www.amazon.de/"


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path= '/Users/darshancb/PycharmProjects/AutomationFramework/chromedriver')

@when('Open Amazon.de home page with valid URL')
def openHomePage(context):
    context.driver.get(URL)
    context.driver.maximize_window()

@then('Set the english language')
def setEnglishLanguage(context):
    context.driver.find_element_by_xpath('//*[@id="icp-nav-flyout"]/span/span[2]').click()
    context.driver.find_element_by_xpath('//*[@id="customer-preferences"]/div/div/form/div[1]/div[1]/div[2]/div/label/i').click()
    context.driver.find_element_by_xpath('//*[@id="icp-btn-save"]/span/input').click()
    time.sleep(4)

@when('Click on the login page and login page of the Amazon portal should open {signin}')
def clickLoginPage(context, signin):
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
        assert signinval == signin, 'Sign in page is not available'
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

@then('Input the invalid username {invaluser}')
def invaliduser(context, invaluser):
    try:
        signinelement = context.driver.find_element_by_xpath("//*[@id='ap_email']")
    except NoSuchElementException as e:
        print(e.msg)
    signinelement.send_keys(invaluser)
    try:
        context.driver.find_element_by_xpath("//*[@id='continue']").click()
    except NoSuchElementException as e:
        context.driver.close()
        assert False, "Invalid User Name"
        print(e.msg)
    time.sleep(2)

@then('validate the error message {errorval}')
def validateerrormsg(context, errorval):
    try:
        errormsg = context.driver.find_element_by_xpath("//*[@id='auth-error-message-box']/div/div/ul/li/span").text
        assert errormsg == errorval, 'Error message is not correct' + str(errorval)
    except AssertionError as e:
        print(e.args)

@then('Input the valid password {pwd}')
def validPassword(context, pwd):
    try:
        setpassword = context.driver.find_element_by_xpath("//*[@id='ap_password']")
        setpassword.send_keys(pwd)
    except NoSuchElementException as e:
        print(e.msg)
    context.driver.find_element_by_xpath("//*[@id='signInSubmit']").click()
    time.sleep(2)

@then('Input the invalid password {invalpwd}')
def invalidpassword(context, invalpwd):
    try:
        setpassword = context.driver.find_element_by_xpath("//*[@id='ap_password']")
        setpassword.send_keys(invalpwd)
    except NoSuchElementException as e:
        print(e.msg)
    context.driver.find_element_by_xpath("//*[@id='signInSubmit']").click()

@then('Validate password error message {pwderror}')
def passwordErrormsg(context, pwderror):
    try:
        time.sleep(5)
        errormsg = context.driver.find_element_by_xpath("//*[@id='auth-error-message-box']/div/h4").text
        print(errormsg)
    except:
        context.driver.close()
        assert False, "Test Failed"
    assert pwderror == errormsg, "Test should fail"

@then('Validate password error {errorpwd}')
def errorpassword(context, errormsg):
    try:
        pwderror = context.driver.find_element_by_xpath('//*[@id="auth-error-message-box"]/div/div/ul/li/span').text
        print(pwderror)
    except:
        context.driver.close()
        assert False, "Test Failed"
    assert pwderror == errormsg, 'invalid password'

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


