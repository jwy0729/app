from time import sleep
import configparser
import random

class unapproved():
    def unapproved(self,base,no):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'待审批工单')
        except:
            try:
                base.name_click(u'工单')
                base.name_click(u'待审批工单')
            except:
                base.name_click(u'工作')
                base.name_click(u'工单')
                base.name_click(u'待审批工单')
        sleep(2)
        base.name_click(no)
    def refuse(self,base):
        sleep(3)
        i = random.randint(0, 1000)
        try:
            base.name_click('审批')
        except:
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('审批')
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et','审批拒绝原因'+str(i))
        base.name_click('拒绝')
    def Pass(self,base):
        sleep(3)
        i = random.randint(0, 1000)
        try:
            base.name_click('审批')
        except:
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('审批')
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '审批通过原因' +str(i))
        base.name_click('通过')