from DropDown import DropDown
from ReturnPage import Returnpage
import configparser
from WipeUp import WipeUp
from time import sleep

from base import base


class Maintain():
    DropDown = DropDown()
    ReturnPage=Returnpage()
    WipeUp=WipeUp()
    cp = configparser.SafeConfigParser()
    cp.read('base.ini', encoding='utf-8')
    def __init__(self):
        pass
    def maintain(self):
        try:
            base.name_click(u'计划性维护')
        except BaseException:
                base.name_click(u'工作')
                base.name_click(u'计划性维护')
        sleep(5)
        Maintain.DropDown.dropDown()
        try:
            base.class_name_click_number('android.widget.LinearLayout',1)
            Maintain.DropDown.dropDown()
            Maintain.ReturnPage.returnpage()
        except BaseException:
            print("无维护任务")
        sleep(2)
        Maintain.WipeUp.wipeUp()
        sleep(2)
        Maintain.ReturnPage.returnpage()