from time import sleep
import configparser

from base import base


class history():
    def __init__(self):
        pass
    def history(self,no):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'待存档工单')
        except BaseException:
            try:
                base.name_click(u'工单')
                base.name_click(u'工单查询')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'工单')
                base.name_click(u'工单查询')
        sleep(2)
        base.id_sendkey('com.facilityone.product.shang:id/work_order_code',no)
        base.name_click('确定')
        base.id_click('com.facilityone.product.shang:id/work_order_query_rl')

