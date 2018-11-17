from Energy.Energy import Energy
from base import Base
from ReturnPage import Returnpage

class EnergyMenu():
    Energy = Energy()
    Energy.energy(Base)
    Energy.content(Base)
    Energy.change(Base)
    Returnpage = Returnpage()
    Returnpage.returnpage(Base)
