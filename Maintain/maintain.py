from DropDown import DropDown
from ReturnPage import Returnpage
import configparser
from WipeUp import WipeUp
from time import sleep
class maintain():
    DropDown = DropDown()
    ReturnPage=Returnpage()
    WipeUp=WipeUp()
    cp = configparser.SafeConfigParser()
    cp.read('base.ini', encoding='utf-8')
    def __init__(self):
        pass
    def Asset(self,base):
        try:
            base.name_click(u'计划性维护')
        except BaseException:
                base.name_click(u'工作')
                base.name_click(u'计划性维护')
        sleep(3)
        # 左滑
        view=base.calss_name_size('android.widget.LinearLayout')
        h = int(view['height'])
        w = int(int(view['width']) * 0.7)
        w1=int(w-500)
        w2=int(w+500)
        base.driver.swipe(w,h,w1,h)
        sleep(5)
        base.driver.swipe(w,h,w2,h)
        base.driver.implicitly_wait(300)
        maintain.DropDown.dropDown(base)
        base.driver.implicitly_wait(0)
        try:
            base.class_name_click_number('android.widget.LinearLayout',1)
        except BaseException:
            print("无维护任务")
        sleep(2)
        maintain.DropDown.dropDown(base)
        maintain.ReturnPage.returnpage(base)
        sleep(1)
        WipeUp.wipeUp(base)
        maintain.ReturnPage.returnpage(base)