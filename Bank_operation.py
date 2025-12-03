class bank_account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,deposit):
        self.deposit=deposit
        c=self.balance+self.deposit
        print(c)
    def withdraw(self,withdraw):
        self.withdraw=withdraw
        if self.balance<self.withdraw:
            print("insufficient balance")
        else:
            c=self.balance+self.withdraw
            print(c)
    def show_balance(self):
        print(c)  
c=float(input("Enter balance"))  
d=float(input("Enter deposit: "))
e=float(input("Enter withdrwal: "))
n=input("name")
a=bank_account(n,c)
a.deposit(d)
a.withdraw(e)
a.show_balance()