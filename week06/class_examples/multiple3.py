class P:
    def __init__(self, p) -> None:
        self.__p = p

class Q:
    def __init__(self, q) -> None:
        self.__q = q

class A(P):
    def __init__(self, p, a) -> None:
        super().__init__(p)
        self.__a = a

class B(Q):
    def __init__(self, q, b) -> None:
        super().__init__(q)
        self.__b = b
        
class C(A, B):
    def __init__(self, p, q, a, b, c) -> None:
        A.__init__(self, p, a)
        B.__init__(self, q, b)
        self.__c = c
    
o = C(1, 2, 3, 4, 5)    # What is C? C is a class name, create an object of C
print(C.__mro__)
print(vars(o))

