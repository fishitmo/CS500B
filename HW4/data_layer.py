from enum import Enum
from abc import ABC , abstractmethod
class PeriodicalType(Enum):
    JOURNAL = "JOURNAL"
    MAGAZINE = "MAGAZINE"
    NEWSPAPER = "NEWSPAPER"
    

class CoverType(Enum):
    HARDCOVER = "HARDCOVER"
    PAPERBACK = "PAPERBACK"
    CLOTHCOVER = "CLOTHCOVER"
    
class FormatType(Enum):  
    DVD = "DVD"
    BLU_RAY = "BLU_RAY"
    VCD = "VCD"
    

class Catalog(ABC):
    
    def __init__(self, catalog_num: int , title: str, published_date: str) -> None:
        
        self.__catalog_num = catalog_num
        self.__title = title
        self.__published_date = published_date
        
    @property
    def catalog_num(self) -> int:
        return self.__catalog_num
        
    def __eq__(self, other) -> bool:
        if isinstance(other, Catalog):
            return self.__catalog_num == other.catalog_num
        return False
    
    @abstractmethod
    def __str__(self):
        pass

class Article:
    
    def __init__(self,title: str, author: str, issue_date: str, periodical_title: str) -> None:
        
        self.__title = title
        self.__author = author
        self.__issue_date = issue_date        # article_date
        self.__periodical_title = periodical_title
        
    def __str__(self)-> str:
        
        return (f"Article: '{self.__title}', by {self.__author}\n"
                f"        Published: {self.__issue_date} in {self.__periodical_title}")
        



def main():
    
    art1 = Article('developing an algorithm for neural network', 'Fsehaye Medhanie', '06/30/2024', 'Machine Learning')
    
    print(art1)
    
if __name__ =="__main__":
    main()
        
        
        