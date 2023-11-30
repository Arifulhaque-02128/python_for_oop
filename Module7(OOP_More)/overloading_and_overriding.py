class Person : 
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self) :
        print('Rice, Fish, Daal')
    
    def exercise(self) :
        return NotImplementedError # override na kore call korle error dibe

class Cricketer(Person) :
    def __init__(self, name, age, height, weight, runs, wickets) -> None:
        super().__init__(name, age, height, weight)
        self.runs = runs
        self.wickets = wickets

    def __repr__(self) -> str:
        print(f'Name : {self.name} \nAge : {self.age} \nRuns : {self.runs} \nWickets : {self.wickets}')
        return ''
    
    # override
    def eat(self) :
        print("I eat bread, Chicken and so on")

    def exercise(self):
        print("I used to go GYM")
    
    #overloading
    def __add__(self, other) :
        total = self.runs + other.runs
        return total
    
    def __mul__(self, other) :
        res = self.age * other.age
        return res
    
    def __len__(self) :
        res = self.height
        return res
    
    def __gt__(self, other) :
        if(self.age > other.age) : 
            return 'Sakib is Elder'
        else :
            return 'Sakib is not Elder'


sakib = Cricketer('Sakib', 34, 160, 75, 5700, 321)
# print(sakib)
# sakib.eat()
# sakib.exercise()

tamim = Cricketer('Tamim', 35, 162, 82, 7700, 0)
# print(tamim)
# tamim.eat()
# tamim.exercise()

partnership = sakib + tamim
print(f'Sakib + Tamim : {partnership} runs')

mul = sakib * tamim
print(f'sakib age * tamim age : {mul}')

length = len(sakib)
print(f'Height of Sakib : {length} cm')

elder = sakib > tamim
print(elder)





