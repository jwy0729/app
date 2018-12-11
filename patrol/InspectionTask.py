from time import sleep
import configparser
from base import base
from DropDown import DropDown
from ReturnPage import Returnpage

class InspectionTask():
    DropDown =DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def inspectionTask(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            # base.driver.implicitly_wait(10)
            base.name_click(u'巡检任务')
            # base.driver.implicitly_wait(0)
        except BaseException:
            try:
                base.name_click(u'巡检')
                base.driver.implicitly_wait(30)
                base.name_click(u'巡检任务')
                base.driver.implicitly_wait(0)
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'巡检')
                base.driver.implicitly_wait(30)
                base.name_click(u'巡检任务')
                base.driver.implicitly_wait(0)
        sleep(5)
        for i in range(1000):
           try:
               base.name_click(cp.get('patrol','patrolname'))
               break
           except BaseException:
               InspectionTask.DropDown.dropDown()
               i=i+1
        sleep(2)
        l=len(base.driver.find_elements_by_class_name('android.widget.RelativeLayout'))
        for n in range(1,int(l),2):
            base.class_name_click_number('android.widget.RelativeLayout',n)
            l1=len(base.driver.find_elements_by_class_name('android.widget.RelativeLayout'))
            for j in range(0,int(l1),2):
                try:
                    base.class_name_click_number('android.widget.RelativeLayout',j)
                    InspectionTask.DropDown.dropDown()
                    sleep(2)
                    InspectionTask.Returnpage.returnpage()
                except BaseException:
                    InspectionTask.DropDown.dropDown()
                j=j+1
            InspectionTask.Returnpage.returnpage()
            n=n+1
        # base.id_click('com.facilityone.product.shang:id/patrol_spot_sync_tv')
        sleep(3)
        base.name_click('提交')
        try:
            base.id_click('com.facilityone.product.shang:id/confirm_button')
        except BaseException:
            print('没有未做项')
            sleep(3)
            InspectionTask.Returnpage.returnpage()



