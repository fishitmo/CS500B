
""" 

Write a python program that asks for a string as input and determine whether it is a palindrome (reads the same backward as forward) or not.

Constraints: Use only indvidual character comparsions and string reversal techniques, avoiding slicing and built-in functions like reversed().
"""

# get input from the user
str_input = input("Please enter a string: ")

# check if the string is a palindrome

for i in range(len(str_input) // 2):
    if str_input[i] != str_input[len(str_input)-1-i]:
        print(f"{str_input} is a not a palindrome.")
        break
    elif i == (len(str_input) // 2) - 1:
        print(f"{str_input} is a palindrome.")