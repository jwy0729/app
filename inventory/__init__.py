from inventory.Create import create
from inventory.Reserve import Reserve
from inventory.StorageIn import StorageIn
from inventory.MyReserved import MyReserved
from inventory.Unapproved import Unapproved
from inventory.StorageOut import StorageOut
from inventory.StorageMove import StorageMove
from inventory.StorageCheck import StorageCheck
from ReturnPage import Returnpage

class InventoryMenu():
    # create1 = create()
    # IN = StorageIn()
    # Reserve = Reserve()
    # MyReserved = MyReserved()
    # Unapproved = Unapproved()
    # StorageOut = StorageOut()
    StorageMove = StorageMove()
    StorageCheck = StorageCheck()
    Returnpage=Returnpage()
    def __init__(self):
        # 创建物资
        material = InventoryMenu.create1.create()
        # 入库
        InventoryMenu.IN.storageIn( material)
        # 物资预定
        InventoryMenu.Reserve.reserve(material)
        # 我的预定
        materialNo = InventoryMenu.MyReserved.MyReserved()
        # 物资审核(通过)
        InventoryMenu.Unapproved.unapproved(materialNo)
        InventoryMenu.Unapproved.Pass()
        # 预定出库
        InventoryMenu.StorageOut.StorageOut()
        InventoryMenu.StorageOut.reserved(materialNo)
        InventoryMenu.StorageOut.delivery()
        # 直接出库
        InventoryMenu.StorageOut.StorageOut()
        InventoryMenu.StorageOut.direct(material)
        # 移库
        InventoryMenu.StorageMove.StorageMove(material)
        # 盘点
        InventoryMenu.StorageCheck.StorageCheck(material)
        InventoryMenu.Returnpage.returnpage()
        # 物资预定
        InventoryMenu.Reserve.reserve(material)
        # 预定取消
        InventoryMenu.MyReserved.cancellation()