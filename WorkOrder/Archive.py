from time import sleep
import configparser
import random
class archive():
    def archive(self,base,no):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'待存档工单')
        except:
            try:
                base.name_click(u'工单')
                base.name_click(u'待存档工单')
            except:
                base.name_click(u'工作')
                base.name_click(u'工单')
                base.name_click(u'待存档工单')
        sleep(2)
        base.name_click(no)
    def verifyT(self,base):
        i = random.randint(0, 1000)
        base.driver.implicitly_wait(300)
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.driver.implicitly_wait(0)
        base.name_click('验证')
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et','验证通过'+str(i))
        base.name_click('通过')

    def verifyF(self, base):
        i = random.randint(0, 1000)
        base.driver.implicitly_wait(300)
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.driver.implicitly_wait(0)
        base.name_click('验证')
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '验证不通过' +str(i))
        base.name_click('拒绝')
    def Archive(self,base):
        base.driver.implicitly_wait(300)
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.driver.implicitly_wait(0)
        base.name_click('存档')
