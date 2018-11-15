from time import sleep
class history():
    def __init__(self):
        pass
    def history(self,base,no):
        try:
            base.name_click(u'需求查询')
        except BaseException:
            try:
                base.name_click(u'服务台')
                base.name_click(u'需求查询')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'服务台')
                base.name_click(u'需求查询')
        sleep(2)
        base.name_click(no)
        # 信息未验证
        base.id_click('com.facilityone.product.shang:id/actionbar_back_ll')
        sleep(1)
        base.id_click('com.facilityone.product.shang:id/actionbar_back_ll')

