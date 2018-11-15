from DropDown import DropDown
import random
import configparser
from time import sleep
class StorageCheck():
    DropDown = DropDown()
    def __init__(self):
        pass
    def StorageCheck(self,base,material):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'盘点')
        except BaseException:
            try:
                base.name_click(u'库存')
                base.name_click(u'盘点')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'盘点')
        base.name_click('点击选择仓库')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'warehouse'))
        sleep(2)
        l=len(base.driver.find_elements_by_class_name('android.widget.RelativeLayout'))
        base.class_name_click_number('android.widget.RelativeLayout',int(int(l)-1))
        base.driver.implicitly_wait(0)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',material)
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout').click()
        base.driver.implicitly_wait(0)
        base.id_click('com.facilityone.product.shang:id/ll_root')
        sleep(2)
        StorageCheck.DropDown.dropDown(base)
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout').click()
        sleep(2)
        base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et', 1)
        base.id_click('com.facilityone.product.shang:id/inventory_operate_btn')
        base.name_click('确定')
        sleep(1)
        base.name_click('盘点')