# using super()

class Person:
    def __init__(self, name, age):
        
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    def display(self):
        print("Name =", self.__name)
        print("Age =", self.__age)
        
class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.__gpa = gpa
        
    @property
    def gpa(self):
        return self.__gpa
    
    def display(self):
        super().display()
        print("GPA =", self.__gpa)
        
    def study(self):
        print(f"{self.name} has been studing so hard")
        
def main():
    stud1 = Student("John", 20, 3.5)
    stud1.display()
    stud1.study()
    vars(stud1)
    dir(stud1)

if __name__ == "__main__":
    main()