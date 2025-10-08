# the super() function is used to give access to the methods and properties of a parent or sibiling class

# Without using super()

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
        print("name =", self.__name)
        print("age =", self.__age)
        
# class Student(Person):
#     def __init__(self, name, age, gpa):
#         Person.__init__(self, name, age)
#         self.__gpa = gpa
        
#     @property
#     def gpa(self):
#         return self.__gpa
    
#     def display(self):
#         Person.display(self)
#         print("gpa =", self.__gpa)
        
#     def study(self):
#         print(self.name,"has been studying so hard")

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.__gpa = gpa
        
    @property
    def gpa(self):
        return self.__gpa
    
    def display(self):
        super().display()
        print("gpa =", self.__gpa)
        
    def study(self):
        print(self.name,"has been studying so hard")
        
        
        
def main():
    s1 = Student("John", 20, 3.5)
    # s1.display()
    # s1.study()
    vars(Student)
    
if __name__ == "__main__":
    main()
    