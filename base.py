from appium import webdriver
class Base():
    @staticmethod
    def start(self,url,dervice):
        self.driver=webdriver.Remote(url,dervice)
    @staticmethod
    def class_name_click(self,loc):
        self.driver.find_element_by_class_name(loc).click()
    @staticmethod
    def id_click(self,loc):
        self.driver.find_element_by_id(loc).click()
    @staticmethod
    def name_click(self,loc):
        self.driver.find_element_by_name(loc).click()
    @staticmethod
    def class_name(self,loc):
        return self.driver.find_element_by_class_name(loc)
    @staticmethod
    def by_id(self,loc):
        return self.driver.find_element_by_id(loc)
    @staticmethod
    def id_click_number(self,loc,number):
        self.driver.find_element_by_id(loc)[str(number)].click()
    @staticmethod
    def by_name(self,loc):
        return self.driver.find_element_by_name(loc)
    @staticmethod
    def class_name_text(self,loc):
        return self.driver.find_element_by_class_name(loc).text
    @staticmethod
    def id_text(self,loc):
        return self.driver.find_element_by_id(loc).text
    @staticmethod
    def name_text(self,loc):
        return self.driver.find_element_by_name(loc).text
    @staticmethod
    def class_name_getattribute(self,loc,value):
        return self.driver.find_element_by_class_name(loc).get_attribute(value)
    @staticmethod
    def id_getattribute(self,loc,value):
        return self.driver.find_element_by_id(loc).get_attribute(value)
    @staticmethod
    def id_getattribute_number(self,loc,number,value):
        return self.driver.find_element_by_id(loc)[str(number)].get_attribute(value)
    @staticmethod
    def name_getattribute(self,loc):
        return self.driver.find_element_by_name(loc).get_attribute('value')
    @staticmethod
    def calss_name_size(self,loc):
        return self.driver.find_element_by_class_name(loc).size
    @staticmethod
    def class_name_clear(self,loc):
        self.driver.find_element_by_class_name(loc).clear()
    @staticmethod
    def id_clear(self,loc):
        self.driver.find_element_by_id(loc).clear()
    @staticmethod
    def class_name_sendkey(self,loc,key):
        return self.driver.find_element_by_class_name(loc).send_keys(key)
    @staticmethod
    def id_sendkey(self,loc,key):
        return self.driver.find_element_by_id(loc).send_keys(key)
    @staticmethod
    def name_sendkey(self,loc,key):
        return self.driver.find_element_by_name(loc).send_keys(key)
    @staticmethod
    def class_name_click_number(self,loc,number):
        self.driver.find_elements_by_class_name(loc)[int(number)].click()
    @staticmethod
    def class_name_text_number(self,loc,number):
        self.driver.find_elements_by_class_name(loc)[int(number)].text
    @staticmethod
    def class_name_sendkey_number(self,loc,number,key):
        self.driver.find_elements_by_class_name(loc)[int(number)].send_keys(key)
    @staticmethod
    def id_text_number(self,loc,number):
        self.driver.find_element_by_id(loc)[int(number)].text

