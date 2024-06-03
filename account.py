class Account:
    def __init__(self,number,pin,owner=None):
        self.number=number
        self.__pin=pin
        self.__balance=0
        self.owner = owner
        self.overdraft_limit = None
        self.minimum_balance = None
        self.is_frozen = False
        self.transactions = []
    def show_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
    def deposit(self,amount,pin):
        if pin==self.__pin:
            self.__balance+=amount
            self.transactions.append(f"Deposit: {amount}")
            return f"ksh {amount} was deposited successfully.Current balance is ksh {self.__balance}"
        else:
            return f"Please enter the correct pin"
    def withdraw(self,amount,pin):
        if pin==self.__pin:
            if self.__balance <= 1400:
                return f"The balance  is so small to be withdrawn.The limit is 1400"
            else:
                self.__balance-=amount
                self.transactions.append(f"Withdrawal: {amount}")
                return f"You have succefully withdrawn {amount} new balance is {self.__balance}"
        else:
            return f"Input the correct pin"
    def view_account_details(self, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        return {
            "Owner": self.owner,
            "Balance": self.__balance,
            "Overdraft Limit": self.overdraft_limit,
            "Minimum Balance": self.minimum_balance,
            "Frozen Status": self.is_frozen,
            "Transactions": self.transactions
        }
    def change_owner(self, new_owner, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        self.owner = new_owner
        return f"Account owner changed to {new_owner}"
    def account_statement(self, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        return "\n".join(self.transactions)
    def set_overdraft_limit(self, limit, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        self.overdraft_limit = limit
        return f"Overdraft limit set to {limit}"
    def interest_calculation(self, rate, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        interest = self.__balance * rate / 100
        self.__balance += interest
        self.transactions.append(f"Interest added: {interest}")
        return f"Interest calculated and applied. New balance: {self.__balance}"
    def freeze_account(self, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        self.is_frozen = True
        return "Account frozen"
    def unfreeze_account(self, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        self.is_frozen = False
        return "Account unfrozen"
    def transaction_history(self, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        return self.transactions
    def set_minimum_balance(self, min_balance, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        self.minimum_balance = min_balance
        return f"Minimum balance set to {min_balance}"
    def transfer_funds(self, recipient_number, amount, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        if self.is_frozen:
            return "Account is frozen"
        if amount > self.__balance + (self.overdraft_limit if self.overdraft_limit else 0):
            return "Insufficient funds"
        return f"Funds transferred successfully. New balance: {self.__balance - amount}"
    def close_account(self, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        return "Account closed"     
        
