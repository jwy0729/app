from payment.Create import Create
from payment.Unpaid import Unpaid
from ReturnPage import Returnpage
from payment.Paid import Paid
from payment.Refunds import Refunds
from payment.PaymentQuery import PaymentQuery
from payment.RefundsQuery import RefundsQuery
class paymentMenu():
    Create=Create()
    Unpaid=Unpaid()
    Returnpage=Returnpage()
    Paid=Paid()
    Refunds=Refunds()
    PaymentQuery=PaymentQuery()
    RefundsQuery=RefundsQuery()
    def __init__(self):
        # 创建
        time=paymentMenu.Create.create()
        paymentMenu.Unpaid.unpaid(time)
        # 支付
        paymentMenu.Unpaid.pay()
        a=time.split('-')
        i=a[0]
        j=a[1]
        Y=i[-4:]
        M=j
        print(str(Y)+","+str(M))
        paymentMenu.Returnpage.returnpage()
        # 关闭
        paymentMenu.Paid.paid()
        paymentMenu.Paid.close()
        # 退款
        time2 =paymentMenu.Paid.paid()
        paymentMenu.Paid.refund()
        a1 = time2.split('-')
        i1 = a1[0]
        j1 = a[1]
        Y1 = i1[-4 :]
        M1 = j1
        paymentMenu.Returnpage.returnpage()
        # 退款单管理
        paymentMenu.Refunds.refunds()
        paymentMenu.Refunds.close()
        # 缴费单查询
        paymentMenu.PaymentQuery.query(Y,M)
        # 退款单查询
        paymentMenu.RefundsQuery.query(Y1,M1)
        # 创建
        time=paymentMenu.Create.create()
        # 作废
        paymentMenu.Unpaid.unpaid(time)
        paymentMenu.Unpaid.invalid()
        paymentMenu.Returnpage.returnpage()
