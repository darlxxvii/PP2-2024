"""Create a bank account class that has attributes owner, balance and two methods deposit and 
withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several 
deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    pass"""
class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance 
    def deposit(self):
        d=float(input("How much you want to deposit? "))
        self.balance=self.balance+d
        print("Accepted! Your balance is: ", self.balance)
    def withdraw(self):
        w=float(input("How much you want to withdraw? "))
        if w<=self.balance:
            self.balance=self.balance-w
            print("Your withdraw is accepted! Your balance now is : ", self.balance)
        else:
            print("Not enough balance.")
owner=input("Owner's name: ")
balance=float(input("Enter balance: "))
p1=Account(owner, balance)
p1.deposit()
p1.withdraw()
