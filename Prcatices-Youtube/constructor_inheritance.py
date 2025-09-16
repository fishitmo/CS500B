# Constructor in Inheritance Python
# Method Resloution Order (MRO)

# class A:
    
#     def __init__(self):
#         print("In A  init")
    
#     def feature1(self):
#         print("Feature 1 working")
        
#     def feature2(self):
#         print("Feature 2 working")



class A:
    
    def __init__(self):
        print("In A  init")
    
    def feature1(self):
        print("Feature 1-A working")
        
    def feature2(self):
        print("Feature 2 working")
 

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("In B  init")
#     def feature3(self):
#         print("Feature 3 working")
        
#     def feature4(self):
#         print("Feature 4 working")

# class B:
#     def __init__(self):
#         print("In B  init")
#     def feature3(self):
#         print("Feature 3 working")
        
#     def feature4(self):
#         print("Feature 4 working")


class B:
    def __init__(self):
        print("In B  init")
    def feature1(self):
        print("Feature 1-B working")
        
    def feature4(self):
        print("Feature 4 working")
    
class C(A , B):
    
    def __init__(self):
        super().__init__()
        print("In C  init")
        
    def feat(self):
        super().feature2()
        
    
# a1 = A()
# b1 = B()

c1 = C()
# c1.feature1()
c1.feat()


'''
N.B ; Sub class can access all the features of Super class

but Super class can not access any features of Sub class

- if you create objects of Sub class it will  first try find init of Sub class, if it is 
not found then it will call init of Super class
- Method Resolution Order (MRO): whether it is calling for init or a method 
the order of calling will be from left to right
'''
