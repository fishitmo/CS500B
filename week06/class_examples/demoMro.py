# Demonstaation of MRO

class GpX:
    pass

class GpY:
    pass

class GpZ:
    pass

class GpW:
    pass

class GpV:
    pass


class GpA(GpX, GpY):
    pass

class GpB(GpZ, GpW):
    pass

class Child(GpA, GpB, GpV):
    pass


print(Child.__mro__)



