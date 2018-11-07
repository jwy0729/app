from appium import webdriver
class base():
    def start(self,url,dervice):
        self.driver=webdriver.Remote(url,dervice)

    def class_name_click(self,loc):
        self.driver.find_element_by_class_name(loc).click()
    def id_click(self,loc):
        self.driver.find_element_by_id(loc).click()
    def name_click(self,loc):
        self.driver.find_element_by_name(loc).click()
    def class_name(self,loc):
        return self.driver.find_element_by_class_name(loc)
    def by_id(self,loc):
        return self.driver.find_element_by_id(loc)
    def id_click_number(self,loc,number):
        self.driver.find_element_by_id(loc)[str(number)].click()
    def by_name(self,loc):
        return self.driver.find_element_by_name(loc)
    def class_name_text(self,loc):
        return self.driver.find_element_by_class_name(loc).text
    def id_text(self,loc):
        return self.driver.find_element_by_id(loc).text
    def name_text(self,loc):
        return self.driver.find_element_by_name(loc).text
    def class_name_getattribute(self,loc,value):
        return self.driver.find_element_by_class_name(loc).get_attribute(value)
    def id_getattribute(self,loc,value):
        return self.driver.find_element_by_id(loc).get_attribute(value)
    def id_getattribute_number(self,loc,number,value):
        return self.driver.find_element_by_id(loc)[str(number)].get_attribute(value)
    def name_getattribute(self,loc):
        return self.driver.find_element_by_name(loc).get_attribute('value')
    def calss_name_size(self,loc):
        return self.driver.find_element_by_class_name(loc).size
    def class_name_clear(self,loc):
        self.driver.find_element_by_class_name(loc).clear()
    def id_clear(self,loc):
        self.driver.find_element_by_id(loc).clear()
    def class_name_sendkey(self,loc,key):
        return self.driver.find_element_by_class_name(loc).send_keys(key)
    def id_sendkey(self,loc,key):
        return self.driver.find_element_by_id(loc).send_keys(key)
    def name_sendkey(self,loc,key):
        return self.driver.find_element_by_name(loc).send_keys(key)
    def class_name_click_number(self,loc,number):
        self.driver.find_elements_by_class_name(loc)[int(number)].click()
    def class_name_text_number(self,loc,number):
        self.driver.find_elements_by_class_name(loc)[int(number)].text
    def class_name_sendkey_number(self,loc,number,key):
        self.driver.find_elements_by_class_name(loc)[int(number)].send_keys(key)
    def id_text_number(self,loc,number):
        self.driver.find_element_by_id(loc)[str(number)].text

