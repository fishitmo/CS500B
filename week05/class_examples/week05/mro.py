# Demonstration of MRO

class GrandParentX:
    pass

class GrandParentY:
    pass

class GrandParentZ:
    pass

class ParentA(GrandParentX, GrandParentY):
    pass

class ParentB(GrandParentY, GrandParentZ):
    pass

class Child(ParentA, ParentB, GrandParentZ):
    pass


print(Child.mro())

"""
[<class '__main__.Child'>, 
<class '__main__.ParentA'>, <class '__main__.GrandParentX'>, 
<class '__main__.ParentB'>, <class '__main__.GrandParentY'>, 
<class '__main__.GrandParentZ'>, 
<class 'object'>]
"""