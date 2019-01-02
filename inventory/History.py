from time import sleep
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser
from base import base
import unittest
class VHistory():
    DropDown=DropDown()
    Returnpage=Returnpage()
    # def __init__(self):
    #     pass
    def history(self,W):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'库存查询')
        except BaseException:
            try:
                base.name_click(u'库存')
                base.name_click(u'库存查询')
            except BaseException:
                base.name_click(u'工作')
                sleep(1)
                VHistory.DropDown.dropDown()
                base.name_click(u'库存')
                base.name_click(u'库存查询')
        for i in range(100):
            try:
                base.name_click(cp.get('invebtory', 'warehouse'))
                break
            except:
                VHistory.DropDown.dropDown()
        base.id_click('com.facilityone.product.shang:id/tv_filter')
        base.id_sendkey('com.facilityone.product.shang:id/patrol_task_query_name_et',W)
        base.name_click('确定')
        base.id_click('com.facilityone.product.shang:id/f_material_name_tv')
        sleep(2)
        VHistory.DropDown.dropDown()
        sleep(1)
        for j in range(2):
           VHistory.Returnpage.returnpage()