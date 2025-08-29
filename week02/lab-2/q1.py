"""
    Question 1:
Write a Python program to implement a simple calculator.
1. Get two numbers and the operation desire
2. Check the operation
a. If the operation is addition, the result is the first + the second
b. If the operation is subtraction, the result is the first - the second
c. If the operation is multiplication, the result is the first * the second
d. If the operation is division, check the second number
i. If the second number is zero, construct an error message
ii. If the second number is not zero, the result is the first / the second

3. Print out the result or the error message
"""

def main():
    print("A Simple Calculator")
    
    while True:
        num1= int(input("Enter the first number:"))
        num2= int(input("Enter the second number:"))
        operation = input("Enter the operation (+, -, * or /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        
        elif operation == '*':
            result = num1 * num2
            
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            else:
                result = num1 // num2
            
        print("The result is", result)
        
        cont = input("Do you want to continue (y/n)? ")
        if cont.lower() == 'n':
            break

if __name__ == "__main__":
    main()