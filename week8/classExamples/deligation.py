
import enum

class Builder(enum.Enum):
    builderA = 1
    builderB = 2
    builderC = 3
    
class Wood(enum.Enum):
    woodA = 1
    woodB = 2
    woodC = 3
    
class Model(enum.Enum):
    modelA = 1
    modelB = 2
    modelC = 3
    
class Coat(enum.Enum):
    coatA = 1
    coatB = 2
    coatC = 3
    
# create the Table class as an aggreagation of the TableSpec class

class Table:
    def __init__(self, serialNumber, price, tableSpec):
        self.__serialNumber = serialNumber
        self.__price = price
        self.__tableSpec = tableSpec
        
    @property
    def serialNumber(self):
        return self.__serialNumber
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price
        
    @property
    def tableSpec(self):
        return self.__tableSpec
    
    def display(self):
        print("serialNumber:", self.serialNumber)
        print("price:", self.price)
        self.tableSpec.display()
        
        


# create the TableSpec class
class TableSpec:
    def __init__(self, builder, model, backWood, topWood,coat):
        self.__builder = builder
        self.__model = model
        self.__backWood = backWood
        self.__topWood = topWood
        self.__coat = coat
        
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
    
    
    @property
    def coat(self):
        return self.__coat
    
    def display(self):
        print("builder:", self.builder)
        print("model:", self.model)
        print("backWood:", self.backWood)
        print("topWood:", self.topWood)
        print("coat:", self.coat)
        
    # create the match method 
    def match(self, tableSpec):
        if self.builder != tableSpec.builder:
            return False
        if self.model != tableSpec.model:
            return False
        if self.backWood != tableSpec.backWood:
            return False
        if self.topWood != tableSpec.topWood:
            return False
        if self.coat != tableSpec.coat:
            return False
        return True
    
class Inventory:
    def __init__(self):
        self.__tables = []
        
    def addTable(self, serialNumber, price, tableSpec):
        table = Table(serialNumber, price, tableSpec)
        self.__tables.append(table)
        
    def searchTable(self, tableSpec):
        matchedTables = []
        for table in self.__tables:
            if table.tableSpec.match(tableSpec):
                matchedTables.append(table)
        return matchedTables
    
    
def main():
    
    inventory = Inventory()
    inventory.addTable("123456", 1000, TableSpec(Builder.builderA, Model.modelA, Wood.woodA, Wood.woodA, Coat.coatA)) 
    inventory.addTable("223456", 1100, TableSpec(Builder.builderA, Model.modelA, Wood.woodA, Wood.woodA, Coat.coatA)) 
    inventory.addTable("323456", 1200, TableSpec(Builder.builderB, Model.modelB, Wood.woodB, Wood.woodC, Coat.coatA)) 
    inventory.addTable("423456", 1300, TableSpec(Builder.builderB, Model.modelB, Wood.woodB, Wood.woodC, Coat.coatA)) 
    inventory.addTable("523456", 1400, TableSpec(Builder.builderC, Model.modelC, Wood.woodA, Wood.woodC, Coat.coatA))
    
    tableSpec = TableSpec(Builder.builderA, Model.modelA, Wood.woodA, Wood.woodA, Coat.coatA)
    matchedTables = inventory.searchTable(tableSpec)
    for table in matchedTables:
        table.display()
        print()
        
if __name__ == "__main__": 
    main()