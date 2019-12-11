from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")	
	REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
	TITLE = (By.TAG_NAME, 'h1')
	PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
	MSG = (By.CSS_SELECTOR, '.alertinner>strong')
	MSG_PRICE = (By.CSS_SELECTOR, '.alertinner p>strong')
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong')