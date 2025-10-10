class G:
    def __init__(self, g) -> None:
        self.__g = g

class A(G):
    def __init__(self, g, a) -> None:
        G.__init__(self, g)
        self.__a = a

class B(G):
    def __init__(self, g, b) -> None:
        G.__init__(self, g)
        self.__b = b
        
class C(A, B):
    def __init__(self, g, a, b, c) -> None:
        A.__init__(self, g, a)
        B.__init__(self, g, b)
        self.__c = c
    
o = C(1, 2, 3, 4)    # What is C? C is a class name, create an object of C
print(C.__mro__)
print(vars(o))

