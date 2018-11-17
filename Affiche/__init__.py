from Affiche.Affiche import Affiche
from ReturnPage import Returnpage
from base import Base
class AfficheMenu():
    affiche=Affiche()
    title=affiche.Unread(Base)
    affiche.Read(Base,title)
    Returnpage=Returnpage()
    Returnpage.returnpage(Base)

