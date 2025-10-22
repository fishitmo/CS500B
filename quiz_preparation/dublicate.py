class Parent:
    def __init__(self):
        self.__private = "Parents Private"
        
        
    def get_parent_private(self):
        return self.__private
    
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private = "Child Private"
        
    def get_child_private(self):
        return self.__private
    
child = Child()
# print(child.get_parent_private())
# print(child.get_child_private())

print(child._Parent__private)
print(child._Child__private)