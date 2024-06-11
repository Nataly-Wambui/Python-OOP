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

    def display_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "You have entered the wrong pin"
        
    def deposit_funds(self,amount,pin):
        if pin==self.__pin:
            self.__balance+=amount
            return self.__balance
        else:
            return "You have entered the wrong pin"
        
    def withdraw_funds(self,amount,pin):
        if pin==self.__pin:
            if self.__balance < self.overdraft_limit:
                return f"The balance is below {self.overdraft_limit}"
            else:
                self.__balance-=amount
                return self.__balance
        else:
            return "You have entered the wrong pin"
        
    def view_account_details(self, pin):
        if pin== self.__pin:
            return {
            "Owner": self.owner,
            "Balance": self.__balance,
            "Overdraft Limit": self.overdraft_limit,
            "Minimum Balance": self.minimum_balance,
            "Frozen Status": self.is_frozen,
            "Transactions": self.transactions
        }
        else:
            return "You have entered the wrong pin"
        
    def change_account_owner(self, new_owner, pin):
        if pin== self.__pin:
            self.owner = new_owner
            return self.owner
        else:
            return "You have entered the wrong pin"
        
    def display_account_statement(self, pin):
        if pin!= self.__pin:
            return "Wrong PIN"
        return "\n".join(self.transactions)
    
    def set_overdraft_limit(self, limit, pin):
        if pin== self.__pin:
            self.overdraft_limit = limit
            return self.overdraft_limit
        else:
            return "You have entered the wrong pin"
    
    def calculate_interest_rate(self, rate, pin):
        if pin== self.__pin:
            interest = self.__balance * rate / 100
            self.__balance += interest
            return self.__balance
        else:
            return "You have entered the wrong pin"
    
    def freeze_account(self, pin):
        if pin== self.__pin:
            self.is_frozen = True
            return "Account has been frozen"
        else:
            return "You have entered the wrong pin"
    
    
    def unfreeze_account(self, pin):
        if pin== self.__pin:
            self.is_frozen = False
            return "Account has been unfrozen"
        else:
            return "You have entered the wrong pin"
    
    def transaction_history(self, pin):
        if pin== self.__pin:
            return self.transactions
        else:
            return "You have entered the wrong pin"
    
    def set_minimum_balance(self, min_balance, pin):
        if pin== self.__pin:
            self.minimum_balance = min_balance
            return self.minimum_balance
        else:
            return "You have entered the wrong pin"
    
    
    def transfer_funds(self, recipient_number, amount, pin):
        if pin!= self.__pin:
            return "You have entered the wrong pin"
        else:
            if amount > self.__balance and amount > self.overdraft_limit:
                self.__balance -= amount
                return f"You have successfully transferred {amount} to {recipient_number}. New balance: {self.__balance}"
            else:
                return f"{amount} is below the set limit"
    
    
    def close_account(self, pin):
        if pin== self.__pin:
            return "Account closed"
        else:
            return "You have entered the wrong pin"     
        
