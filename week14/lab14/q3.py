"""
EXPLANATION: How Command Pattern Benefits This Application
1. SEPARATION OF CONCERNS:
   - User Interface (main) is decoupled from database operations
   - Each operation is encapsulated in its own command class

2. FLEXIBILITY:
   - Easy to add new database operations (just create a new Command class)
   - Commands can be queued, logged, or undone if needed

3. SINGLE RESPONSIBILITY:
   - Database class (Receiver): Handles SQLite connection and execution
   - Command classes: Contain operation-specific logic
   - Invoker class: Manages command execution

4. EXTENSIBILITY:
   - New commands can be added without modifying existing code
   - Example: Could add DropTableCommand, AlterTableCommand, etc.

5. BATCH OPERATIONS:
   - Multiple commands can be queued and executed together
   - Provides transaction-like behavior
    """



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
        print(f"Record inserted into {self.__table_name}.")


class RetrieveCommand(Command):
    def __init__(self, obj: Database, table_name: str, condition: str | None = None) -> None:
        self.__obj = obj
        self.__table_name = table_name
        self.__condition = condition

    def execute(self) -> None:
        query = f"SELECT * FROM {self.__table_name}"
        if self.__condition:
            query += f" WHERE {self.__condition}"

        print(f"{query};")
        results = self.__obj.execute(query)

        if results:
            print(f"Retrieved {len(results)} record(s):")
            for row in results:
                print(row)
        else:
            print("No records found.")


class UpdateCommand(Command):
    def __init__(self, obj: Database, table_name: str, updates: dict, condition: str) -> None:
        self.__obj = obj
        self.__table_name = table_name
        self.__updates = updates
        self.__condition = condition

    def execute(self) -> None:
        query = f"UPDATE {self.__table_name} SET "

        for column, value in self.__updates.items():
            if isinstance(value, str):
                query += f"{column} = '{value}', "
            else:
                query += f"{column} = {value}, "

        query = query[:-2]
        query += f" WHERE {self.__condition}"

        print(f"{query};")
        self.__obj.execute(query)
        print(f"Record updated in {self.__table_name}.")


class DeleteCommand(Command):
    def __init__(self, obj: Database, table_name: str, condition: str) -> None:
        self.__obj = obj
        self.__table_name = table_name
        self.__condition = condition

    def execute(self) -> None:
        query = f"DELETE FROM {self.__table_name} WHERE {self.__condition}"

        print(f"{query};")
        self.__obj.execute(query)
        print(f"Record deleted from {self.__table_name}.")


class DropTableCommand(Command):
    def __init__(self, obj: Database, table_name: str) -> None:
        self.__obj = obj
        self.__table_name = table_name

    def execute(self) -> None:
        query = f"DROP TABLE IF EXISTS {self.__table_name}"

        print(f"{query};")
        self.__obj.execute(query)
        print(f"Table {self.__table_name} dropped.")


class DatabaseInvoker:
    def __init__(self) -> None:
        self.__commands = []

    def add_command(self, command: Command) -> None:
        self.__commands.append(command)

    def execute_commands(self) -> None:
        for command in self.__commands:
            command.execute()
            print()
        self.__commands.clear()


def main():
  
    print("SQLite Database Client Application - Command Pattern Demo")
    

    # Receiver: Database connection
    db = Database("test.db")

    # Invoker: Manages and executes commands
    invoker = DatabaseInvoker()

    # Drop table if it exists to start fresh
   
    invoker.add_command(DropTableCommand(db, "users"))
    invoker.execute_commands()

    # Demonstration 1: Create Table

    create_cmd = CreateCommand(db, "users", {
        'id': 'INTEGER PRIMARY KEY',
        'name': 'TEXT',
        'email': 'TEXT',
        'age': 'INTEGER'
    })
    invoker.add_command(create_cmd)
    invoker.execute_commands()

    # Demonstration 2: Insert Records
    
    invoker.add_command(InsertCommand(db, "users", {'id': 1, 'name': 'Peter', 'email': 'peter@example.com', 'age': 25}))
    invoker.add_command(InsertCommand(db, "users", {'id': 2, 'name': 'Sarah', 'email': 'sarah@example.com', 'age': 30}))
    invoker.add_command(InsertCommand(db, "users", {'id': 3, 'name': 'John', 'email': 'john@example.com', 'age': 28}))
    invoker.execute_commands()

    # Demonstration 3: Retrieve All Records
   
    retrieve_all_cmd = RetrieveCommand(db, "users")
    invoker.add_command(retrieve_all_cmd)
    invoker.execute_commands()

    # Demonstration 4: Retrieve Specific Record
   
    retrieve_specific_cmd = RetrieveCommand(db, "users", "age > 26")
    invoker.add_command(retrieve_specific_cmd)
    invoker.execute_commands()

    # Demonstration 5: Update Record
    
    update_cmd = UpdateCommand(db, "users", {'age': 26, 'email': 'peter.smith@example.com'}, "id = 1")
    invoker.add_command(update_cmd)
    invoker.execute_commands()

    # Verify update
   
    invoker.add_command(RetrieveCommand(db, "users", "id = 1"))
    invoker.execute_commands()

    # Demonstration 6: Delete Record
  
    delete_cmd = DeleteCommand(db, "users", "id = 3")
    invoker.add_command(delete_cmd)
    invoker.execute_commands()

    # Verify deletion
 
    invoker.add_command(RetrieveCommand(db, "users"))
    invoker.execute_commands()

    # Demonstration 7: Batch Operations

    invoker.add_command(InsertCommand(db, "users", {'id': 4, 'name': 'Alice', 'email': 'alice@example.com', 'age': 22}))
    invoker.add_command(InsertCommand(db, "users", {'id': 5, 'name': 'Bob', 'email': 'bob@example.com', 'age': 35}))
    invoker.add_command(RetrieveCommand(db, "users"))
    invoker.execute_commands()




def sales_demonstration():
    
    print("SALES DATABASE DEMONSTRATION - Command Pattern")
    

    
    sales_db = Database("sales.db")
    invoker = DatabaseInvoker()

    # Drop existing table if present
    invoker.add_command(DropTableCommand(sales_db, "Sales"))
    invoker.execute_commands()

    # Create Sales table
    create_sales_table = CreateCommand(sales_db, "Sales", {
        'salesperson': 'TEXT',
        'amt': 'REAL',
        'year': 'INTEGER',
        'model': 'TEXT',
        'new': 'BOOLEAN'
    })
    invoker.add_command(create_sales_table)
    invoker.execute_commands()

    # Insert sales data

    invoker.add_command(InsertCommand(sales_db, "Sales",
        {'salesperson': 'Tim', 'amt': 16000, 'year': 2010, 'model': 'Honda Fit', 'new': True}))
    invoker.add_command(InsertCommand(sales_db, "Sales",
        {'salesperson': 'Tim', 'amt': 9000, 'year': 2006, 'model': 'Ford Focus', 'new': False}))
    invoker.add_command(InsertCommand(sales_db, "Sales",
        {'salesperson': 'Gayle', 'amt': 8000, 'year': 2004, 'model': 'Dodge Neon', 'new': False}))
    invoker.add_command(InsertCommand(sales_db, "Sales",
        {'salesperson': 'Gayle', 'amt': 28000, 'year': 2009, 'model': 'Ford Mustang', 'new': True}))
    invoker.add_command(InsertCommand(sales_db, "Sales",
        {'salesperson': 'Gayle', 'amt': 50000, 'year': 2010, 'model': 'Lincoln Navigator', 'new': True}))
    invoker.add_command(InsertCommand(sales_db, "Sales",
        {'salesperson': 'Don', 'amt': 20000, 'year': 2008, 'model': 'Toyota Prius', 'new': False}))
    invoker.execute_commands()

    # Query all sales records
    
    invoker.add_command(RetrieveCommand(sales_db, "Sales"))
    invoker.execute_commands()

    # Query sales by specific salesperson
    
    invoker.add_command(RetrieveCommand(sales_db, "Sales", "salesperson = 'Gayle'"))
    invoker.execute_commands()

    # Query new car sales
    
    invoker.add_command(RetrieveCommand(sales_db, "Sales", "new = 1"))
    invoker.execute_commands()

    # Query sales above $20,000
 
    invoker.add_command(RetrieveCommand(sales_db, "Sales", "amt > 20000"))
    invoker.execute_commands()

    # Update a record
   
    invoker.add_command(UpdateCommand(sales_db, "Sales",
        {'amt': 17000}, "salesperson = 'Tim' AND model = 'Honda Fit'"))
    invoker.execute_commands()

    # Verify update
   
    invoker.add_command(RetrieveCommand(sales_db, "Sales", "salesperson = 'Tim'"))
    invoker.execute_commands()

    # Delete a record
  
    invoker.add_command(DeleteCommand(sales_db, "Sales", "year = 2004"))
    invoker.execute_commands()

    # Show remaining records
   
    invoker.add_command(RetrieveCommand(sales_db, "Sales"))
    invoker.execute_commands()

    # Complex query - Sales from 2009 onwards
   
    invoker.add_command(RetrieveCommand(sales_db, "Sales", "year >= 2009"))
    invoker.execute_commands()



if __name__ == "__main__":
    main()
    print("\n\n")
    sales_demonstration()