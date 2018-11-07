import random
import configparser
from time import sleep
class Reserve():
    def reserve(self,base,material):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'物资预定')
        except:
            try:
                base.name_click(u'库存')
                base.name_click(u'物资预定')
            except:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'物资预定')
        base.name_click('点击选择仓库')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'warehouse'))
        base.class_name_click_number('android.widget.RelativeLayout',1)
        base.driver.implicitly_wait(0)
        base.id_click('com.facilityone.product.shang:id/et_supervisor_add_store_name')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',cp.get('login','realname'))
        base.class_name_click_number('android.widget.RelativeLayout',1)
        base.driver.implicitly_wait(0)
        base.class_name_click('android.widget.LinearLayout')
        base.driver.implicitly_wait(300)
        base.id_click('com.facilityone.product.shang:id/et_materials_code')
        base.driver.implicitly_wait(0)
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', material)
        base.driver.implicitly_wait(0)
        base.class_name_click_number('android.widget.RelativeLayout',1)
        view=base.calss_name_size('android.widget.LinearLayout')
        y=int(view['height'])
        y1=y+y*0.3
        x=int(view['wigth'])
        print(x+','+y+','+y1)
        base.driver.swipe(x,y,x,y1)
        base.id_sendkey('com.facilityone.product.shang:id/et_materials_book_number',1)
        base.name_click('添加')
        base.name_click('预定')


