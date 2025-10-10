class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa
        
    
    def dowork(self):
        print("Student", self.name, "doing homework")
        
    def display(self):
        print("Name =", self.name)
        print("GPA =", self.gpa)




class Teacher:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    
        
    def dowork(self):
        print("Teacher", self.name, "teaching classes")
        
    def display(self):
        print("Name =", self.name)
        print("Salary =", self.salary)
        
class TA(Teacher, Student):
    def __init__(self, name, gpa, salary):        
        super().__init__(name, gpa)
        
    def dowork(self):
        super().dowork()
        print("TA", self.name, "grading homework")
        
    def display(self):
        super().display()
def main():
    # s = Student("John", 3.5)
    # s.dowork()
    # s.display()
    
    ta = TA("John", 3.5, 50000)
    ta.dowork()
    ta.display()
    print(TA.mro())
    
if __name__ == "__main__":
    main()