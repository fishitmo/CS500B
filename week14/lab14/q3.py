from abc import ABC, abstractmethod
import sqlite3
class Database:
    
    def __init__(self, db_file) -> None:
        self.__db_file = db_file
        self.__conn = sqlite3.connect(self.__db_file)
        
    def execute(self, query, params = None):
        if params is None:
            params = []
            
        cursor = self.__conn.cursor()
        cursor.execute(query, params)
        self.__conn.commit()
        return cursor.fetchall()
    
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
    
class CreateCommand(Command):
    def __init__(self, obj: Database, table_name: str, columns: dict) -> None:
        self.__obj = obj
        self.__table_name = table_name
        self.__columns = columns
        
    def execute(self) -> None:
        query = "CREATE TABLE if not exist"
        params = []
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.fetc
  
def main():
    pass  
    
if __name__ == "__main__":
    main()