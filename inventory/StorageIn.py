import random
import configparser
from time import sleep

from base import base


class StorageIn():
    def __init__(self):
        pass
    def storageIn(self,material):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'入库')
        except BaseException:
            try:
                base.name_click(u'库存')
                base.name_click(u'入库')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'入库')
        sleep(2)
        base.name_click('点击选择仓库')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'warehouse'))
        sleep(2)
        l = len(base.driver.find_elements_by_class_name('android.widget.RelativeLayout'))
        base.class_name_click_number('android.widget.RelativeLayout', int(int(l) - 1))
        base.driver.implicitly_wait(0)
        i=random.randint(0,10000)
        base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et','描述'+str(i))
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',material)
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()
        base.driver.implicitly_wait(0)
        base.id_click('com.facilityone.product.shang:id/ll_root')
        base.id_click('com.facilityone.product.shang:id/material_add_batch')
        base.name_sendkey('请输入供应商名称','供应商'+str(i))
        base.name_click('请选择过期时间')
        base.name_click('确定')
        due_date=base.id_text('com.facilityone.product.shang:id/et_select_due_date')
        base.id_sendkey('com.facilityone.product.shang:id/et_cost',str(i))
        base.id_sendkey('com.facilityone.product.shang:id/et_amount',2)
        base.name_click('保存')
        sleep(1)
        base.name_click('保存')
        base.id_click('com.facilityone.product.shang:id/inventory_save_btn')








