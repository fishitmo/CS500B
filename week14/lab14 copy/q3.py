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
        query = "CREATE TABLE if not exists " + self.__table_name + "("
        for column, data_type in self.__columns.items():
            query += column + " " + data_type + ","
        
        query = query[:-2] + ")"
        print(f"{query};")
        self.__obj.execute(query)
        print(f"Table {self.__table_name} created.")
        
class InsertCommand(Command):
    def __init__(self, obj: Database, table_name: str, columns: dict) -> None:
        self.__obj = obj
        self.__table_name = table_name
        self.__columns = columns
        
    def execute(self) -> None:
        query = "INSERT INTO " + self.__table_name + "("
        
        for column in self.__columns.keys():
            query += column +  ", "
        
        query = query[:-2] + ") VALUES ("
        
        for value in self.__columns.values():
            if isinstance(value, str):
                query += f"'{value}', "
            else:
                query += f"{value}, "
                
        query = query[:-2] + ")"
        print(f"{query};")
        self.__obj.execute(query)
        print(f"Table {self.__table_name} has been inserted.")
        
        
  
def main():
    db = Database("test.db")
    
    command = CreateCommand(db, "users", {'id': 'INTEGER PRIMARY KEY', 'name':'TEXT'})
    command.execute()
    
    command = InsertCommand(db, "users", {'id': 1, 'name':'Peter'})
    command.execute()
    
    
if __name__ == "__main__":
    main()
    
    

# 1. SEPARATION OF CONCERNS:
#    - User Interface (main) is decoupled from database operations
#    - Each operation is encapsulated in its own command class

# 2. FLEXIBILITY:
#    - Easy to add new database operations (just create a new Command class)
#    - Commands can be queued, logged, or undone if needed

# 3. SINGLE RESPONSIBILITY:
#    - Database class (Receiver): Handles SQLite connection and execution
#    - Command classes: Contain operation-specific logic
#    - Invoker class: Manages command execution

# 4. EXTENSIBILITY:
#    - New commands can be added without modifying existing code
#    - Example: Could add DropTableCommand, AlterTableCommand, etc.

# 5. BATCH OPERATIONS:
#    - Multiple commands can be queued and executed together
#    - Provides transaction-like behavior
#     """)