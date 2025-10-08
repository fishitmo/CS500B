from apple import Apple
from barrel import Barrel


def main():
    print("Market Test Program")
    print()
    
    while True:
        capcity = float(input("Enter the capacity of the barrel:"))
        barrel = Barrel(capcity)
        
        while True:
            type = input("Enter apple type:")
            weight = float(input("Enter apple weight:"))
            price = float(input("Enter apple price:"))
            apple = Apple(type, weight, price)
            barrel.add_apple(apple)
            
            choice = input("Do you want to add another apple? (y/n):")
            print()
            if choice.lower() != "y":
                print("Your barrel has these apples:")
                print(barrel)
                break
            
        choice = input("Do you want to add another barrel? (y/n):")
        print()
        if choice.lower() != "y":
            print("Goodbye")
            break            
        
                

if __name__ == "__main__":
    main()