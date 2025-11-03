class Something:
    
    def __init__(self, name) -> None:
        self.__name  = name
        
    def walk(self):
        print(f"{self.__name} Walking...")
        
    def sleep(self):
        print(f"{self.__name} Sleeping...")
        
        
class Decorator(Something):
    def __init__(self, obj: Something):
        self.__obj = obj
    
    def walk(self):
        self.__obj.walk()
        
    def sleep(self):
        self.__obj.sleep()
    
    def swim(self)->None:
        print("Swimming...")
    
    def jump(self)->None:
        print("Jumping...")
        
    
        

    
def main():
    obj = Something("Peter")
    obj = Decorator(obj)
    obj.swim()
    obj.jump()
    obj.walk()
    obj.sleep()
        
if __name__ == "__main__":
    main()

    