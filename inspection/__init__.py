from inspection.Inspection import Inspection
from inspection.Validation import Validation
from inspection.History import History
from ReturnPage import Returnpage

class InspectionMenu():
    Inspection=Inspection()
    Validation=Validation()
    History=History()
    Returnpage=Returnpage()
    def __init__(self):
        try:
            InspectionMenu.Inspection.inspection()
            time=InspectionMenu.Validation.validation()
            Y=time[0,4]
            M=time[5:7]
            InspectionMenu.Returnpage.returnpage()
            InspectionMenu.History.history(Y,M)
            InspectionMenu.Returnpage.returnpage()
        except BaseException:
            return 0
