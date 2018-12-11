from Energy.Energy import Energy
from ReturnPage import Returnpage

class EnergyMenu():
    energy = Energy()
    Returnpage = Returnpage()
    def __init__(self):
        try:
            EnergyMenu.energy.energy()
            EnergyMenu.energy.content()
            EnergyMenu.energy.change()
            EnergyMenu.Returnpage.returnpage()
        except BaseException:
            return 0

