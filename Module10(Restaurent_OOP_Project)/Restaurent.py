class Restaurent :
    def __init__(self, name, rent, menu = []) -> None:
        self.name = name 
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = menu
        self.rent = rent
        self.revenue = 0
        self.expenses = 0
        self.balance = 0
        self.profit = 0

    
    def add_employee(self, employee_type, employee) :
        if(employee_type == 'chef') :
            self.chef = employee
        
        elif(employee_type == 'server') :
            self.server = employee

        elif(employee_type == 'manager') : 
            self.manager = employee
    

    def add_order(self, order) :
        self.orders.append(order)

    def recieve_payment(self, order, amount, customer) :
        if (amount >= order.bill) :
            self.revenue += order.bill
            self.balance += order.bill
            customer.bill_due = 0
            extra = amount - order.bill
            if (extra == 0) : 
                print("Bill Paid. Thanks for visiting us.")
            else : 
                print(f'Bill Paid. You will get {extra} TK back. Thanks for visiting us.')
        
    def pay_expenses(self, amount, description) :
        if (amount < self.balance) :
            self.balance -= amount
            self.expenses += amount
            print(f'Expenses {amount} TK for {description}')

        else :
            print(f'No enough money in balance to pay {amount} Tk for {description}')

    def pay_salary(self, employee) :
        if( self.balance > employee.salary) :
            self.balance -= employee.salary
            self.expenses += employee.salary
            employee.recieve_salary()
            print(f'Paid {employee.salary} TK to {employee.name}\n')
        else :
            print(f'No enough money in balance to pay {employee.salary} Tk to {employee.name} as his salary')
        

    def show_employee(self) : 
        print("--------- OUR EMPLOYEE ---------")
        print('\n')
        if self.manager is not None : 
            print(f'Name : {self.manager.name} \t Salary : {self.manager.salary}')

        if self.chef is not None : 
            print(f'Name : {self.chef.name} \t Salary : {self.chef.salary}')

        if self.server is not None : 
            print(f'Name : {self.server.name} \t Salary : {self.server.salary}')

        print('\n \n')
