from abc import ABC, abstractmethod
# from typing import Optional
import enum
class ClassroomType(enum.Enum):
    LECTURE_HALL = 1
    SEMINAR_ROOM = 2
    COMPUTER_LAB = 3
    LEARNING_CLASSROOM = 4
class OnlineSchoolType(enum.Enum):
    PUBLIC_SCHOOL = 1
    CHARTER_SCHOOL = 2
    PRIVATE_SCHOOL = 3

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

class Student(Displayable):
    def __init__(self, student_id:int, student_name:str, total_scores : float) -> None:
        self.__student_id = student_id
        self.__student_name = student_name
        self.__total_scores = total_scores
    

    # setters and getters here
    @property
    def student_id(self) -> int:
        return self.__student_id
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
    def __init__(self,school_name:str) -> None:
        self.__school_name = school_name
        self.__students:list[Student] = []
        

    
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

    def get_top_five_students(self) -> list[Student]:
        top_five :list[Student] = []
        
        for student in self:
            current_score = student.total_scores
            
            
            inserted = False
            for i in range(len(top_five)):
                if current_score > top_five[i].total_scores:
                    top_five.insert(i, student)
                    inserted = True
                    break
            
           
            if not inserted and len(top_five) < 5:
                top_five.append(student)
            
            
            if len(top_five) > 5:
                top_five = top_five[:5]
        
        return top_five
    
    def get_student(self,student_id : int) -> Student|None:
        for student in self:
            if student.student_id == student_id:
                return student
        return None
    

class Classroom(Displayable):
    def __init__(self,classroom_name:str,area:float,seats:int,type :ClassroomType ) -> None:
        self.__classroom_name = classroom_name
        self.__area = area
        self.__seats = seats
        self.__type = type
        self.__students : list[Student] = []
        
    
    @property
    def type(self) -> ClassroomType:
        return self.__type
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

    def remove_students(self,student_name:str) -> None:
        i = 0
        while i< len(self.__students):
            if self.__students[i].student_name == student_name:
                self.__students[i]= self.__students[-1]
                self.__students.pop()
            else:
                i+=1
    def get_students_count(self):
        return len(self.__students)
            
class OnlineSchool(School):
    def __init__(self, school_name: str, students: list[Student],category :OnlineSchoolType) -> None:
        super().__init__(school_name)
        self.__category = category
        self.__classrooms :list[Classroom]= []
        
        self.__students: list[Student] = []
        
    @property
    def category(self) ->OnlineSchoolType:
        return self.__category
    def __iter__(self):
            self.__index =-1
            return self
    def __next__(self):
         
         if self.__index >= len(self.__classrooms) -1:
            raise StopIteration()
         self.__index +=1
         classroom = self.__classrooms[self.__index]
         return classroom
    def __str__(self) -> str:
        output = super().__str__()
        output+= f"Category : {self.__category}\n"
        for classroom in self:
            output+=str(classroom)
        return output
    def add_classroom(self,classroom:Classroom)->None:
        self.__classrooms.append(classroom)
    def find_largest_classroom(self) -> Classroom:
        largest=0


        for classroom in self:
            if classroom.get_students_count()>largest:
                largest=classroom.get_students_count()
                largest_classroom = classroom
        return largest_classroom
            
    def get_classroom_to_type(self) -> dict:
        classroom_dict : dict[ClassroomType,list[Classroom]]= {}
        
        for classroom in self:
            classroom_type = classroom.type
            
            if classroom_type not in classroom_dict:
                classroom_dict[classroom_type] = []
            
            classroom_dict[classroom_type].append(classroom)
        
        return classroom_dict
    def assign_student_to_classroom(self, student_id: int, classroom_type: ClassroomType) -> None:
        for s in self.__students:
            if s.student_id == student_id:
                student = s
                break
        
        
        available_classrooms: list[Classroom] = []
        for classroom in self.__classrooms:
            if classroom.type == classroom_type :
                available_classrooms.append(classroom) 
        available_classrooms[0].add_student(student)
    def display(self) -> None:
        print(self)
def main():
    

    student1 = Student(1,"Shazib",123.89)
    student2 = Student(2,"haseeb",113.89)
    student3 = Student(3,"abdullah",132.89)
    student4 = Student(4,"Peter",133.89)
    student5 = Student(5,"Lilly",178.89)
    student6 = Student(6,"Peter",1201.89)
    student7 = Student(7,"Peter",12.89)

   



    # testing School Class

    school = School("SFBU")
    school.add_student(student1)
    school.add_student(student2)
    # school.add_student(student3)

    print(school)
    #school after adding a student
    school.add_student(student3)

    print("School After adding a student")

    school.display()

    print("Top  students are:")

    students_top = school.get_top_five_students()

    for student in students_top:
        print(student)



    print("Student with student id 2 is")
    print(school.get_student(2))

    # testing classroom 
    classroom = Classroom("101 Lab",456.23,23,ClassroomType.COMPUTER_LAB,students)

    classroom.display()

    print("Classroom after adding multiple student")
    
    classroom.add_student(student4)
    classroom.add_student(student5)
    classroom.add_student(student6)
    classroom.add_student(student7)
    print(classroom)

    print("Students after removing Peter")

    classroom.remove_students("Peter")

    classroom.display()
    class_rooms = []
    class_rooms.append(classroom)


    online_School = OnlineSchool ("SFBU ONLINE SCHOOL", students,OnlineSchoolType.PRIVATE_SCHOOL,class_rooms)
    print(online_School)

    online_School.add_classroom(classroom)
    print(online_School)
    online_School.assign_student_to_classroom(2,ClassroomType.COMPUTER_LAB)
    clas_type= online_School.get_classroom_to_type()
    room = online_School.find_largest_classroom()
    print(room)


if __name__ == "__main__":
    main()
    

        

        

                
        
    
        