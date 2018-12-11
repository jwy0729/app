from appium import webdriver
class base():
    driver=None
    @staticmethod
    def start(url,dervice):
        base.driver=webdriver.Remote(url,dervice)
    @staticmethod
    def class_name_click(loc):
         base.driver.find_element_by_class_name(loc).click()
    @staticmethod
    def id_click(loc):
        base.driver.find_element_by_id(loc).click()
    @staticmethod
    def name_click(loc):
        base.driver.find_element_by_name(loc).click()
    @staticmethod
    def name_click_number(loc,number):
        base.driver.find_elements_by_name(loc)[int(number)].click()
    @staticmethod
    def class_name(loc):
        return base.driver.find_element_by_class_name(loc)
    @staticmethod
    def by_id(loc):
        return base.driver.find_element_by_id(loc)
    @staticmethod
    def id_click_number(loc,number):
        base.driver.find_elements_by_id(loc)[int(number)].click()
    @staticmethod
    def by_name(loc):
        return base.driver.find_element_by_name(loc)
    @staticmethod
    def class_name_text(loc):
        return base.driver.find_element_by_class_name(loc).text
    @staticmethod
    def id_text(loc):
        return base.driver.find_element_by_id(loc).text
    @staticmethod
    def name_text(loc):
        return base.driver.find_element_by_name(loc).text
    @staticmethod
    def class_name_getattribute(loc,value):
        return base.driver.find_element_by_class_name(loc).get_attribute(value)
    @staticmethod
    def id_getattribute(loc,value):
        return base.driver.find_element_by_id(loc).get_attribute(value)
    @staticmethod
    def id_getattribute_number(loc,number,value):
        return base.driver.find_element_by_id(loc)[int(number)].get_attribute(value)
    @staticmethod
    def name_getattribute(loc):
        return base.driver.find_element_by_name(loc).get_attribute('value')
    @staticmethod
    def calss_name_size(loc):
        return base.driver.find_element_by_class_name(loc).size
    @staticmethod
    def class_name_clear(loc):
        base.driver.find_element_by_class_name(loc).clear()
    @staticmethod
    def id_clear(loc):
        base.driver.find_element_by_id(loc).clear()
    @staticmethod
    def class_name_sendkey(loc,key):
        return base.driver.find_element_by_class_name(loc).send_keys(key)
    @staticmethod
    def id_sendkey(loc,key):
        return base.driver.find_element_by_id(loc).send_keys(key)
    @staticmethod
    def name_sendkey(loc,key):
        return base.driver.find_element_by_name(loc).send_keys(key)
    @staticmethod
    def class_name_click_number(loc,number):
        base.driver.find_elements_by_class_name(loc)[int(number)].click()
    @staticmethod
    def class_name_text_number(loc,number):
       return base.driver.find_elements_by_class_name(loc)[int(number)].text
    @staticmethod
    def class_name_sendkey_number(loc,number,key):
        base.driver.find_elements_by_class_name(loc)[int(number)].send_keys(key)
    @staticmethod
    def id_text_number(loc,number):
        return base.driver.find_element_by_id(loc)[int(number)].text
    @staticmethod
    def quit():
        base.driver.quit()


