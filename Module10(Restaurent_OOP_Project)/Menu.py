class Food : 
    def __init__(self, name, price) -> None:
        self.name = name 
        self.price = price
        self.cooking_time = 15


class Burger(Food) : 
    def __init__(self, name, price, meat, ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients

class Pizza(Food) :
    def __init__(self, name, price, size, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings


class Drink(Food) : 
    def __init__(self, name, price, isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold


#composition
class Menu : 
    def __init__(self) -> None:
        self.burgers = []
        self.pizzas = []
        self.drinks = []
    
    def add_to_menu(self, item_type, item) : 
        if (item_type == 'burger') :
            self.burgers.append(item)
        elif(item_type == 'pizza') : 
            self.pizzas.append(item)
        elif(item_type == 'drink') : 
            self.drinks.append(item)

    def remove_from_menu(self, item_type, item) : 
        if (item_type == 'burger') :
            if (item in self.burgers) :
                self.burgers.remove(item)
        elif(item_type == 'pizza') : 
            if(item in self.pizzas) : 
                self.pizzas.remove(item)
        elif(item_type == 'drink') : 
            if(item in self.drinks) : 
                self.drinks.remove(item)

    def show_menu(self) : 
        print('\n \n')
        print("--------- FOOD MENU ---------")
        print('\n')
        for pizza in self.pizzas : 
            print(f'Name : {pizza.name} \t Price : {pizza.price}')

        for burger in self.burgers : 
            print(f'Name : {burger.name} \t Price : {burger.price}')
        
        for drink in self.drinks : 
            print(f'Name : {drink.name} \t Price : {drink.price}')

        print('\n \n')
