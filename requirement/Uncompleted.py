from appium import webdriver
from time import sleep
import random
import configparser

class uncompleted():
    def __init__(self):
        pass
    def uncompleted(self,base,inf):
        try:
            base.name_click(u'待处理需求')
        except BaseException:
            try:
                base.name_click(u'服务台')
                base.name_click(u'待处理需求')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'服务台')
                base.name_click(u'待处理需求')
        sleep(2)
        base.name_click(inf)
        sleep(1)
#        数据信息没验证
        no=base.id_text('com.facilityone.product.shang:id/service_demand_item_id_describe_tv')
        # print(no)
        return no
    def wo(self,base):
        # 创建工单
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        sleep(2)
        base.name_click(u'生成工单')
        # 信息未验证
        base.id_click('com.facilityone.product.shang:id/report_service_type_ll')
        base.class_name_sendkey('android.widget.EditText',cp.get('word','type'))
        base.class_name_click_number('android.widget.RelativeLayout', 1)
        try:
            base.name_click(u'确定')
            print(12)
        except BaseException:
            print('无子集')
        base.id_click('com.facilityone.product.shang:id/report_priority_ll')
        base.class_name_click_number('android.widget.RelativeLayout',1)
        view=base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout').size
        h=int(view['height'])
        w=int(view['width'])
        h1=int(h*0.4)+h
        print(h1,h,w)
        sleep(3)
        # 下面下拉有问题
        # base.driver.swipe(w,h,w,h1,10000)
        sleep(2)
        # 没写图片上传
        base.class_name_click('android.widget.TextView')
        base.id_click('com.facilityone.product.shang:id/actionbar_back_ll')
        sleep(1)
        base.id_click('com.facilityone.product.shang:id/actionbar_back_ll')
    def save(self,base):
        i = random.randint(0, 1000)
        base.id_click('com.facilityone.product.shang:id/service_demand_item_handle_content_add_iv')
        base.name_sendkey('请输入处理內容','测试工作内容'+i)
        base.name_click(u'保存')
        base.id_click('com.facilityone.product.shang:id/actionbar_back_ll')
    def complete(self,base):
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.name_click(u'完成')
        detail=base.id_text('com.facilityone.product.shang:id/actionbar_title_tv')
        if detail=="需求详情":
            print('该需求存在工单未完成')
        else:
            print('需求已完成')
        base.id_click('com.facilityone.product.shang:id/actionbar_back_ll')