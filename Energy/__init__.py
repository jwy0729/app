from Energy.Energy import Energy
from ReturnPage import Returnpage
from base import base
class EnergyMenu():
    energy = Energy()
    Returnpage = Returnpage()
    def __init__(self):
        try:
            EnergyMenu.energy.energy()
            EnergyMenu.energy.content()
            EnergyMenu.energy.change()
        except BaseException:
            for i in range(10):
                try:
                    name = base.id_text('com.facilityone.product.shang:id/work_list_item_name_iv')
                    if name == '能源管理':
                        break
                    else:
                        EnergyMenu.Returnpage.returnpage()
                except BaseException:
                    EnergyMenu.Returnpage.returnpage()


