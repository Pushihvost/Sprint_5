from locators import MainPageLocators as MPL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.helpers import is_element_present
from utils.urls import BASE_URL
from utils.data_test import password, test_email

class TestLogin:

    def test_successful_login(self, driver):

        driver.find_element(*MPL.LOG_AND_REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.LOGIN_NO_ACCOUNT_BUTTON))
        driver.find_element(*MPL.LOGIN_EMAIL).send_keys(test_email)
        driver.find_element(*MPL.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*MPL.LOGIN_LOG_BUTTON).click()

        assert driver.current_url == BASE_URL  #по заданию нужно, по факту не совпадает
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.NAME_USER)).text == "User."
        assert is_element_present(driver, MPL.AVATAR)






