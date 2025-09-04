'''
Question 6:
Write a method triangle_of_symbols that displays a solid triangle of symbols whose height is specified in
integer parameter “height”, the symbol is specified in string parameter “symbol”. For example, if height is 4 and
the symbolis *, the method should display
   *
  ***
 *****
*******
Create a main function that reads the height and symbol of the triangle and then calls the triangle_of_symbols
method to display the triangle of symbols.

'''

def traingle_of_symbols(height, symbol):
    for i in range(height):
        for j in range(height - i -1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print(symbol, end="")
        print()

def main():
    height = int(input("Enter the height:"))
    symbol = input("Enter the symbol:")
    traingle_of_symbols(height, symbol)
    
if __name__ == "__main__":
    main()