import random
import configparser
from time import sleep
class create():
    def create(self,base):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'新建物资')
        except:
            try:
                base.name_click(u'库存')
                base.name_click(u'新建物资')
            except:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'新建物资')
        base.name_click('点击选择仓库')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',cp.get('invebtory','warehouse'))
        sleep(2)
        base.class_name_click_number('android.widget.RelativeLayout',1)

        
        base.driver.implicitly_wait(0)
        i=random.randint(0,10000)
        base.id_sendkey('com.facilityone.product.shang:id/et_shelves','货架信息'+str(i))
        base.id_sendkey('com.facilityone.product.shang:id/material_info_name','物资'+str(i))
        base.id_sendkey('com.facilityone.product.shang:id/material_info_code','bm'+str(i))
        base.id_sendkey('com.facilityone.product.shang:id/material_info_unit','kg'+str(i))
        base.id_sendkey('com.facilityone.product.shang:id/material_info_brand','品牌'+str(i))
        base.id_sendkey('com.facilityone.product.shang:id/material_info_model','NHG'+str(i))
        base.id_sendkey('com.facilityone.product.shang:id/material_info_ratified_price',str(i))
        base.id_sendkey('com.facilityone.product.shang:id/material_info_minimum_stock',21)
        base.id_sendkey('com.facilityone.product.shang:id/material_info_initial_number',10)
        base.name_sendkey('请输入或选择供应商','供应商'+str(i))
        base.id_sendkey('com.facilityone.product.shang:id/et_cost',22)
        base.id_click('com.facilityone.product.shang:id/et_select_due_date')
        base.name_click('确定')
        due_date=base.id_text('com.facilityone.product.shang:id/et_select_due_date')
        base.name_click("保存")
        return '物资'+str(i)










