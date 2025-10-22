class A:
    def __init__(self):
        print("A.__init__called")
        self.a_value = 1
        
        
class B:
    def __init__(self):
        print("B.__init__called")
        self.b_value = 2
        
   
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c_value = 3
        
        

c = C()
print(c)