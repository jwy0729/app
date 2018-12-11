from Asset.Asset import Asset
from ReturnPage import Returnpage
from time import sleep
from patrol.InspectionTask import InspectionTask
from patrol.InspectionHistory import InspectionHistory
class InspectionMenu():
    InspectionTask = InspectionTask()
    InspectionHistory=InspectionHistory()
    Returnpage = Returnpage()
    def __init__(self):
        # 巡检任务
        InspectionMenu.InspectionTask.inspectionTask()
        sleep(3)
        # 巡检查询
        InspectionMenu.InspectionHistory.inspectionHistory()
#       巡检报修
        InspectionMenu.InspectionHistory.Inspection()



