# Demonstration of Method Resolution Order (MRO)

class GrandParentX:
    pass

class GrandParentY:
    pass

class GrandParentZ:
    pass

class GrandParentW:
    pass

class GrandParentV:
    pass

class ParentA(GrandParentX, GrandParentY):
    pass

class ParentB(GrandParentZ, GrandParentW):
    pass

class Child(ParentA, ParentB, GrandParentV):
    pass

print(Child.mro())