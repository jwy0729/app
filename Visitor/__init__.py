from Visitor.Create import Create
from ReturnPage import Returnpage
from base import Base
from Visitor.Query import Query

class CreateMenu():
    Create=Create()
    Query = Query()
    Returnpage = Returnpage()
    def __init__(self):
        time = CreateMenu.Create.create()
        CreateMenu.Query.query(time)
        CreateMenu.Returnpage.returnpage()
