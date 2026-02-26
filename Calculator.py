def Calculator():
    while True:
        print("Enter the first number:")
        num1 = float(input())
        
        print("Enter the second number:")
        num2 = float(input())
        
        print("Select operation: +, -, *, /")
        operation = input()
        
        if operation == '+':
            result = num1 + num2
            print("Result: ", result)
        elif operation == '-':
            result = num1 - num2
            print("Result: ", result)
        elif operation == '*':
            result = num1 * num2
            print("Result: ", result)
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print("Result: ", result)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please try again.")
        
        print("Do you want to perform another calculation? (yes/no)")
        continue_calculation = input().lower()
        if continue_calculation != 'yes':
            break

if __name__ == "__main__":
    Calculator()