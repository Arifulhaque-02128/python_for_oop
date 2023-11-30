class Animal :
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self) : 
        print('I cant make a sound')

    def eat(self) : 
        print('I eat nothing. ')
        print()


class Dog(Animal) :
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Gheu Gheu")
    
    def eat(self) :
        print("I eat bones")
        print()


class Cat(Animal) :

    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Meao, Meao")
    
    def eat(self) :
        print("I eat fish")
        print()

class Bird(Animal) :
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Kuhu Kuhu")



dog1 = Dog('Shephard')
dog1.make_sound()
dog1.eat()

cat1 = Cat('Bonni')
cat1.make_sound()
cat1.eat()

bird1 = Bird('Titu')
bird1.make_sound()
bird1.eat()