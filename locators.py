from selenium.webdriver.common.by import By

class MainPageLocators:
    LOG_AND_REGISTER_BUTTON = (By.XPATH, ".//button[contains(text(),'Вход и регистрация')]")
    POST_AD_BUTTON = (By.XPATH, ".//button[contains(text(),'Разместить объявление')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='name']") 
    APPLY_BUTTON = (By.XPATH, ".//button[contains(text(),'Применить')]")
    
    LOGIN_LOG_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти')]")
    LOGIN_NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(),'Нет аккаунта')]") 
    LOGIN_EMAIL = (By.XPATH, ".//input[@name='email']")
    LOGIN_PASSWORD = (By.XPATH, ".//input[@name='password']")
    
    REGISTER_CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(),'Создать аккаунт')]")
    REGISTER_HAVE_ALREADY_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(),'Уже есть аккаунт')]")
    REGISTER_EMAIL = (By.XPATH, ".//input[@name='email']") 
    REGISTER_PASSWORD = (By.XPATH, ".//input[@name='password']") 
    REGISTER_PASSWORD_REPEAT = (By.XPATH, ".//input[@name='submitPassword']") 

    AVATAR = (By.XPATH, ".//button[contains(@class, 'circleSmall')]")
    NAME_USER = (By.XPATH, ".//h3[@class='profileText name']")

    EMAIL_ERROR = (By.XPATH, ".//span[contains(text(), 'Ошибка')]")
    FIELDS_ERROR = (By.XPATH, ".//div[contains(@class, 'input_inputError')]")

    LOGOUT = (By.XPATH, ".//button[contains(text(), 'Выйти')]")

    MODAL_WINDOW = (By.XPATH, ".//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]") 
   
    AD_NAME = (By.XPATH, "//input[@name='name']")
    AD_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
    AD_PRICE = (By.XPATH, "//input[@name='price']")
    AD_PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

    DROPDOWN_CATEGORY_ARROW = (By.XPATH, "(//button[contains(@class,'dropDownMenu_arrow')])[1]")
    DROPDOWN_CITY_ARROW = (By.XPATH, "(//button[contains(@class,'dropDownMenu_arrow')])[2]")

    DROPDOWN_CATEGORY_BOOK = (By.XPATH, "//span[contains(text(), 'Книги')]")
    DROPDOWN_CITY_SP = (By.XPATH, "//span[contains(text(), 'Санкт-Петербург')]")

    RADIOBUTTON_BY = (By.XPATH, "//div[@class='radioUnput_inputRegular__FbVbr']")

    AD_LAST_CARD = (By.XPATH, "//div[@class='card'][last()]")

    MY_PROFILE = (By.XPATH, "//h1[contains(text(), 'Мой профиль')]")
