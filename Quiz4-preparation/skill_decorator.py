from abc import ABC , abstractmethod

class Person(ABC):
    @abstractmethod
    def work(self):
        pass
    
class Student(Person):
    
    def work(self):
        print("Studing ...")
        
class Teacher(Person):
    
    def work(self):
        print("Teaching ...")
        
class SkillDecorator(Person):
    
    def __init__(self, obj: Person)->None:
        
        self.__obj = obj
        
    def work(self):
        self.__obj.work()
        
class Software(SkillDecorator):
    
    def work(self):
        super().work()
        print("Programming ...")
        
class Hardware(SkillDecorator):
    def work(self):
        super().work()
        print("Maintenance ...")
        
class Management(SkillDecorator):
    
    def work(self):
        super().work()
        print("Managing ...")
        

def main():
    pers1 = Student()
    pers1 = Software(pers1)
    pers1 = Hardware(pers1)
    pers1 = Management(pers1)
    pers1.work()
    
    pers2 = Management(Hardware(Software(Teacher())))
    pers2.work()

if __name__ =="__main__":
    main()
    