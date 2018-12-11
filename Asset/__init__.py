from Asset.Asset import Asset
from ReturnPage import Returnpage
from base import base
from WipeUp import WipeUp
class AssetMenu():
    Asset = Asset()
    Returnpage = Returnpage()
    WipeUp=WipeUp()
    def __init__(self):
        try:
            AssetMenu.Asset.asset()
            AssetMenu.Asset.rissue()
            AssetMenu.Returnpage.returnpage()
            AssetMenu.WipeUp.wipeUp()
            AssetMenu.Returnpage.returnpage()
        except BaseException:
            return 0


