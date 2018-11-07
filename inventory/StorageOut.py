import random
import configparser
from time import sleep
class StorageOut():
    i=random.randint(0,10000)
    def StorageOut(self,base):
        try:
            base.name_click(u'出库')
        except:
            try:
                base.name_click(u'库存')
                base.name_click(u'出库')
            except:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'出库')
        sleep(3)
    # 预定出库
    def reserved(self,base,no):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(no)
        except:
            for StorageOut.i in range(10000):
              n=1
              view = base.calss_name_size('android.widget.LinearLayout')
              y = int(view['height'])
              y1 = int(y + y * 0.3*n)
              x = int(view['wigth'])
              print(x + ',' + y + ',' + y1)
              base.driver.swipe(x, y, x, y1)
              try:
                  base.name_click(no)
                  break
              except:
                  n=n+1
        base.name_click('请选择领用人')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
        base.id_click_number('com.facilityone.product.shang:id/report_select_item_rl', 1)
        base.driver.implicitly_wait(0)
    def  delivery(self,base):
         base.name_click('出库')
    def refuse(self,base):
        base.name_click('取消出库')
    # 直接出库
    def direct(self,base,material):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        base.name_click('直接出库')
        base.driver.implicitly_wait(300)
        base.name_click('点击选择仓库')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'warehouse'))
        base.id_click_number('com.facilityone.product.shang:id/report_select_item_rl', 1)
        base.driver.implicitly_wait(0)
        base.driver.implicitly_wait(300)
        base.name_click('点击选择领用人')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
        base.id_click_number('com.facilityone.product.shang:id/report_select_item_rl', 1)
        base.driver.implicitly_wait(0)
        base.driver.implicitly_wait(300)
        base.name_click('点击选择主管')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
        base.id_click_number('com.facilityone.product.shang:id/report_select_item_rl', 1)
        base.driver.implicitly_wait(0)
        base.class_name_click('android.widget.LinearLayout')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', material)
        base.id_click_number('com.facilityone.product.shang:id/report_select_item_rl', 1)
        base.driver.implicitly_wait(0)
        view = base.calss_name_size('android.widget.LinearLayout')
        y = int(view['height'])
        y1 = int(y + y * 0.5 )
        x = int(view['wigth'])
        print(x + ',' + y + ',' + y1)
        base.driver.swipe(x, y, x, y1)
        base.id_click('com.facilityone.product.shang:id/ll_root')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', material)
        base.id_click_number('com.facilityone.product.shang:id/report_select_item_rl', 1)
        base.driver.implicitly_wait(0)
        base.id_click('com.facilityone.product.shang:id/material_inventory_count_tv')
        base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et',1)
        base.id_click('com.facilityone.product.shang:id/inventory_operate_btn')
        base.name_click('确定')
        base.name_click('出库')