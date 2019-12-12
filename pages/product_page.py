from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON)
        link.click()

    def get_title(self):
        return self.browser.find_element(*ProductPageLocators.TITLE).text

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def should_add_to_basket(self, title, price):
        msg_title = self.browser.find_element(*ProductPageLocators.MSG)
        msg_price = self.browser.find_element(*ProductPageLocators.MSG_PRICE)
        assert title==msg_title.text, "{} not in {}".format(title,msg.text)
        assert price==msg_price.text, "{} not in {}".format(price,msg.text)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Not dissapeared, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented, but should be"