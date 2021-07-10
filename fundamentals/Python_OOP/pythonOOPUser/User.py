
class User:
    def __init__(self, name, account):
        self.name = name
        #self.account_balance = balance
        self.bank_account = account
        
    def make_withdrawal(self,amount):
        self.bank_account.account_balance -= amount
        return self
    
    def make_deposit(self, deposit):
        self.bank_account.account_balance += deposit
        return self
        
    def display_user_balance(self):
        return print(self.name, self.bank_account.account_balance)
        
    def transfer_money(self, other_user, amount):
        self.bank_account.account_balance -= amount
        other_user.bank_account.account_balance += amount
        return self
    def testingme(self):
        self.bank_account.deposit(100)
        


class BankAccount:
    def __init__(self, balance = 0):
        self.account_balance = balance
        self.intRate = 0.01
    
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self,amount):
        if self.account_balance > 0:
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    def display_account_info(self):
        print(self.account_balance)
        return self
    def yeild_interest(self):
        if account_balance > 0 :
            account_balance += account_balance * self.intRate
        return self




account1 = BankAccount()
account2 = BankAccount()
#account1.deposit(110).deposit(88).deposit(50).display_account_info().withdraw(50).display_account_info()
#account2.deposit(110).deposit(88).display_account_info().withdraw(50).withdraw(30).withdraw(75).withdraw(63).display_account_info()

instance11 = User('samer', account2)
instance11.make_deposit(700)
instance11.display_user_balance()






'''
instance1 = User('osaid', 300)
instance2 = User('mhamad', 500)
instance3 = User('samer', 800)


instance1.make_deposit(500).make_deposit(30).make_deposit(100).make_withdrawal(200)
instance3.make_deposit(150).make_withdrawal(90).make_withdrawal(20).make_withdrawal(75)
instance1.display_user_balance()
instance3.display_user_balance()
instance1.transfer_money(instance2, 260)
instance2.display_user_balance()
'''
