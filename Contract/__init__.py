from Contract.Management import Management
from ReturnPage import Returnpage
import configparser
from base import base
from time import sleep
from Contract.History import History
class ContractMenu():
    management=Management()
    Returnpage = Returnpage()
    history=History()
    def __init__(self):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        ContractMenu.management.management()
        ContractMenu.management.activity(cp.get('contract', 'expired1'))
        # 验证不通过
        base.driver.implicitly_wait(10)
        ContractMenu.management.acceptReject()
        base.driver.implicitly_wait(0)
        sleep(2)
        ContractMenu.management.management()
        ContractMenu.management.activity(cp.get('contract', 'NotStart'))
        # 终止
        base.driver.implicitly_wait(10)
        ContractMenu.management.terminate()
        base.driver.implicitly_wait(0)
        sleep(2)
        ContractMenu.management.management()
        ContractMenu.management.activity(cp.get('contract', 'NotStart'))
        # 恢复
        base.driver.implicitly_wait(10)
        ContractMenu.management.recovery()
        base.driver.implicitly_wait(0)
        sleep(2)
        ContractMenu.management.management()
        ContractMenu.management.activity(cp.get('contract', 'NotStart'))
        # 终止
        base.driver.implicitly_wait(10)
        ContractMenu.management.terminate()
        base.driver.implicitly_wait(0)
        sleep(2)
        ContractMenu.management.management()
        ContractMenu.management.activity(cp.get('contract', 'NotStart'))
        # 存档
        base.driver.implicitly_wait(10)
        ContractMenu.management.archive()
        base.driver.implicitly_wait(0)
        sleep(2)
        ContractMenu.management.management()
        ContractMenu.management.activity(cp.get('contract', 'executing'))
        # 终止
        base.driver.implicitly_wait(10)
        ContractMenu.management.terminate()
        base.driver.implicitly_wait(0)
        sleep(2)
        ContractMenu.management.management()
        ContractMenu.management.activity(cp.get('contract', 'expired2'))
        # 验证通过
        base.driver.implicitly_wait(10)
        ContractMenu.management.acceptPass()
        base.driver.implicitly_wait(0)
        # 合同查询
        ContractMenu.history.history(cp.get('contract', 'expired2'))
        ContractMenu.Returnpage.returnpage()

