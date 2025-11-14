class LegacyRectangle:
    
    def __init__(self, width: int, height: int) -> None:
        
        self.__width = width
        self.__height = height
        
    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height
    
    
class ModernShape:
    
    def __init__(self, area: int, perimeter: int) -> None:
        
        self.__area = area
        self.__perimeter = perimeter
        
    def get_area(self) -> int:
        return self.__area
    
    def get_perimeter(self) -> int:
        return self.__perimeter
    
class RectangleAdapter(ModernShape):
    def __init__(self, obj: LegacyRectangle) -> None:
        self.__obj = obj
        
    def get_area(self) -> int:
        return self.__obj.get_height()*self.__obj.get_width()
    
    def get_perimeter(self) -> int:
        return (self.__obj.get_height() + self.__obj.get_width())*2
    
class ShapeFactory:
    
    @staticmethod
    def get_shape() -> ModernShape:
        # return ModernShape(100, 40)
        return RectangleAdapter(LegacyRectangle(10,10))
    
def main():
    
    shape = ShapeFactory.get_shape()
    print(shape.get_area())
    print(shape.get_perimeter())
    
if __name__ =="__main__":
    main()
    
    
    # Those are the remain I need to do for the lab
    """
    ● Using the attributes of the LegacyRectangle object, implement the RectangleAdapter class's get_area()
    and get_perimeter() methods.
   ● Create a ShapeAdapter adapter class that implements the LegacyRectangle interface. The
   ModernShape object should be adapted to the LegacyRectangle interface by the ShapeAdapter. Also,
   ask yourself which class is the adaptee in this case?.
   ● Using the attributes of the ModernShape object, implement the ShapeAdapter class's get_width() and
   get_height() methods.
    """