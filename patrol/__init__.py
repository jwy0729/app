from Asset.Asset import Asset
from ReturnPage import Returnpage
from time import sleep
from patrol.InspectionTask import InspectionTask
from patrol.InspectionHistory import InspectionHistory
from base import base
class InspectionMenu():
    InspectionTask = InspectionTask()
    InspectionHistory=InspectionHistory()
    Returnpage = Returnpage()
    def __init__(self):
        # 巡检任务
        try:
            InspectionMenu.InspectionTask.inspectionTask()
        except BaseException:
            for i in range(10):
                try:
                    name = base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name == '巡检':
                        break
                    else:
                        base.driver.implicitly_wait(1000)
                        InspectionMenu.Returnpage.returnpage()
                        base.driver.implicitly_wait(0)
                except BaseException:
                    base.driver.implicitly_wait(100)
                    InspectionMenu.Returnpage.returnpage()
                    base.driver.implicitly_wait(0)
            sleep(3)
            #       巡检报修
        try:
            InspectionMenu.InspectionHistory.InspectionHistorey()
        except BaseException:
            for i in range(10):
                try:
                    name = base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name == '巡检':
                        break
                    else:
                        base.driver.implicitly_wait(1000)
                        InspectionMenu.Returnpage.returnpage()
                        base.driver.implicitly_wait(0)
                except BaseException:
                    base.driver.implicitly_wait(1000)
                    InspectionMenu.Returnpage.returnpage()
                    base.driver.implicitly_wait(0)
        InspectionMenu.Returnpage.returnpage()





