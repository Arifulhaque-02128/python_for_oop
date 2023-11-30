def my_function(arg1, *args):
    print("First argument:", arg1)
    print("Additional arguments:", args)

my_function("first", "second", "third", "fourth")


def my_function(arg1, **kwargs):
    print("First argument:", arg1)
    print("Additional arguments:", kwargs)

my_function("first", second="2nd", third="3rd", fourth="4th")


