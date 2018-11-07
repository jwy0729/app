import random
import configparser
from time import sleep
class StorageIn():
    def storageIn(self,base,material):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'入库')
        except:
            try:
                base.name_click(u'库存')
                base.name_click(u'入库')
            except:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'入库')
        sleep(2)
        base.name_click('点击选择仓库')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',cp.get('invebtory','warehouse'))
        base.id_click_number('com.facilityone.product.shang:id/report_select_item_rl',1)
        base.driver.implicitly_wait(0)
        i=random.randint(0,10000)
        base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et','描述'+i)
        base.id_click('android.widget.LinearLayout')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',material)
        base.driver.implicitly_wait(0)
        base.class_name_click_number('android.widget.RelativeLayout',1)
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
        base.name_click('入库')








