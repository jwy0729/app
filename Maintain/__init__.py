from Maintain.maintain import Maintain
from ReturnPage import Returnpage
import datetime
from base import base
class MaintainMenu():
    maintain=Maintain()
    Returnpage = Returnpage()
    def __init__(self):
        try:
            MaintainMenu.maintain.maintain()
        except BaseException:
            for i in range(10):
                try:
                    name = base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    time=datetime.datetime.now().strftime("Y%.m%")
                    if name ==time:
                        break
                    else:
                        MaintainMenu.Returnpage.returnpage()
                except BaseException:
                    MaintainMenu.Returnpage.returnpage()
        MaintainMenu.Returnpage.returnpage()
