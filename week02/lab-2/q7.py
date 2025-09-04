'''
Question 7:
Write a method circle_of_symbols that displays a solid circle of symbols whose radius is specified in integer
parameter “radius”, the symbol is specified in string parameter “symbol”. For example, if radius is 6 and the
symbolis *, the method should display
Please enter the radius of the circle: 6
Please enter the symbol character: A
      A A A A A
    A A A A A A A
  A A A A A A A A A
A A A A A A A A A A A
A A A A A A A A A A A
A A A A A A A A A A A
A A A A A A A A A A A
A A A A A A A A A A A
  A A A A A A A A A
    A A A A A A A
      A A A A A
Create a main function that reads the height and symbol of the circle and then calls the circle_of_symbols
method to display the circle of symbols.
'''

def circle_of_symbols(radius, symbol):
    for i in range(-radius,  radius+1):
        for j in range(-radius, radius+1):
            if i**2 + j**2 < (radius*(radius-1)):
                print(symbol, end=" ")
            else:
                print(" ", end=" ")
        print()
def main():
    radius = int(input("Enter the radius:"))
    symbol = input("Enter the symbol:")
    circle_of_symbols(radius, symbol)

if __name__ == "__main__":
    main()