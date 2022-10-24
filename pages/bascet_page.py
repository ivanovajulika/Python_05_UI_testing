from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_link()       
        

    def should_be_basket_link(self):
        assert 'basket' in self.browser.current_url, 'wrong url'

    def count(self):
        message = self.browser.find_element(*BasketPageLocators.FORM_QUANTITY).get_attribute("value")
        print(f'Книг в корзине: {message}')
        return message


#Достаем значение атрибута
# nowText = driver.find_element_by_id("source").get_attribute("value")
# print(nowText)
    