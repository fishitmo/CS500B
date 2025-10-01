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
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project
    
        
    def dowork(self):
        print("Teacher", self.name, "teaching classes")
        
    def display(self):
        print("Name =", self.name)
        print("Salary =", self.salary)
        print("Project =", self.project)
        
class TA(Teacher, Student):
    def __init__(self, name, gpa, salary, project):        
        # super().__init__(name, gpa) # TypeError: __init__() missing 1 required positional argument: 'project'
        super().__init__(name,salary, project)
        
    def dowork(self):
        super().dowork()
        print("TA", self.name, "grading homework")
        
    def display(self):
        super().display()
def main():
  
    
    ta = TA("John", 3.5, 50000, 'MAX5')
    ta.dowork()
    ta.display()
    
if __name__ == "__main__":
    main()