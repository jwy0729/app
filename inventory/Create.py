import random
import configparser
from time import sleep
from DropDown import DropDown
from base import base
import unittest

class create(unittest.TestCase):
    DropDown=DropDown()
    # def __init__(self):
    #     pass
    def create(self):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'新建物资')
            except BaseException:
                try:
                    base.name_click(u'库存')
                    base.name_click(u'新建物资')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'库存')
                    base.name_click(u'新建物资')
            base.name_click('点击选择仓库')
            base.driver.implicitly_wait(300)
            base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'warehouse'))
            sleep(2)
            l = len(base.driver.find_elements_by_class_name('android.widget.RelativeLayout'))
            base.class_name_click_number('android.widget.RelativeLayout', int(int(l) - 1))
            base.driver.implicitly_wait(0)
            i = random.randint(0, 10000)
            base.id_sendkey('com.facilityone.product.shang:id/et_shelves', '货架信息' + str(i))
            base.id_sendkey('com.facilityone.product.shang:id/material_info_name', '物资' + str(i))
            base.id_sendkey('com.facilityone.product.shang:id/material_info_code', 'bm' + str(i))
            base.id_sendkey('com.facilityone.product.shang:id/material_info_unit', 'kg' + str(i))
            create.DropDown.dropDown()
            base.driver.implicitly_wait(200)
            base.id_sendkey('com.facilityone.product.shang:id/material_info_brand', '品牌' + str(i))
            base.driver.implicitly_wait(0)
            base.id_sendkey('com.facilityone.product.shang:id/material_info_model', 'NHG' + str(i))
            base.id_sendkey('com.facilityone.product.shang:id/material_info_ratified_price', str(i))
            create.DropDown.dropDown()
            base.id_sendkey('com.facilityone.product.shang:id/material_info_minimum_stock', 21)
            base.driver.implicitly_wait(200)
            base.id_sendkey('com.facilityone.product.shang:id/material_info_initial_number', 10)
            base.driver.implicitly_wait(0)
            base.name_sendkey('请输入或选择供应商', '供应商' + str(i))
            create.DropDown.dropDown(base)
            base.id_sendkey('com.facilityone.product.shang:id/et_cost', 22)
            base.id_click('com.facilityone.product.shang:id/et_select_due_date')
            base.name_click('确定')
            due_date = base.id_text('com.facilityone.product.shang:id/et_select_due_date')
            create.DropDown.dropDown()
            base.name_sendkey('请输入备注', '库存备注' + str(i))
            base.name_click("保存")
            sleep(7)
            return '物资' + str(i)
        except BaseException:
            self.assertEqual(0,1, "库存新建物资模块，测试未通过")
