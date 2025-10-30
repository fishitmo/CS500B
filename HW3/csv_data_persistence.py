import csv
from idata_persistence import IDataPersistence
import os


class CSVDataPersistence(IDataPersistence):
    
    
    def __init__(self, file_path: str, delimiter=',', encoding='utf-8'):
       
        if not file_path:
            raise ValueError("File path cannot be empty")
        
        if not delimiter:
            raise ValueError("Delimiter cannot be empty")
        
        
        self.__file_path = file_path
        self.__delimiter = delimiter
        self.__encoding = encoding
        
        
    @property
    def file_path(self) -> str:
      
        return self.__file_path
    
    @property
    def delimiter(self) -> str:
      
        return self.__delimiter
    
    @property
    def encoding(self):
    
        return self.__encoding
    
    
    def save(self, data: list[dict]) -> bool:
 
        try:
            # Validate data
            if not isinstance(data, list):
                raise ValueError("Data must be a list")
            
            if len(data) == 0:
                # Empty data - create empty file with no headers
                with open(self.__file_path, 'w', newline='', encoding=self.__encoding) as file:
                    pass
                return True
            
            # Validate all items are dictionaries
            for item in data:
                if not isinstance(item, dict):
                    raise ValueError("All data items must be dictionaries")
            
            # Get all unique keys from all dictionaries 
            all_keys: list[str] = []
            for item in data:
                for key in item.keys():
                    if key not in all_keys:
                        all_keys.append(key)

            # sort keys
            fieldnames = all_keys[:]
            n = len(fieldnames)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if str(fieldnames[j]) > str(fieldnames[j + 1]):
                        fieldnames[j], fieldnames[j + 1] = fieldnames[j + 1], fieldnames[j]
            
            # Write to CSV file
            with open(self.__file_path, 'w', newline='', encoding=self.__encoding) as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=self.__delimiter)
                writer.writeheader()
                writer.writerows(data)
            
            return True
            
        except IOError as e:
            raise IOError(f"Failed to save data to {self.__file_path}: {str(e)}")
        except Exception as e:
            raise ValueError(f"Invalid data format: {str(e)}")
    
    def load(self):
     
        try:
           
            
            # Read from CSV file
            data = []
            with open(self.__file_path, 'r', newline='', encoding=self.__encoding) as file:
                reader = csv.DictReader(file, delimiter=self.__delimiter)
                for row in reader:
                    data.append(dict(row))
            
            return data
            
        except FileNotFoundError as e:
            raise e
        except IOError as e:
            raise IOError(f"Failed to load data from {self.__file_path}: {str(e)}")
        except Exception as e:
            raise IOError(f"Error reading CSV file: {str(e)}")
    
    def delete(self, identifier):
     
        try:
            # Load all data
            data = self.load()
            
            if len(data) == 0:
                return False
            
            
            identifier_field = None
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                for key in data[0]:
                    identifier_field = key
                    break
            
            if not identifier_field:
                return False
            
            
            original_length = len(data)
            i = 0
            while i < len(data):
                current = data[i]
                current_id = None
                if isinstance(current, dict):
                   
                    if identifier_field is not None and identifier_field in current:
                        current_id = current.get(identifier_field)
                if current_id == identifier:
                    data.pop(i)
                    
                else:
                    i += 1
            
            
            if len(data) == original_length:
                return False
            
            
            self.save(data)
            return True
            
        except Exception as e:
            raise IOError(f"Failed to delete record: {str(e)}")
    
    def update(self, identifier, updated_data):
        
        try:
            # Validate updated_data
            if not isinstance(updated_data, dict):
                raise ValueError("Updated data must be a dictionary")
            
            # Load all data
            data = self.load()
            
            if len(data) == 0:
                return False
            
            # Get the identifier field name (first key)
            identifier_field = None
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                for key in data[0]:
                    identifier_field = key
                    break
            
            if not identifier_field:
                return False
            
            # Find and update the record
            found = False
            for item in data:
                if item.get(identifier_field) == identifier:
                    item.update(updated_data)
                    found = True
                    break
            
            if not found:
                return False
            
            # Save updated data
            self.save(data)
            return True
            
        except ValueError as e:
            raise e
        except Exception as e:
            raise IOError(f"Failed to update record: {str(e)}")
    
    def exists(self, identifier):
        
        try:
            # Load all data
            data = self.load()
            
            if len(data) == 0:
                return False
            
            # Get the identifier field name (first key)
            identifier_field = None
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                for key in data[0]:
                    identifier_field = key
                    break
            
            if not identifier_field:
                return False
            
            # Check if identifier exists
            for item in data:
                if item.get(identifier_field) == identifier:
                    return True
            
            return False
            
        except Exception as e:
            raise IOError(f"Failed to check existence: {str(e)}")
    
    
    def __str__(self):
       
        return f"CSVDataPersistence(file='{self.__file_path}', delimiter='{self.__delimiter}', encoding='{self.__encoding}')"
    
    

if __name__ == "__main__":
    
    pass
    # print(" TESTING CSVDATAPERSISTENCE CLASS ")
    
    # # Test file path
    # test_file = "test_data.csv"
    
    # print("\nCreating CSVDataPersistence Instance:")
   
    # try:
    #     csv_persistence = CSVDataPersistence(test_file, delimiter=',', encoding='utf-8')
    #     print(f"CSVDataPersistence created successfully")
    #     print(csv_persistence)
    # except Exception as e:
    #     print(f"Error: {e}")
        
    # print("\n Verifying Interface Implementation:")
   
    # print(f"Implements IDataPersistence: {isinstance(csv_persistence, IDataPersistence)}")
    
    # print("\nTesting Getter Methods:")
    
    # print(f"File Path: {csv_persistence.file_path}")
    # print(f"Delimiter: '{csv_persistence.delimiter}'")
    # print(f"Encoding: {csv_persistence.encoding}")
    
    # print("\nTesting save() Method:")
    
    # # Sample property data
    # properties_data = [
    #     {
    #         'address': '123 Main Street',
    #         'price': '250000',
    #         'square_footage': '1800',
    #         'bedrooms': '3',
    #         'owner': 'John Smith',
    #         'type': 'HOUSE',
    #         'status': 'AVAILABLE'
    #     },
    #     {
    #         'address': '456 Oak Avenue',
    #         'price': '350000',
    #         'square_footage': '2200',
    #         'bedrooms': '4',
    #         'owner': 'Jane Doe',
    #         'type': 'TOWNHOUSE',
    #         'status': 'AVAILABLE'
    #     },
    #     {
    #         'address': '789 Pine Road',
    #         'price': '180000',
    #         'square_footage': '1200',
    #         'bedrooms': '2',
    #         'owner': 'Bob Johnson',
    #         'type': 'APARTMENT',
    #         'status': 'PENDING'
    #     }
    # ]
    
    # try:
    #     result = csv_persistence.save(properties_data)
    #     print(f"Saved {len(properties_data)} records to {test_file}")
    #     print(f"Save result: {result}")
    # except Exception as e:
    #     print(f"Error: {e}")
        
        
    # print("\n Testing load() Method:")
    
    # try:
    #     loaded_data = csv_persistence.load()
    #     print(f"Loaded {len(loaded_data)} records from {test_file}")
    #     print("\nLoaded data:")
    #     for idx, record in enumerate(loaded_data, 1):
    #         print(f"\n  Record {idx}:")
    #         for key, value in record.items():
    #             print(f"    {key}: {value}")
    # except Exception as e:
    #     print(f"Error: {e}")
        
        
    # print("\nTesting exists() Method:")
    
    # try:
    #     exists1 = csv_persistence.exists('123 Main Street')
    #     print(f"'123 Main Street' exists: {exists1}")
        
    #     exists2 = csv_persistence.exists('999 Non-Existent St')
    #     print(f"'999 Non-Existent St' exists: {exists2}")
    # except Exception as e:
    #     print(f"Error: {e}")
        
    
    # print("\nTesting update() Method:")
    
    
    # try:
    #     update_data = {
    #         'price': '240000',
    #         'status': 'SOLD'
    #     }
        
    #     result = csv_persistence.update('123 Main Street', update_data)
    #     print(f"Update result: {result}")
        
    #     # Verify update
    #     updated_records = csv_persistence.load()
    #     for record in updated_records:
    #         if record['address'] == '123 Main Street':
    #             print(f"\n  Updated record:")
    #             print(f"    Address: {record['address']}")
    #             print(f"    New Price: ${record['price']}")
    #             print(f"    New Status: {record['status']}")
    #             break
    # except Exception as e:
    #     print(f"Error: {e}")
        
        
    # print("\nTesting update() with Non-Existent Record:")
    
    # try:
    #     result = csv_persistence.update('999 Fake St', {'price': '999999'})
    #     print(f"Update non-existent record result: {result}")
    #     print(f"Correctly returned False for non-existent record")
    # except Exception as e:
    #     print(f"Error: {e}")
        
    
    # print("\nTesting delete() Method:")
    
    # try:
    #     print(f"Records before delete: {len(csv_persistence.load())}")
        
    #     result = csv_persistence.delete('789 Pine Road')
    #     print(f"Delete result: {result}")
        
    #     print(f"Records after delete: {len(csv_persistence.load())}")
        
    #     # Verify deletion
    #     still_exists = csv_persistence.exists('789 Pine Road')
    #     print(f"Record still exists: {still_exists}")
    # except Exception as e:
    #     print(f"Error: {e}")
        
    # print("\nTesting delete() with Non-Existent Record:")
    
    # try:
    #     result = csv_persistence.delete('999 Fake St')
    #     print(f"Delete non-existent record result: {result}")
    #     print(f"Correctly returned False for non-existent record")
    # except Exception as e:
    #     print(f"Error: {e}")
        
    
    # print("\nTesting with Different Delimiter:")
    
    # pipe_file = "test_data_pipe.csv"
    # try:
    #     pipe_persistence = CSVDataPersistence(pipe_file, delimiter='|')
    #     print(f"Created CSV persistence with pipe delimiter")
        
    #     pipe_persistence.save(properties_data[:2])
    #     print(f"Saved data with pipe delimiter")
        
    #     loaded = pipe_persistence.load()
    #     print(f"Loaded {len(loaded)} records with pipe delimiter")
        
    #     #Clean up
    #     if os.path.exists(pipe_file):
    #         os.remove(pipe_file)
    # except Exception as e:
    #     print(f"Error: {e}")
        
        
    # print("\nTesting Invalid Data Handling:")
    
    
    
    # try:
    #     csv_persistence.save("not a list")
    #     print("ERROR: Should reject non-list data!")
    # except ValueError as e:
    #     print(f"Correctly rejected non-list data: {str(e)[:50]}")
    
    # # Non-dict items
    # try:
    #     csv_persistence.save([1, 2, 3])
    #     print("ERROR: Should reject non-dict items!")
    # except ValueError as e:
    #     print(f"Correctly rejected non-dict items: {str(e)[:50]}")
    
    # # Non-dict update data
    # try:
    #     csv_persistence.update('123 Main Street', "not a dict")
    #     print("ERROR: Should reject non-dict update data!")
    # except ValueError as e:
    #     print(f"Correctly rejected non-dict update: {str(e)[:50]}")
        
        
    # print("\nTesting __str__ :")
    # print(f"str(csv_persistence):  {str(csv_persistence)}")
   
    
    # print("\nViewing Actual CSV File Content:")
  
    # if os.path.exists(test_file):
    #     print(f"Content of {test_file}:")
        
    #     with open(test_file, 'r') as f:
    #         content = f.read()
    #         print(content)
        
        
    # print("\nCleaning Up Test Files:")
   
    # if os.path.exists(test_file):
    #     os.remove(test_file)
    #     print(f"Removed {test_file}")
    

