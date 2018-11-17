from Visitor.Create import Create
from ReturnPage import Returnpage
from base import Base

class CreateMenu():
    Create=Create()
    time=Create.create(Base)
    Create.query(Base,time)
    Returnpage=Returnpage()
    Returnpage.returnpage(Base)