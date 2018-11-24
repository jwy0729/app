from base import base


class Returnpage():
    def returnpage(self):
        try:
            base.id_click('com.facilityone.product.shang:id/actionbar_back_ll')
        except BaseException:
            base.id_click('com.facilityone.product.shang:id/actionbar_back_fullscreen_ll')