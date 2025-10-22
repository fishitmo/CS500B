from abc import ABC, abstractmethod
import enum
class ClassroomType(enum.Enum):
    LECTURE_HALL = 1
    SEMINAR_ROOM = 2
    COMPUTER_LAB = 3
    LEARNING_CLASSROOM = 4

class Displayable(ABC):
    def display(self):
        pass

class Student(Displayable):
    def __init__(self, student_id:int, student_name:str, total_scores : float) -> None:
        self.__student_id = student_id
        self.__student_name = student_name
        self.__total_scores = total_scores
    

    # setters and getters here

    @property
    def student_name(self) -> str:
        return self.__student_name
    @property
    def total_scores(self) -> float:
        return self.__total_scores
    
    @student_name.setter
    def student_name(self, student_name:str):
        self.__student_name = student_name
    @total_scores.setter
    def total_scores(self, total_scores:float):
        self.__total_scores = total_scores

    # str function

    def __str__(self) -> str:
        return f"Student Id : {self.__student_id}\nStudent Name: {self.student_name}\nTotal Socres: {self.total_scores}\n"
    
    def display(self) -> None:
        print(self)

class School(Displayable):
    def __init__(self,school_name:str,students:list[Student]) -> None:
        self.__school_name = school_name
        self.__students = []
        for student in students:
            self.__students.append(student)

    
    @property
    def school_name(self) -> str:
        return self.__school_name
    @school_name.setter
    def school_name(self,school_name:str) -> None:
        self.__school_name = school_name
    def __iter__(self):
            self.__index =-1
            return self
    def __next__(self):
         
         if self.__index >= len(self.__students) -1:
            raise StopIteration()
         self.__index +=1
         student = self.__students[self.__index]
         return student  

    def __str__(self) -> str:
        output = f"School Name: {self.school_name}\n"

        for student in self:
            output += str(student)

        return output

    def display(self) -> None:
        print(self)

    def add_student(self,student: Student) -> None:
        self.__students.append(student)
class Classroom(Displayable):
    def __init__(self,classroom_name:str,area:float,seats:int,type :ClassroomType ,students:list[Student]) -> None:
        self.__classroom_name = classroom_name
        self.__area = area
        self.__seats = seats
        self.__type = type
        self.__students = []
        for student in students:
            self.__students.append(student)
    
    def __iter__(self):
            self.__index =-1
            return self
    def __next__(self):
         
         if self.__index >= len(self.__students) -1:
            raise StopIteration()
         self.__index +=1
         student = self.__students[self.__index]
         return student  

    def  __str__(self) -> str:
        output = f"Classroom Name: {self.__classroom_name}\nArea : {self.__area}\nSeats : {self.__seats}\nType : {self.__type}\n"
        
        for student in self:
            output += str(student)

        return output
    def add_student(self,student: Student) -> None:
        self.__students.append(student)
    def display(self) -> None:
        print(self)

def main():
    students : list[Student] = []

    student1 = Student(1,"Shazib",123.89)
    student2 = Student(2,"haseeb",133.89)
    student3 = Student(3,"abdullah",133.89)

    students.append(student1)
    students.append(student2)

    # testing School Class

    school = School("SFBU",students)

    print(school)
    #school after adding a student
    school.add_student(student3)

    print("School After adding a student")

    school.display()

    # testing classroom 
    classroom = Classroom("101 Lab",456.23,23,ClassroomType.COMPUTER_LAB,students)

    classroom.display()

    print("Classroom after adding a student")
    student4 = Student(4,"Peter",133.89)
    classroom.add_student(student4)
    print(classroom)





if __name__ == "__main__":
    main()
    

        

        

                
        
    
        