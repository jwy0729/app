from Asset.Asset import Asset
from ReturnPage import Returnpage
from base import base

class AssetMenu():
    Asset = Asset()
    Returnpage = Returnpage()
    def __init__(self):
        AssetMenu.Asset.asset()
        AssetMenu.Asset.rissue()
        AssetMenu.Returnpage.returnpage()


