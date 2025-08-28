'''
Problem specification: Find an average.
Goal: Find the average of three numbers.
Output: The user will enter three numbers interactively, n1, n2, and n3.
Formula: n1 + n2 + n3
Average = ----------——-
3
• Program sketch:
1. Define real numbers n1, n2, n3 and Average.
2. Print program titles.
3. prompt the user to enter three numbers.
4. Read n1, n2, and n3 and print them out again so that the user can verify that
they were entered correctly.
5. Add the three numbers and divide the sum by 3. Store the result in Average.
6. Print the result with two decimal places.

• According to the specification, try to write a Python Program by yourself.
'''

# Finda an average

print("**Goal:/t/t/t Find the average of three numbers.**")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3= float(input("Enter the third number:"))

average = (num1 + num2 + num3) / 3

print(f"The average of {num1}, {num2} and {num3} is : {average:.2f}") 