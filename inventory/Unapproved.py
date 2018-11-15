import random
import configparser
from time import sleep
from ReturnPage import Returnpage
class Unapproved():
    returnpage=Returnpage()
    i=random.randint(0,10000)
    def __init__(self):
        pass
    def unapproved(self,base,no):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'库存审核')
        except BaseException:
            try:
                base.name_click(u'库存')
                base.name_click(u'库存审核')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'库存审核')
        sleep(2)
        base.name_click(no)
        base.driver.implicitly_wait(300)
        base.name_click('审批')
    def Pass(self,base):
        base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et','通过'+str(Unapproved.i))
        base.name_click('通过')
        Unapproved.returnpage.returnpage(base)
    def Reject(self,base):
        base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et', '不通过' + str(Unapproved.i))
        base.name_click('不通过')
        Unapproved.returnpage.returnpage(base)

