from DropDown import DropDown
from ReturnPage import returnpage
import random
import configparser
from time import sleep
class Affiche():
    DropDown = DropDown()
    ReturnPage=returnpage()
    def Unread(self,base):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'公告')
        except:
                base.name_click(u'工作')
                base.name_click(u'公告')
        base.class_name_click_number('android.widget.RelativeLayout',1)
        title=base.id_text('com.facilityone.product.shang:id/tv_detail_title')
        returnpage.returnpage(base)
        return title
    def Read(self,base,title):
        base.id_click('com.facilityone.product.shang:id/textview')
        i=0
        while i<=100:
           try:
               base.name_click(title)
               break
           except:
               DropDown.dropDown(base)
           i=i+1
