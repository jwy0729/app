import random
import configparser
from time import sleep
from ReturnPage import returnpage
class MyReserved():
    returnpage=returnpage()
    def MyReserved(self,base):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'我的预定')
        except:
            try:
                base.name_click(u'库存')
                base.name_click(u'我的预定')
            except:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'我的预定')
        base.driver.implicitly_wait(300)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()
        base.driver.implicitly_wait(0)
        base.driver.implicitly_wait(300)
        no=base.id_text('com.facilityone.product.shang:id/tv_reservation_code')
        base.driver.implicitly_wait(0)
        MyReserved.returnpage.returnpage(base)
        MyReserved.returnpage.returnpage(base)
        return no
    def cancellation(self,base):
        i=random.randint(0,10000)
        base.name_click('取消预定')
        base.name_sendkey('请输入原因','取消预定'+str(i))
        base.name_click('确定')
        MyReserved.returnpage.returnpage(base)
