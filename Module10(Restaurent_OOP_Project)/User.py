from abc import ABC, abstractmethod

class User(ABC) : 
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User) : 
    def __init__(self, name, phone, email, address, money) -> None:
        super().__init__(name, phone, email, address)
        self.__order = None
        self.bill_due = 0
        self.wallet = money

    @property
    def order(self) :
        return self.order
    
    @order.setter
    def order(self, order) : 
        self.__order = order


    def place_order(self, order) : 
        self.order = order
        self.bill_due += order.bill
        return f'{self.name} placed an order with bill {order.bill}'
    
    def pay_for_order(self, order, amount) :
        #Submit money to the manager
        return (amount - order.bill)

    def tips_for_waiter(self, tips_amount) :
        pass

    def write_review(self, text) :
        pass


class Employee(User) :
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department
    
    def recieve_salary(self) :
        self.due = 0

class Chef(Employee) :
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_items = None
    


class Server(Employee) :
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.tips_earning = 0

    def recieve_tips(self, tips_amount) :
        self.tips_earning += tips_amount 


class Manager(Employee) :
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)


