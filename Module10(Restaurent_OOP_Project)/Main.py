from Menu import Burger, Pizza, Drink, Menu
from Restaurent import Restaurent
from User import Chef, Server, Manager, Customer
from Order import Order

def main() : 
    menu = Menu ()
    # add pizza to the menu
    pizza1 = Pizza('BBQ Pizza', 600, 'large', ['grilled chicken', 'Onions', 'Cheese', 'Sauce', 'Tomato'])
    menu.add_to_menu('pizza', pizza1)
    pizza2 = Pizza('Hawalian Beef Pizza', 800, 'large', ['beef', 'cheese', 'sausage', 'mashroom', 'sauce'])
    menu.add_to_menu('pizza', pizza2)
    pizza3 = Pizza('Margherrita Prawn Pizza', 700,'large', ['Prawn', 'chicken', 'cheese', 'mashroom', 'sauce', 'tomato'])
    menu.add_to_menu('pizza', pizza3)

    # add burger to the menu
    burger1 = Burger('Beef Double Burger', 300, 'beef', ['beef', 'latos', 'cheese', 'sauce', 'bread'])
    menu.add_to_menu('burger', burger1)
    burger2 = Burger('Crispy Chicken Burger', 250, 'chicken', ['crispy chicken', 'latos', 'cheese', 'bread'])
    menu.add_to_menu('burger', burger2)
    burger3 = Burger('Mashroom Swiss Burger', 200, 'chicken', ['mashroom', 'chicken', 'latos', 'cheese', 'sauce', 'bread'])
    menu.add_to_menu('burger', burger3)
    burger4 = Burger('Naga Burger', 360, 'chicken', ['chicken', 'chilie', 'bread', 'sauce'])
    menu.add_to_menu('burger', burger4)


    # add drink to the menu
    coke = Drink("Coke", 50, True)
    menu.add_to_menu('drink', coke)
    coffe = Drink("Black Coffe", 100, False)
    menu.add_to_menu('drink', coffe)


    # show the menu
    menu.show_menu()


    # add employee 
    restaurent = Restaurent("Khaza Baba Restaurent", 2000, menu)
    
    chef = Chef("Abdul Momin", '3949020', 'abdul@gmail.com', 'Chittagong', 1000, "02.01.2021", 'chef')
    restaurent.add_employee('chef', chef)

    manager = Manager("Rustom Ali", '455020', 'rustom@gmail.com', "Dhaka", 1000, "02.02.2021", 'manager')
    restaurent.add_employee('manager', manager)

    server = Server("Shamim Ahmed", "8889020", 'shamim@gmail.com', "Sylhet", 500, "02.03.2021", 'server')
    restaurent.add_employee('server', server)


    # show employee
    restaurent.show_employee()


    #create customer and placing an order for the customer
    customer1 = Customer("Kuddus Ali", '28347787', 'kuddus@gmail.com', 'Chittagong', 2000)
    order1 = Order(customer1, [pizza1, coke])
    customer1.place_order(order1)
    restaurent.add_order(order1)

    #customer paying bill
    value = customer1.pay_for_order(order1, 1000)
    if(value >= 0) : 
        restaurent.recieve_payment(order1, 1000, customer1)
    else : 
        print(f'Please pay {-(value)} TK more.')

    
    #create customer2 and placing an order for the customer2
    customer2 = Customer("Karim Ali", '448877', 'karim@gmail.com', 'Chittagong', 2000)
    order2 = Order(customer1, [burger4, coffe])
    customer2.place_order(order2)
    restaurent.add_order(order2)

    #customer2 paying bill
    value2 = customer2.pay_for_order(order2, 460)
    if(value2 >= 0) : 
        restaurent.recieve_payment(order2, 460, customer2)
    else : 
        print(f'Please pay {-(value2)} TK more.')

    #create customer3 and placing an order for the customer3
    customer3 = Customer("Rahmat Ali", '99237747', 'rahmat@gmail.com', 'Chittagong', 5000)
    order3 = Order(customer3, [burger4, pizza2, pizza3, coke, coke, coffe])
    customer3.place_order(order3)
    restaurent.add_order(order3)

    #customer2 paying bill
    value3 = customer3.pay_for_order(order3, 3000)
    if(value3 >= 0) : 
        restaurent.recieve_payment(order3, 3000, customer3)
    else : 
        print(f'Please pay {-(value3)} TK more.')


    #get restaurent income
    print(f'\nRevenue : {restaurent.revenue} \t Expenses : {restaurent.expenses} \t Balance : {restaurent.balance}\n')

    #paying rent of the restaurent
    restaurent.pay_expenses(restaurent.rent, "Rent")

    #get restaurent income
    print(f'\nRevenue : {restaurent.revenue} \t Expenses : {restaurent.expenses} \t Balance : {restaurent.balance}\n')

    #pay salary to the chef
    restaurent.pay_salary(chef)

    #get restaurent income
    print(f'\nRevenue : {restaurent.revenue} \t Expenses : {restaurent.expenses} \t Balance : {restaurent.balance}\n')



#call the main function 
if __name__ == '__main__' : 
    main()
