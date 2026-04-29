import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators as MPL


def random_email():
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f'{login}@yandex.ru'

def is_element_present(driver, locator):
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locator))
        return True
    except:
        return False


def register_user(driver, email, password):
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.LOG_AND_REGISTER_BUTTON)).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.LOGIN_NO_ACCOUNT_BUTTON))
    driver.find_element(*MPL.LOGIN_NO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.REGISTER_EMAIL))
    driver.find_element(*MPL.REGISTER_EMAIL).send_keys(email)
    driver.find_element(*MPL.REGISTER_PASSWORD).send_keys(password)
    driver.find_element(*MPL.REGISTER_PASSWORD_REPEAT).send_keys(password)        
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MPL.REGISTER_CREATE_ACCOUNT_BUTTON)).click()


