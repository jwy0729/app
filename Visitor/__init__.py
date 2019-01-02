from Visitor.Create import VCreate
from ReturnPage import Returnpage
from Visitor.Query import Query

class VisitorMenu():
    Create=VCreate()
    Query = Query()
    Returnpage = Returnpage()
    def __init__(self):
        try:
            time = VisitorMenu.Create.create()
            VisitorMenu.Returnpage.returnpage()
            VisitorMenu.Query.query(time)
            VisitorMenu.Returnpage.returnpage()
        except BaseException:
            return 0
