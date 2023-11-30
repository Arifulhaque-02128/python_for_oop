class Phone : 
    company = "Redmi"

    def __init__(self, owner, color, price, model) -> None:
        self.owner = owner
        self.model = model
        self.color = color
        self.price = price
    
    def __repr__(self) -> str:
        return f'The owner of this phone, {self.model} is {self.owner}. Developed by {self.company}.'
    

my_phone = Phone('Arif', 'purple', 15000, 'Redmi 9')
print(my_phone)

friend_phone = Phone('Anis', 'Black', 26000, 'Redmi 10')
print(friend_phone)