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
                sleep(1)
                Validation.DropDown.dropDown()
                base.name_click(u'承接查验')
                base.name_click(u'查验验收')
        base.name_click(cp.get('inspection','vtask'))
        startTime=base.id_text('com.facilityone.product.shang:id/inspection_start_time_tv')
        base.name_click('验收')
        base.driver.tap([(196,641)],1)
        sleep(2)
        element=base.driver.find_element_by_id('com.facilityone.product.shang:id/work_order_detail_hand_write_hv')
        TouchAction(base.driver).press(element,340,260).move_to(element,340,500).move_to(element,500,500).release().perform()
        base.name_click('保存')
        base.id_sendkey('com.facilityone.product.shang:id/popup_content_et','承接查验验收描述')
        base.name_click('确定')
        Validation.Returnpage.returnpage()
        return startTime
