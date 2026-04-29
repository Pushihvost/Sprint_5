from locators import MainPageLocators as MPL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.helpers import is_element_present
from utils.data_test import password, test_email, ad_name, ad_desc, ad_price

class TestCreateAd:

    def test_create_ad_unauthorized_user(self, driver):
        driver.find_element(*MPL.POST_AD_BUTTON).click()

        assert is_element_present(driver, MPL.MODAL_WINDOW)

    def test_create_ad_authorized_user(self, driver):

        driver.find_element(*MPL.LOG_AND_REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.LOGIN_NO_ACCOUNT_BUTTON))
        driver.find_element(*MPL.LOGIN_EMAIL).send_keys(test_email)
        driver.find_element(*MPL.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*MPL.LOGIN_LOG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.NAME_USER)).text == "User."

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MPL.POST_AD_BUTTON)).click()

        driver.find_element(*MPL.AD_NAME).send_keys(ad_name)
        driver.find_element(*MPL.AD_NAME).send_keys(ad_desc)
        driver.find_element(*MPL.AD_NAME).send_keys(ad_price)
        driver.find_element(*MPL.DROPDOWN_CATEGORY_ARROW).click()
        driver.find_element(*MPL.DROPDOWN_CATEGORY_BOOK).click()
        driver.find_element(*MPL.DROPDOWN_CITY_ARROW).click()
        driver.find_element(*MPL.DROPDOWN_CITY_SP).click()
        driver.find_element(*MPL.RADIOBUTTON_BY).click()

        driver.find_element(*MPL.AD_PUBLISH_BUTTON).click()

        driver.refresh()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MPL.AVATAR)).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MPL.MY_PROFILE))

        assert is_element_present(driver, MPL.AD_LAST_CARD)
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((MPL.AD_LAST_CARD), ad_name ))






