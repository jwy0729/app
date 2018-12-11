from Visitor.Create import Create
from ReturnPage import Returnpage
from Visitor.Query import Query

class VisitorMenu():
    Create=Create()
    Query = Query()
    Returnpage = Returnpage()
    def __init__(self):
        time = VisitorMenu.Create.create()
        VisitorMenu.Returnpage.returnpage()
        VisitorMenu.Query.query(time)
        VisitorMenu.Returnpage.returnpage()
