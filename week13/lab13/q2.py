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
    
class ShapeAdapter(LegacyRectangle):
    
    def __init__(self, obj: ModernShape) -> None:
        self.__obj = obj
        
    def get_width(self) -> float:
        import math
        perimeter = self.__obj.get_perimeter()
        area = self.__obj.get_area()
        
        semi_perimeter = perimeter/2
        discriminant = (semi_perimeter**2) - (4*area)
        
        if discriminant < 0:
            raise ValueError("Invalide area/perimeter combination for a rectangle")
        # take the larger root as width
        width = (semi_perimeter + math.sqrt(discriminant))/2
        return width
    
    def get_height(self) -> float:
        
        import math
        perimeter = self.__obj.get_perimeter()
        area = self.__obj.get_area()
        
        semi_perimeter = perimeter/2
        discriminant = (semi_perimeter**2) - (4*area)
        
        if discriminant < 0:
            raise ValueError("Invalide area/perimeter combination for a rectangle")
        # take the smaller root as height
        height = (semi_perimeter - math.sqrt(discriminant))/2
        return height
    
class ShapeFactory:
    
    @staticmethod
    def get_shape() -> ModernShape:
        # return ModernShape(100, 40)
        return RectangleAdapter(LegacyRectangle(10,10))
    
    @staticmethod
    def get_legacy_rectangle() -> LegacyRectangle:
        return ShapeAdapter(ModernShape(100, 40))
    
def main():
    
    shape = ShapeFactory.get_shape()
    # print(shape.get_area())
    print(f"Area: {shape.get_area()} ")
    # print(shape.get_perimeter())
    print(f"Perimeter: {shape.get_perimeter()}")
    
    shape2 = ShapeFactory.get_legacy_rectangle()
    print(f"Width: {shape2.get_width()} ")
    print(f"Height: {shape2.get_height()}")

    
if __name__ =="__main__":
    main()
    
    
