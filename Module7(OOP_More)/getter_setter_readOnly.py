class Bank : 
    bank = 'Brac'
    def __init__(self, name, age, money) -> None:
        self._name = name
        self.__age = age
        self.__balance = money
    
    def age(self) : 
        return self.__age
    
    # getter, Read Only ----> we can only read the property, cant change or set the value
    @property
    def bank_balance (self) : 
        return self.__balance
    
    # setter 
    @bank_balance.setter
    def set_balance(self, amount) : 
        if( amount > 0) :
            self.__balance = amount
    
    # setter 
    @bank_balance.setter
    def deposit(self, amount) : 
        if (amount > 0) : 
            self.__balance += amount

samsu = Bank("Samsu", 34, 40000)
print(samsu._name)
# print(samsu.__balance) # we cant access private attribute (__balance)
print('Age : ', samsu.age())

print(f'Balance of Samsu : ', samsu.bank_balance) # getter convert the method into a property

samsu.set_balance = 50000 # set the balance amount to 50000 TK

print(f'Balance of Samsu : ', samsu.bank_balance, ' (After set the balance)') 

samsu.deposit = 5000 # deposit 5000 Tk

print(f'Balance of Samsu : ', samsu.bank_balance, ' (After deposit)') 







