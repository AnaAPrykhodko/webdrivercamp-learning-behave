from selenium import webdriver
from behave_basics.components.base import Base

def before_all(context):
    browser = webdriver.Chrome()
    context.browser = browser
    context.helper = Base(browser)


def after_all(context):
    context.browser.quit()
