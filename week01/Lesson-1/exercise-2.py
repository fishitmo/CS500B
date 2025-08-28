"""
    Exercises

• Problem specification: Find the square feet (Area) of a house.
Goal: Find the square feet (Area) of a house.
Output: The user will enter length and width interactively.
Formula: area = length * area.

• Program sketch:
1. Define integer numbers length, width and area.
2. Print program titles.
3. prompt the user to enter length and width.
4. Read length, width and print them out again so that the user can

verify that they were entered correctly.
5. Multiply the two numbers. Store the result in area.
6. Print the area.

"""

print('**Goal:/t/t/t Find the square feet (Area) of a house.**')

length = float(input("Enter the length of the house in feet:"))
print(f"the length of the house is : {length} feet")
width = float(input("Enter the width of the house in feet:"))
print(f"the width of the house is : {width} feet")


area = length * width

print(f"The area of the house with length {length} feet and width {width} feet is : {area:.2f} square feet") 