import random

colors = ["Green", "Red", "Yellow"]


class Apple:
    
    def __init__(self, color, weight, price):
        self.color = color
        self.weight = weight
        self.price = price
        
    def change_color(self):
        clr = random.randint(0, 2)
        self.color = colors[clr]
        
    def __str__(self):
        return f"Color: {self.color}, Weight: {self.weight}, Price: {self.price}"

class Barrel:
    
    def __init__(self):
        self.list = []
        
    def add_apple(self, apple):
         self.list.append(apple)
         
    def change_all_colors(self):
        for apple in self.list:
            apple.change_color()
            
    def displayall(self):
        for apple in self.list:
            print(str(apple))
            
def main():
    a1 = Apple('Yellow', 0.5, 2.0)
    a2 = Apple('Red', 0.56, 2.0)
    a3 = Apple('Green', 1.2, 3.5)
    
    b1 = Barrel()
    b1.add_apple(a1)
    b1.add_apple(a2)
    b1.add_apple(a3)
    b1.displayall()
    
    print("\nAfter color changed:")
    b1.change_all_colors()
    b1.displayall()
    

if __name__ == "__main__":
    main()
        