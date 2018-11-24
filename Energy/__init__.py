from Energy.Energy import Energy
from base import Base
from ReturnPage import Returnpage

class EnergyMenu():
    energy = Energy()
    Returnpage = Returnpage()
    def __init__(self):
        EnergyMenu.energy.energy()
        EnergyMenu.energy.content()
        EnergyMenu.energy.change()
        EnergyMenu.Returnpage.returnpage()

