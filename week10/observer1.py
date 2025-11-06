from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def notify(self, data) -> None:
        pass
    
    @abstractmethod
    def subscribe(self, observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer) -> None:
        pass
class Observer(ABC):
    @abstractmethod
    def update(self, data) -> None:
        pass


class Teacher(Subject):
    def __init__(self, name) -> None:
        self.__name = name
        self.__observers = []
        
        
    def subscribe(self, observer) -> None:
        self.__observers.append(observer)
    
    def unsubscribe(self, observer) -> None:
        self.__observers.remove(observer)
        
    def notify(self, data) -> None:
        for observer in self.__observers:
            observer.update(data)
        
    def create_assignment(self, assignment: str) -> None:
        print(f"Teacher: {self.__name} is creating a new assignment {assignment}")
        self.notify(assignment)


class Student(Observer):
    def __init__(self, name):
        self.__name= name
    
    def do_assignment(self, assignment) -> None:
        print(f"Student: {self.__name} is doing assignment {assignment}")
    
    def update(self, data) -> None:
        self.do_assignment(data) 
        
class Dean(Observer):
    
    def __init__(self, name) -> None:
        self.__name = name
    
    def review_assignment(self, assignment: str) -> None:
        print(f"Dean: {self.__name} is reviewing assignment {assignment}")
    def update(self, data) -> None:
        self.review_assignment(data)
def main():
    teacher = Teacher("Mr. Smith")
    student1 = Student("Alice")
    student2 = Student("Bob")
    # student3 = Student("Fsehaye")
    dean = Dean("Dr. Johnson")
    teacher.subscribe(dean)
    teacher.subscribe(student1)
    teacher.subscribe(student2)
    # teacher.subscribe(student3)
    # teacher.unsubscribe(student3)
    teacher.create_assignment("HW1") 
    print()
    teacher.create_assignment("HW2")

   
    # student1.do_assignment("HW1")
    # student2.do_assignment("HW1")

   
if __name__ == "__main__":
    main()