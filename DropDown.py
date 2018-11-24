from base import base


class DropDown():
    def dropDown(self):
        try:
            view=base.driver.find_element_by_id('com.facilityone.product.shang:id/patrol_task_query_dianwei_detail_sv').size
        except BaseException:
            try:
                view = base.driver.find_element_by_id('android:id/content').size
            except BaseException:
                try:
                    view = base.driver.find_element_by_id(
                        'com.facilityone.product.shang:id/patrol_task_query_menu_fliter_sv').size
                except BaseException:
                    try:
                        view = base.driver.find_element_by_id('android:id/list').size
                    except BaseException:
                        try:
                            view = base.driver.find_element_by_id('com.facilityone.product.shang:id/sv_root').size
                        except BaseException:
                            try:
                                view = base.driver.find_element_by_id('com.facilityone.product.shang:id/ms_view').size
                            except BaseException:
                                view = base.driver.find_element_by_id('com.facilityone.product.shang:id/root').size
        y = int(view['height'] * 0.75)
        y1 = int(view['height'] * 0.25)
        x = int(view['width'] * 0.5)
        return base.driver.swipe(x, y, x, y1,1000)
