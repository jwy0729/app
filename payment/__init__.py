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
        time1=paymentMenu.Unpaid.pay()
        a=time1.split('-')
        i=a[0]
        j=a[1]
        Y=i[-4:]
        M=j
        paymentMenu.Returnpage.returnpage()
        # 关闭
        time2=paymentMenu.Paid.paid()
        a1 = time2.split('-')
        i1 = a[0]
        j1 = a[1]
        Y1 = i[-4:]
        M1 = j
        paymentMenu.Paid.close()
        # 退款
        paymentMenu.Paid.paid()
        paymentMenu.Paid.refund()
        paymentMenu.Returnpage.returnpage()
        # 退款单管理
        paymentMenu.Refunds.refunds()
        paymentMenu.Returnpage.returnpage()
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
