class Product:
    def __init__(self, name: str, price: int) -> None:
        self.__name = name
        self.__price = price
    
class Phone(Product):
    def __init__(self, name: str, price: int, network: str) -> None:
        Product.__init__(self, name, price)
        # super().__init__(name, price)
        self.__network = network
        
class Computer(Product):
    def __init__(self, name: str, price: int, speed: int) -> None:
        Product.__init__(self,name, price)
        # super().__init__(name, price)
        self.__speed = speed
        
class SmartPhone(Phone, Computer):
    def __init__(self, name: str, price: int, network: str, speed: int, camera: str) -> None:
        Phone.__init__(self, name, price, network)
        Computer.__init__(self, name, price, speed)
        self.__camera = camera
        
def main():
    # P = Phone("iPhone", 1200, "5G")
    # C = Computer("MacBook", 2500, 4000)
    # print(SmartPhone.mro())
    obj = SmartPhone("iPhone", 1200, "5G", 4000, "8K")
    # print(obj)
    print(vars(obj))
    print(SmartPhone.mro())

if __name__ == "__main__":
    main()
    
