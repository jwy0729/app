from Maintain.maintain import maintain
from ReturnPage import Returnpage
class Maintain():
    maintain=maintain()
    Returnpage = Returnpage()
    def __init__(self):
        Maintain.maintain.Asset()
        Maintain.Returnpage.returnpage()