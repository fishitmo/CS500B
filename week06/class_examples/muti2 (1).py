class P:
    def __init__(self, p) -> None:
        self.p = p
    def __str__(self) -> str:
        return f"p={self.p}"
    
class A(P):
    def __init__(self, p, a) -> None:
        P.__init__(self, p)
        self.a = a

    def __str__(self) -> str:
        
        return f"a={self.a}"

class B(P):
    def __init__(self, p, b) -> None:
        P.__init__(self, p)
        self.b = b
        
    def __str__(self) -> str:
        return  f"b={self.b}"

class C(A, B):
    def __init__(self, p, a, b, c) -> None:
        A.__init__(self, p, a)
        B.__init__(self, p, b)
        self.c = c
    def __str__(self) -> str:
        return A.__str__(self) + "\n" + B.__str__(self) + f"\nc={self.c}"
        
    
def main():
    obj = C(5, 10, 20, 30)
    print(vars(obj))
    print(obj)

if __name__ == "__main__":
    main()