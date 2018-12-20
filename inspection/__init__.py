from inspection.Inspection import Inspection
from inspection.Validation import Validation
from inspection.History import IHistory
from ReturnPage import Returnpage
from base import base
class InspectionMenu():
    Inspection=Inspection()
    Validation=Validation()
    History=IHistory()
    Returnpage=Returnpage()
    def __init__(self):
        try:
            InspectionMenu.Inspection.inspection()
        except BaseException:
            for i in range(10):
                try:
                    # 需要更改
                    base.id_text('com.facilityone.product.shang:id/conttact_bar_chart')
                    break
                except BaseException:
                    InspectionMenu.Returnpage.returnpage()
        try:
            time = InspectionMenu.Validation.validation()
            Y = time[0, 4]
            M = time[5:7]
            InspectionMenu.Returnpage.returnpage()
        except BaseException:
            for i in range(10):
                try:
                    # 需要更改
                    base.id_text('com.facilityone.product.shang:id/conttact_bar_chart')
                    break
                except BaseException:
                    InspectionMenu.Returnpage.returnpage()
        try:
           InspectionMenu.History.history(Y, M)
        except BaseException:
            for i in range(10):
                try:
                    # 需要更改
                    base.id_text('com.facilityone.product.shang:id/conttact_bar_chart')
                    break
                except BaseException:
                    InspectionMenu.Returnpage.returnpage()
        InspectionMenu.Returnpage.returnpage()
