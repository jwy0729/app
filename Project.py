from appium import webdriver
from time import sleep
import configparser
class project():
    def project(self,base):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        sleep(1)
        base.class_name_sendkey('android.widget.EditText',cp.get('project','proj'))
        base.id_click('com.facilityone.product.shang:id/content_rl')
        sleep(5)

