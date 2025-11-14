class FirstSystem:
    
    def foo(self, x:int) -> str:
        return str(x)
    
    
class SecondSystem:
    
    def bar(self, y: str) ->int:
        
        return int(y)
    
class ThirdSystem:
    def dump(self, x: str, y:str) -> int:
        return int(x) + int(y)
    
class Adapter2(FirstSystem):
    
    def __init__(self, obj: ThirdSystem) ->None:
        self.__obj = obj
        
    def foo(self, x:int) -> str:
        
        return str(self.__obj.dump(str(x) , "0"))     
    
class Adapter(FirstSystem):
    
    def __init__(self, obj: SecondSystem) ->None:
        self.__obj = obj
        
    def foo(self, x:int) -> str:
        
        return str(self.__obj.bar(str(x)))

class Factory:
    
    @staticmethod
    def get_system() -> FirstSystem:
        # return FirstSystem()
        # return Adapter(SecondSystem())
        return Adapter2(ThirdSystem())
    
    
def main():
    
    system= Factory.get_system()
    print(system.foo(123))
    
if __name__ =="__main__":
    main()    
    