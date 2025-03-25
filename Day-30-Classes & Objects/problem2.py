class account():
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
        
    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            print(f"Deposited {amount} Remaining Balance {self.balance}")
        else:
            print("Deposit amount should be positive")
        
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print("Invalid transaction.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            
    def get_balance(self):
        return self.balance
    
acc1 = account("12345678", 1000)
acc1.deposit(500)
acc1.withdraw(300)
print(f"Final Balance: {acc1.get_balance()}")


        