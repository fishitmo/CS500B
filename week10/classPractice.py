from __future__ import annotations
from abc import ABC , abstractmethod

class Subject(ABC):
    @abstractmethod
    def notify(self, data: object) -> None:
        pass
    
    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass
    
    
class Observer(ABC):
    @abstractmethod
    def update(self, data) -> None:
        pass
    
class Teacher(Subject):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observers = []
        
    def subscribe(self, observer: Observer) -> None:
        return self.__observers.append(observer)
    
    def unsubscribe(self, obsever: Observer) -> None:
        return self.__observers.remove(Observer)
    
    def notify(self, data: object) ->None:
        for observer in self.__observers:
            observer.update(data)
            
    def create_assignment(self, assignment: str):
        print(f"Teacher {self.__name} created assignment {assignment}")
        self.notify(assignment)
        
        
class Student(Observer):
    def __init__(self, name: str) -> None:
        self.__name = name
    
    def do_assignment(self, assignment: str) -> None:
        print(f"Student {self.__name} is doing assignment {assignment}")
        
    
    def update(self, data) -> None:
        self.do_assignment(data)
        
class Dean(Observer):
    def __init__(self, name: str) -> None:
        self.__name = name
        
    def review_assignment(self, assignment: str) -> None:
        
        print(f"Dean {self.__name} is review assignment {assignment}")
        
        
    def update(self, data)-> None:
        self.review_assignment(data)
        

def main():
    
    t = Teacher("Henry")
    s1 = Student("Peter")
    s2 = Student("Nancy")
    s3 = Student("Lily")
    d = Dean("Dave")
    
    
    t.subscribe(d)
    t.subscribe(s1)
    t.subscribe(s2)
    t.subscribe(s3)
    
    t.create_assignment("HW4")
    
    
if __name__ == "__main__":
    main()
    

        
            
        
        
        