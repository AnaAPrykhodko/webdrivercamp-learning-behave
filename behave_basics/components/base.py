from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
        element.click()

    def find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return element

    def find_visible_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
        return element

    def find_all_elements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, locator))
        )
        return elements
