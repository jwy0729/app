from random import random
from time import sleep
import configparser
from base import base
from DropDown import DropDown
from ReturnPage import Returnpage
from WorkOrder.Created import created
class InspectionHistory():
    DropDown =DropDown()
    Returnpage=Returnpage()
    create=created()
    def __init__(self):
        pass
    def inspectionHistory(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'巡检查询')
        except BaseException:
            try:
                base.name_click(u'巡检')
                base.name_click(u'巡检查询')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'巡检')
                base.name_click(u'巡检查询')
        sleep(5)
        base.id_click('com.facilityone.product.shang:id/patrol_task_query_fliter_tv')
        base.id_sendkey('com.facilityone.product.shang:id/patrol_task_query_name_et',cp.get('patrol','patrolname'))
        base.id_click('com.facilityone.product.shang:id/patrol_task_query_menu_fliter_sure_btn')
        base.class_name_click('android.widget.RelativeLayout')
        base.driver.implicitly_wait(300)
        base.class_name_click('android.widget.LinearLayout')
        base.driver.implicitly_wait(0)
        base.class_name_click('android.widget.LinearLayout')
        InspectionHistory.Returnpage.returnpage()
        InspectionHistory.Returnpage.returnpage()
    def Inspection(self):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'巡检查询')
        except BaseException:
            try:
                base.name_click(u'巡检')
                base.name_click(u'巡检查询')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'巡检')
                base.name_click(u'巡检查询')
        sleep(5)
        base.id_click('com.facilityone.product.shang:id/patrol_task_query_fliter_tv')
        base.id_click('com.facilityone.product.shang:id/patrol_task_query_menu_fliter_reset_btn')
        InspectionHistory.DropDown.dropDown()
        InspectionHistory.DropDown.dropDown()
        base.id_click('com.facilityone.product.shang:id/content_ll')
        base.id_click('com.facilityone.product.shang:id/patrol_task_query_menu_fliter_sure_btn')
        j, k, n,i=1
        for i in range(10):
            try:
                base.class_name_click('android.widget.RelativeLayout')
                break
            except BaseException:
                base.id_click('com.facilityone.product.shang:id/patrol_task_query_pre_tv')
                i=i+1
        for n in range(100):
            try:
                base.id_click('com.facilityone.product.shang: id / patrol_group_item_exception_status_tv')
                break
            except BaseException:
                InspectionHistory.DropDown.dropDown()
                n = n + 1

        for j in range(100):
            base.class_name_click_number('android.widget.LinearLayout',j)
            for k in range(100):
                try:
                    base.id_click('com.facilityone.product.shang:id/patrol_task_history_dianwei_question_repair_btn')
                    base.name_click('报修')
                    InspectionHistory.create.create('巡检')
                    z=0
                    break
                except BaseException:
                    InspectionHistory.DropDown.dropDown()
            if z==0:
                break
            else:
                j=j+1
        if z!=0:
            print('无异常数据')