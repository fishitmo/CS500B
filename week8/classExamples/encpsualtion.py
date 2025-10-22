
import enum

class Builder(enum.Enum):
    builderA = 1
    builderB = 2
    builderC = 3
    
    
class Models(enum.Enum):
    modelA = 1
    modelB = 2
    modelC = 3
    
class Wood(enum.Enum):
    woodA = 1
    woodB = 2
    woodC = 3


class TableSpec:
    def __init__(self, builder, model, backWood, topWood):
        self.__builder = builder
        self.__model = model
        self.__backWood = backWood
        self.__topWood = topWood
        
    @property
    def builder(self):
        return self.__builder
    
    @property
    def model(self):
        return self.__model
    
    @property
    def backWood(self):
        return self.__backWood
    
    @property
    def topWood(self):
        return self.__topWood
    
    def display(self):
        print("builder:", self.builder)
        print("model:", self.model)
        print("backWood:", self.backWood)
        print("topWood:", self.topWood)
        
class Table:
    def __init__(self, serialNumber, price, builder, model, backWood, topWood):
        self.__serialNumber = serialNumber
        self.__price = price
        self.__tableSpec = TableSpec(builder, model, backWood, topWood)
        
    @property
    def serialNumber(self):
        return self.__serialNumber
    
    @property
    def price(self):
        return self.__price
    
    @property
    def tableSpec(self):
        return self.__tableSpec
    
    def display(self):
        print("serialNumber:", self.serialNumber)
        print("price:", self.price)
        self.tableSpec.display()
        
        
class Inventory:
    def __init__(self):
        self.__tables = []
        
    def addTable(self, serialNumber, price, 
                 builder, model, backWood, topWood):
        table = Table(serialNumber, price, 
                      builder, model, backWood, topWood)
        self.__tables.append(table)
        
    def searchTable(self, tableSpec):
        matchedTables = []
        for table in self.__tables:
            if table.tableSpec.builder != tableSpec.builder:
                continue
            if table.tableSpec.model != tableSpec.model:
                continue
            if table.tableSpec.backWood != tableSpec.backWood:
                continue
            if table.tableSpec.topWood != tableSpec.topWood:
                continue
            matchedTables.append(table)
        return matchedTables
    
def main():
   
    inventory = Inventory()
    inventory.addTable("123456", 1000, Builder.builderA, Models.modelA, Wood.woodA, Wood.woodA) 
    inventory.addTable("223456", 1100, Builder.builderA, Models.modelA, Wood.woodA, Wood.woodA) 
    inventory.addTable("323456", 1200, Builder.builderB, Models.modelB, Wood.woodB, Wood.woodC) 
    inventory.addTable("423456", 1300, Builder.builderB, Models.modelB, Wood.woodB, Wood.woodC) 
    inventory.addTable("523456", 1400, Builder.builderC, Models.modelC, Wood.woodA, Wood.woodC)
    
    tableSpec = TableSpec(Builder.builderA, Models.modelA, Wood.woodA, Wood.woodA)
    matchedTables = inventory.searchTable(tableSpec)
    for table in matchedTables:
        table.display()

if __name__ == "__main__":
    main()