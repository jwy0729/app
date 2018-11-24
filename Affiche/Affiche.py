from DropDown import DropDown
from ReturnPage import Returnpage
import random
import configparser
from base import base
from time import sleep
class Affiche():
    DropDown = DropDown()
    ReturnPage=Returnpage()
    def __init__(self):
        pass
    def Unread(self):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'公告')
        except BaseException:
                base.name_click(u'工作')
                base.name_click(u'公告')
        base.class_name_click_number('android.widget.RelativeLayout',1)
        title=base.id_text('com.facilityone.product.shang:id/tv_detail_title')
        Affiche.ReturnPager.Returnpage()
        return title
    def Read(self,title):
        base.id_click('com.facilityone.product.shang:id/textview')
        i=0
        while i<=100:
           try:
               base.name_click(title)
               break
           except BaseException:
               DropDown.dropDown()
           i=i+1
