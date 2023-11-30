# decorator having no parameter
def timer(func) :

    def inner_func() : 
        print('time starts')
        func()
        print('timer ends')

    return inner_func

@timer 
def get_factorial() :
    print('Calculating the factorial.')

# get_factorial()


# decorator having specific numbers of parameter (n1, n2)
def multiply(func) : 
    def inner_func(a, b) :
        print('multiply starts')
        func(a, b)
        print('multiply ends')

    return inner_func

@multiply
def get_mul(n1, n2) :
    print("Inside get_mul, product : ", end='')
    res = n1*n2
    print(res)
    

# get_mul(10, 20)



# decorator having unknown numbers of parameter (using *args or **kargs)
def sum_many(func) : 

    def inner_func(*args) :
        print('sum starts')
        func(args)
        print('sum ends')

    return inner_func

@sum_many
def get_sum(n) :
    print("Inside get_sum, total : ", end='')
    total = sum(n)
    print(total)
    

get_sum(10, 20, 30, 40)
