


class Property:

    def __init__(self, address: str, price: float, square_footage: int, num_bedrooms: int, property_type: str) -> None:
        self.__address = address
        self.__price = price
        self.__square_footage = square_footage
        self.__num_bedrooms = num_bedrooms
        self.__property_type = property_type

    @property
    def address(self) -> str:
        return self.__address

    @property
    def price(self) -> float:
        return self.__price

    @property
    def square_footage(self) -> int:
        return self.__square_footage

    @property
    def num_bedrooms(self) -> int:
        return self.__num_bedrooms

    @property
    def property_type(self) -> str:
        return self.__property_type
    
    
    
if __name__ == "__main__":
    pass


