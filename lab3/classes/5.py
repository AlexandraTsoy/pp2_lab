class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposite(self,dep):
        self.balance = self.balance + dep
        print(str(self.owner) + " has:" )
        print(str(self.balance))
    def withdraw(self, w):
        if self.balance >= w:
            self.balance -= w
            print("Balance:")
            print(self.balance)
        else:
            print("Impossible")

name = input()
c = int(input())
d = int(input())
a = Account(name,0)
a.deposite(c)
a.withdraw(d)