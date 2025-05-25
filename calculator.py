while True:
    a1 = float(input("Enter first number: "))
    c1 = input("Enter operator (+, -, *, /, %): ")
    b1 = float(input("Enter second number: "))
    if c1 == '+':
        print(f'Addition of {a1} and {b1} is: {a1 + b1}')
    elif c1 == '-':
        print(f'Subtraction of {a1} and {b1} is: {a1 - b1}')
    elif c1 == '*':
        print(f'Multiplication of {a1} and {b1} is: {a1 * b1}')
    elif c1 == '/':   
        if b1 != 0:
            print(f'Division of {a1} and {b1} is: {a1 / b1}')
        else:
            print("Cannot divide by zero.")
    elif c1 == '%':
        if b1 != 0:
            print(f'Modulus of {a1} and {b1} is: {a1 % b1}')    
        else:
        
            print("Cannot perform modulus by zero.")
    else:
        print("Invalid operator. Please use +, -, *, /, or %.")
        
    choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if choice != 'yes':
        print("Goodbye!")
        break