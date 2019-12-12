from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART = (By.CSS_SELECTOR,'.hidden-xs a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")	
	REG_FORM = (By.CSS_SELECTOR, "#register_form")
	PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
	PASSWORD_REP = (By.CSS_SELECTOR, "#id_registration-password2")
	EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
	REG_BTN = (By.CSS_SELECTOR, '#register_form .btn-primary')

class ProductPageLocators():
	BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
	TITLE = (By.TAG_NAME, 'h1')
	PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
	MSG = (By.CSS_SELECTOR, '.alertinner>strong')
	MSG_PRICE = (By.CSS_SELECTOR, '.alertinner p>strong')
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong')

class BasketPageLocators():
	EMPTY_MSG = (By.CSS_SELECTOR, '#content_inner p')