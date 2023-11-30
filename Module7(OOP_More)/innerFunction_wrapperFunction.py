
# inner function ----> we can return a function.
def outer_func() :
    print('Outer function is start.')
    def inner_func() :
        print('Inner Function')
        return 'Its inner function'
    print('Outer functionn is end')

    return inner_func

# print(outer_func())
# print(outer_func()()) # returned function should be called 



# wrapper functin ----> passing function as a parameter
def do_something(work) :
    print('Work starts')
    work()
    print('Work ends')


def coding() :
    print("I am coding")

do_something(coding)


    

    