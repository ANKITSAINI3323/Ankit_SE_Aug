
class BankDemo:
    balance = 0
    
    def checkBalance(self):
        print("Current Balance : ",self.balance)

    def deposit(self,amt):
        self.balance = self.balance + amt
        print("Amount Deposited Successful.")

    def withdraw(self,amt1):
        if amt1<self.balance:
            self.balance = self.balance - amt1
            print("Withdrawal is Successful")
        else:
            print("Insufficient Fund")


p=BankDemo()
p.checkBalance()
amt = int(input("Enter Amount to Deposit : "))
p.deposit(amt)
p.checkBalance()
amt1 = int(input("Enter Amount to Withdraw : "))
p.withdraw(amt1)
p.checkBalance()







