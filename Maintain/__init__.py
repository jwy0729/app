from Maintain.maintain import Maintain
from ReturnPage import Returnpage
class MaintainMenu():
    maintain=Maintain()
    Returnpage = Returnpage()
    def __init__(self):
        try:
            MaintainMenu.maintain.maintain()
            MaintainMenu.Returnpage.returnpage()
        except BaseException:
            return 0