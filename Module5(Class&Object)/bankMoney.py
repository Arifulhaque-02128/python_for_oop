class Bank :
    user = 'Arif'

    def __init__(self, initial_amount) -> None:
        self.balance = initial_amount
        self.max_withdraw = 1000000
        self.min_withdraw = 100

    def deposit(self, amount) : 
        if(amount > 0) :
            self.balance += amount
    
    def withdraw(self, amount) :
        if(self.balance > amount) :
            if(amount < self.min_withdraw or amount > self.max_withdraw) :
                return f'You cant withdraw amount less than {self.min_withdraw} and more than {self.max_withdraw}'
            else :
                self.balance -= amount
                return f'You have withdrawn {amount} TK. Your current balance is {self.balance}'
        else :
            return f'You dont have enough Money. Your current balance is ${self.balance}'
    def get_balance(self) :
        return f'Your current balance is ${self.balance}'


sonali_bank = Bank(1000)
print(sonali_bank.get_balance())
sonali_bank.deposit(20000)
print(sonali_bank.withdraw(6000000))
print(sonali_bank.withdraw(50))
print(sonali_bank.withdraw(6000))
