from inspection.Inspection import Inspection
from inspection.Validation import Validation
from inspection.History import History
from ReturnPage import Returnpage
from base import Base

class InspectionMenu():
    Inspection=Inspection()
    Validation=Validation()
    History=History()
    Returnpage=Returnpage()
    def __init__(self):
        InspectionMenu.Inspection.inspection()
        InspectionMenu.Validation.validation()
        InspectionMenu.History.history()
        InspectionMenu.Returnpage.returnpage()
