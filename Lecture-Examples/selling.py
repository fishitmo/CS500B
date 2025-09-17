from market import Apple, Barrel

def main():
    print("The Market Test Program")
    print()
    
    while True:
        capacity = float(input("Enter the capacity of the barrel: "))
        
        barrel = Barrel(capacity)
        while True:
           type = input("Enter the type of the apple: ")
           weight = float(input("Enter the weight of the apple: "))
           price = float(input("Enter the price of the apple: "))
           apple = Apple(type, weight, price)
           barrel.add_apple(apple)
           
           choice = input("Do you want to add another apple? (y/n): ")
           print()
           if choice.lower() != 'y':
               print("Your barrell has these apples:")
               print(barrel)
               break
           
        choice = input("Do you want to add another barrel? (y/n): ")
        print()
        if choice.lower() != 'y':
            print("Goodbye")
            break
        
if __name__ == '__main__':
    main()