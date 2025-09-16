# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram  = ram
    
#     def config(self):
#         print("Config is:", self.cpu, self.ram)
    
    
    
# com1 = Computer("i5", 16)
# com2 = Computer("Rizen 3", 8)

# com1.config()
# com2.config()        


# class Computer:
#     def __init__(self):
#         self.name = "Fsehaye"
#         self.age = 35
        
#     def update(self):
#         self.age = 36
        
#     def compare(self, other):
#         if self.age == other.age:
#             return True
#         else: 
#             return False
        
        

# c1 = Computer()
# c2 = Computer()
# c1.update()

# if c1.compare(c2):
#     print("They are the same")
# else:
#     print("They are different")
    
    

# '''
# when we talk about variables in oop, ther are two types of variables:
#     1. Instance Variables
#     2. Class(Static) Variables
# '''


# class Car:
    
#     # if you define a varibale outside the class , it is called a class variable
    
#     wheels = 4    # class namespace
    
#     def __init__(self):
        
#         '''
#         if you define a varibale inside the class, it is called instance variable 
#         '''
#         self.mil= 10           # instance namespace
#         self.com = "BMW"       # instance namespace
        

# c1 = Car()
# c2 = Car()

# c1.mil = 8

'''

namespace is an area where you create and store object/varibale
    there are two types of namespace:
        1.  Class namespace
        2. Object/Instance namespace

'''

# Car.wheels = 5

# # print(c1.mil, c1.com)
# # print(c2.mil, c2.com)

# print(c1.mil, c1.wheels)
# print(c2.mil, c2.wheels)













# print(id(c1))
# print(id(c2))




'''
when we talk about methods in oop, there are three types of methods:
    1. Instance Methods
       Ther are two types of instance methods:
           1. Accessor Methods : only for reading or fetching data
           2. Mutator Methods : only for updating data or changing data
           
           N.B : If you are working with instance methods 
           then you need to pass self as a parameter in the method
    2. Class Methods
       
    N.B : If you are working with class methods 
    then you need to pass cls as a parameter in the method
    3. Static Methods
     we use a static method when we do not want to use any instance or class variables in the method
     
     
'''



# class Student:
#     school = "SFBU"
    
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     # avg is an instance method 
#     def avg(self): # if you are working with instance variables then you need to pass self as a parameter in the method
#         return (self.m1 + self.m2 + self.m3)/3  
     
#     # get_m1 is an accessor
#     def get_m1(self): # if you are working with instance variables then you need to pass self as a parameter in the method
#         return self.m1
    
#     # set_m1 is a mutator
#     def set_m1(self, value): # if you are working with instance variables then you need to pass self as a parameter in the method
#         self.m1 = value
     
#      # info is a class method
#      # if you want to create a class method then you need to use a special symbol or way of doing it called decorator   
#     @classmethod
#     def get_school(cls): # if you are working with class variables then you need to pass cls as a parameter in the method
#         return cls.school
#     # info is a static method
#     # this method is not dependent on any instance or class variables
#     # if you want to create a static method then you need to use a special symbol or way of doing it called decorator
#     @staticmethod
#     def info():
#         print("This is student class .. in abc module")
    

# s1 = Student(50, 60 , 70)
# s2 = Student(80, 90, 100)

# print(s1.avg())
# print(s2.avg())

# print(Student.get_school())
# print(Student.info())



# Start the next with Inner class in python @ 51:13


# Inner class in python

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
        
    class Laptop:
        
        def __init__(self):
            self.brand = "Lenovo"
            self.cpu = "Ryzen 3"
            self.ram = 32
            
        def show(self):
            print(self.brand, self.cpu, self.ram)
            

s1 = Student("Fsehaye", 1)
s2 = Student("Flix", 2)

s1.show()

