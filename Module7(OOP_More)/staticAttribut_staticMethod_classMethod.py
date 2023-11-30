class Shopping :
    cart = [] # static attribute
    totalCost = 0 # static attribute

    def __init__(self, name) -> None:
        self.name = name
    
    def purchase(self, item, price, amount) :
        self.cart.append(item)
        self.totalCost += price
        remaining = amount - price

        print(f'Total Purchase : {self.totalCost}')
        print('Cart : ', end=' ')
        for i in self.cart :
            print(i, end=', ')
        
        print()
        print(f"Remaining : {remaining}")
    
    @classmethod # we can call a class method directly without making any instance
    def visiting(self, item) :
        print(f'I have came to watch {item}, not to buy.')
    
    @staticmethod  # static method dont need any self, and it can't access any class attribute (like : cart, name, totalCost). And we can call a static method directly without making any instance
    def multiply(a, b) :
        result = a * b
        return result
    

bashundhara = Shopping('bashundhara')
bashundhara.purchase('sunglass', 500, 1000)
bashundhara.purchase('cap', 200, 1000)
# bashundhara.visiting('shoe') 

# Shopping.purchase('shoe', 1250, 2000) # we can not call purchase method directly wihout making any instance

print()
Shopping.visiting('Shoe') # we can call visiting method directly wihout making any instance, because it is a class method

print()
print(f'Result : {Shopping.multiply(40, 5)}')


