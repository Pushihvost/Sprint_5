from locators import MainPageLocators as MPL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from utils.helpers import random_email, is_element_present, register_user
from utils.urls import BASE_URL
from utils.data_test import password, test_email


class TestRegistration:
    
    def test_register_user_correct_login_password_success(self, driver):

        driver.find_element(*MPL.LOG_AND_REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.LOGIN_NO_ACCOUNT_BUTTON))
        driver.find_element(*MPL.LOGIN_NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.REGISTER_EMAIL))
        driver.find_element(*MPL.REGISTER_EMAIL).send_keys(random_email())
        driver.find_element(*MPL.REGISTER_PASSWORD).send_keys(password)
        driver.find_element(*MPL.REGISTER_PASSWORD_REPEAT).send_keys(password)        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MPL.REGISTER_CREATE_ACCOUNT_BUTTON)).click()

        
        assert driver.current_url == BASE_URL #по заданию нужно, по факту не совпадает и правильно падает
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.NAME_USER)).text == "User."
        assert is_element_present(driver, MPL.AVATAR)

    @pytest.mark.parametrize('email', ('new_mail', '@yandex.ru', 'new_mail@yandex'))    
    def test_register_user_invalid_email_fail(self, driver, email):       
        
        register_user(driver, email, password)

        assert is_element_present(driver, MPL.EMAIL_ERROR)

        fields_error = driver.find_elements(*MPL.FIELDS_ERROR)
        assert fields_error is not None
        assert len(fields_error) == 3

    def test_register_exist_user_fail(self, driver):
        
        register_user(driver, test_email, password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MPL.LOGOUT)).click()
        register_user(driver, test_email, password)

        assert is_element_present(driver, MPL.EMAIL_ERROR)

        fields_error = driver.find_elements(*MPL.FIELDS_ERROR)
        assert fields_error is not None
        assert len(fields_error) == 3
