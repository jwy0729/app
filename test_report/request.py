import unittest

class MyTestCase(unittest.TestSuite):
    def requirement(self,n,m):
        self.addTests(n,1,m)
    def affiche(self,n):
        self.addTests(n,1,"testError")
    def asset(self,n):
        self.addTests(n,1,"testError")
    def contract(self,n):
        self.addTests(n,1,"testError")
    def energy(self,n):
        self.addTests(n,1,"testError")
    def inspection(self,n):
        self.addTests(n,1,"testError")
    def inventory(self,n):
        self.addTests(n,1,"testError")
    def knowledge(self,n):
        self.addTests(n,1,"testError")
    def maintain(self,n):
        self.addTests(n,1,"testError")
    def patrol(self,n):
        self.addTests(n,1,"testError")
    def vistor(self,n):
        self.addTests(n,1,"testError")
    def workorder(self,n):
        self.addTests(n,1,"testError")