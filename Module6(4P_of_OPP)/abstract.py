from abc import ABC, abstractmethod

class Animal(ABC) :
    @abstractmethod
    def make_sound(self) : # As make_sound() is an abstract method, child class must have it
        pass

    def eat(self) : # eat() is not an abstract method, so it's optional for child class
        print('I eat nothing. ')


class Dog(Animal) :
    def make_sound(self):
        print("Gheu Gheu")
    
    def eat(self) :
        print("I eat bones")


class Cat(Animal) :
    def make_sound(self):
        print("Meao, Meao")
    
    def eat(self) :
        print("I eat fish")

class Bird(Animal) :
    def make_sound(self):
        print("Kuhu Kuhu")



dog1 = Dog()
dog1.make_sound()
dog1.eat()

cat1 = Cat()
cat1.make_sound()
cat1.eat()

bird1 = Bird()
bird1.make_sound()
bird1.eat()
    

