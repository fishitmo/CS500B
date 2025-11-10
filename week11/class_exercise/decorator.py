from abc import ABC, abstractmethod, abstractproperty

class Perosn(ABC):
    @abstractmethod
    def work(self)->None:
        
        pass
    
    
class Student(Perosn):
    def work(self)->None:
        print("studying ...")

class SkillDecorator(Perosn):
    def __init__(self,  obj: Perosn) -> None:
        self.__obj = obj
        
    def work(self)->None:
        self.__obj.work()


class Software(SkillDecorator):
     def work(self)->None:
        super().work()
        print("Programming ...")
 

class Hardware(SkillDecorator):
    def work(self)->None:
        super().work()
        print("Wiring ...")

class Management(SkillDecorator):
    def work(self)->None:
        super().work()
        print("Managing ...")

def main():
    obj = Student()
    obj = Management(Hardware(Software(obj)))
    obj.work()

if __name__ == "__main__":
    main()  
    
    
    