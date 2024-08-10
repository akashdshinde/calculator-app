
from calc_func import do_addition,do_substraction
from area import calculate_area_rectangle
from multiply import do_multiplication

def main():
    print("welcome to the calculator app")
    print("""
          \nselect the function from the given functions
          1. Add
          2. Substract
          3. Multiply
          4. Area
          """)
    
    user_input = input("select the function")
    
    a = int(input("value of A "))
    b = int(input("value of B "))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "2":
        result = do_substraction(a,b)
    elif user_input == '3':
        result = do_multiplication(a,b) 
    elif user_input == '4':
        result = calculate_area_rectangle(a,b)

    print("Result:",result)

if __name__ == "__main__":
    main()