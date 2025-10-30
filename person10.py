class Hand:
    def __init__(self, fingers):
        self.__fingers = fingers
        
    def __str__(self):
        return f"Hand: {self.__fingers}"
   
class Person:
    
    def __init__(self, name, age, lfingers, rfingers):
        self.__name = name
        self.__age = age
        self.__lhand = Hand(lfingers) # Create Object
        self.__right = Hand(rfingers) # Create Object
    
   
    
    def __str__(self):
        return f"Person: {self.__name}, Age: {self.__age}, {self.__lhand}, {self.__right}"
        
def main():
    # lhand = Hand(5)
    # rhand = Hand(5)
    p1 = Person("John", 25, 5, 5)
    p2 = Person("Jane", 30, 4, 5)
    print(p1)
    print(p2)
        

if __name__ == "__main__":
    main()
