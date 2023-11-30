class Bank : 
    def __init__(self, holder_name, branch, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute
        self._branch = branch # protected attribute
        self.__balance = initial_deposit # private attribute
    
    def deposit(self, amount) :
        if(amount > 0) :
            self.__balance += amount
    
    def get_balance(self) -> float :
        return self.__balance
    

dbbl = Bank('Asif', 'Sylhet', 10000)
print(dbbl.holder_name)
# print('Branch : ', dbbl._branch)
# print('Balance : ', dbbl.__balance)  # Can't be accessed because __balance is a private attribute

print('Balance : ', dbbl.get_balance())

dbbl.deposit(5000)
print('After Deposit, Balance : ', dbbl.get_balance())
