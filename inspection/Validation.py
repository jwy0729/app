import random
from time import sleep
from appium import webdriver
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser
from appium.webdriver.common.touch_action import TouchAction

from base import base


class Validation():
    DropDown=DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def validation(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'查验验收')
        except BaseException:
            try:
                base.name_click(u'承接查验')
                base.name_click(u'查验验收')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'承接查验')
                base.name_click(u'查验验收')
        base.name_click(cp.get('inspection','vtask'))
        base.name_click('验收')
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.GridView').click()
        sleep(2)
        TouchAction(base.driver).press(100,100).move_to(300,400).release().perform()
        base.name_click('保存')
        base.id_sendkey('com.facilityone.product.shang:id/popup_content_et','承接查验验收描述')
        base.name_click('确定')
        Validation.Returnpage.returnpage()
