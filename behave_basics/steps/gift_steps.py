from behave import *
from time import sleep
from decimal import Decimal



@step('Navigate to {url}')
def step_impl(context, url):
    context.browser.get(url)




@step('Search for {search_item}')
def step_impl(context, search_item):
    context.helper.find_element("//input[@id='search']").send_keys(search_item)
    context.helper.click("//button[@type='submit']")


@step('Verify header of the page contains {search_item}')
def step_impl(context, search_item):
    context.helper.find_element(f"//h1[contains(.,'{search_item}')]")


@step('Select {option} in {section} section')
def step_impl(context, option, section):
    context.helper.click(f"//div[@data-test='pictureNavigation']"
                         f"[.//h2//span[text()='{section}']]//span[text()='{option}']")


@step('Collect all items on the first page into {var}')
@step('Collect all items on the first page into {var} on the {level} level')
def step_impl(context, var, level=None):
    locator = "//span[@data-test='current-price']"
    for _ in range(5):
        sleep(3)
        context.browser.execute_script("window.scrollBy(0, 2000)")

    elements = context.helper.find_all_elements(locator)
    if level == "feature":
        setattr(context.feature, var, elements)
    else:
        setattr(context, var, elements)



@step('Verify all collected results\' {param} is {condition}')
def step_impl(context, param, condition):
    correct_price = Decimal(condition[1:])
    for element in context.feature.elements:
        head, sep, tail = element.text.strip('$ ').partition('-')
        current_price = float(head)
        if Decimal(current_price) >= correct_price:
            return False


@step('Print the current url')
def print_url(context):
    print(context.browser.current_url)
