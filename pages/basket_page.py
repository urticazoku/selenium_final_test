from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def cart_should_be_empty(self):
    	msg = self.browser.find_element(*BasketPageLocators.EMPTY_MSG).text
    	assert "empty" in msg, "Basket should be empty, but not"