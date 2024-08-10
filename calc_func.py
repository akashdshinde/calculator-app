# addition
def do_addition(a:int,b:int):
    return a + b
# substraction
def do_substraction(a,b):
    return a - b
# division
def do_division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return 'can not divide by zero'

