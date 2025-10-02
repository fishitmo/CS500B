from abc import ABC, abstractmethod, abstractproperty

class Parent(ABC):
    
    @abstractmethod
    def dowork(self):
        pass
    
    @abstractmethod
    def make_money(self):
        pass
class Child(Parent):
    
    def dowork(self):
        print("Learn computer programming")
        
class Grandchild(Child):
    
    def make_money(self):
        print("Stock  Trading!")
        
def main():
    
    # TypeError: Can't instantiate abstract class Parent with abstract methods dowork, make_money
    # p = Parent()
    
    # TypeError: Can't instantiate abstract class Child with abstract methods make_money
    # c = Child()
    
    g = Grandchild()
    g.dowork()
    g.make_money()
    
    
if __name__ == "__main__":
    main()
   