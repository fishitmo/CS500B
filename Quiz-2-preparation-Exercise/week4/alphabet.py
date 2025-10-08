class ClassA:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c
    def method_a(self):
        print("method_a =", self.a)
    def _method_b(self):
        print("_method_b =",self._b)
    def __method_c(self):
        print("__method_c =",self.__c)


class ClassB(ClassA):
    def __init__(self, a, b, c, d):
        ClassA.__init__(self, a, b, c)
        self._d = d         # protected attribute
        
    def method_d(self):            # protected method
        print("method_d =", self._d)
        
    def method_test(self):
        # These two attribute are allowed 
        print("a =", self.a)
        print("b =", self._b)
        # print("c =", self.__c)  # This is a private attribute and should have access only by class A
        
        # these two method calls are allowed
        ClassA.method_a(self)
        ClassA._method_b(self)
        # ClassA.__method_c(self)  # This is a private method and should have access only with in class A
        
def main():
    bobj = ClassB(2, 4, 6, 8)
    # bobj.method_test()
    # print()
    print("bobj.a =", bobj.a)
    print("bobj._b =", bobj._b)
    # print("bobj.__c =", bobj.__c)
    
    bobj.method_a()
    bobj._method_b()
    # bobj.__method_c()
    bobj.method_d()

if __name__ == "__main__":
    main()