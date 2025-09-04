'''
Question 5:
Write a method rectangle_of_symbols that displays a solid rectangle of symbols whose height and width are
specified in integer parameter “height” and “width” respectively. And this method also receive a third parameter
of type char called “symbol”. For example, if height is 5, weight is 4, and the symbol is *, the method should
display
****
****
****
****
****
Create a main function that reads the height, width and symbol of the user and then calls the
rectangle_of_symbols method to display the rectangle of symbols. Example,
def main():
print('Print a rectangle of symbols')
height = int(input("Enter the height: "))
weight = int(input("Enter the weight: "))
symbol = input("Enter the symbol: ")
rectangle_of_symbols(height, weight, symbol)
'''

def rectangle_of_symbols(height, width, symbol):
    for i in range(height):
        for j in range(width):
            print(symbol, end="")
        print()
def main():
    print("Print a rectangle of symbols")
    height = int(input("Enter the height: "))
    width = int(input("Enter the width:"))
    symbol = input("Enter the symbol:")
    rectangle_of_symbols(height, width, symbol)
    
if __name__ == "__main__":
    main()