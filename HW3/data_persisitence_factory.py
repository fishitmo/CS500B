from csv_data_persistence import CSVDataPersistence
from idata_persistence import IDataPersistence
import os

class DataPersistenceFactory:
    
    
    # Class-level configuration (can be modified if needed)
    _DEFAULT_DATA_DIRECTORY = "D:/SFBU/CS500B/HW3/data"
    _DEFAULT_DELIMITER = ","
    _DEFAULT_ENCODING = "utf-8"
    
    # File names for different entities
    _PROPERTY_FILE = "properties.csv"
    _OWNER_FILE = "owners.csv"
    _BUYER_FILE = "buyers.csv"
    
    @classmethod
    def set_data_directory(cls, directory):
        
        if not directory:
            raise ValueError("Directory cannot be empty")
        cls._DEFAULT_DATA_DIRECTORY = directory.strip()
    
    @classmethod
    def get_data_directory(cls):
        
        return cls._DEFAULT_DATA_DIRECTORY
    
    @classmethod
    def set_default_delimiter(cls, delimiter):
        
        if not delimiter:
            raise ValueError("Delimiter cannot be empty")
        cls._DEFAULT_DELIMITER = delimiter
    
    @classmethod
    def get_default_delimiter(cls):
        
        return cls._DEFAULT_DELIMITER
    
    @classmethod
    def set_default_encoding(cls, encoding):
        
        if not encoding:
            raise ValueError("Encoding cannot be empty")
        cls._DEFAULT_ENCODING = encoding.strip()
    
    @classmethod
    def get_default_encoding(cls):
       
        return cls._DEFAULT_ENCODING
    
    @staticmethod
    def create_property_persistence():
        
        file_path = os.path.join(
            DataPersistenceFactory._DEFAULT_DATA_DIRECTORY,
            DataPersistenceFactory._PROPERTY_FILE
        )
        
        return CSVDataPersistence(
            file_path,
            delimiter=DataPersistenceFactory._DEFAULT_DELIMITER,
            encoding=DataPersistenceFactory._DEFAULT_ENCODING
        )
    
    @staticmethod
    def create_owner_persistence():
        
        file_path = os.path.join(
            DataPersistenceFactory._DEFAULT_DATA_DIRECTORY,
            DataPersistenceFactory._OWNER_FILE
        )
        
        return CSVDataPersistence(
            file_path,
            delimiter=DataPersistenceFactory._DEFAULT_DELIMITER,
            encoding=DataPersistenceFactory._DEFAULT_ENCODING
        )
    
    @staticmethod
    def create_buyer_persistence():
        
        file_path = os.path.join(
            DataPersistenceFactory._DEFAULT_DATA_DIRECTORY,
            DataPersistenceFactory._BUYER_FILE
        )
        
        return CSVDataPersistence(
            file_path,
            delimiter=DataPersistenceFactory._DEFAULT_DELIMITER,
            encoding=DataPersistenceFactory._DEFAULT_ENCODING
        )
    
    @staticmethod
    def create_persistence(persistence_type):
        
        persistence_type_lower = persistence_type.lower().strip()
        
        if persistence_type_lower == 'property' or persistence_type_lower == 'properties':
            return DataPersistenceFactory.create_property_persistence()
        elif persistence_type_lower == 'owner' or persistence_type_lower == 'owners':
            return DataPersistenceFactory.create_owner_persistence()
        elif persistence_type_lower == 'buyer' or persistence_type_lower == 'buyers':
            return DataPersistenceFactory.create_buyer_persistence()
        else:
            raise ValueError(f"Invalid persistence type: {persistence_type}. Must be 'property', 'owner', or 'buyer'")
    
    @staticmethod
    def create_custom_persistence(file_path, delimiter=None, encoding=None):
        
        # Manually choose delimiter and encoding without ternary expressions
        if delimiter is not None:
            actual_delimiter = delimiter
        else:
            actual_delimiter = DataPersistenceFactory._DEFAULT_DELIMITER

        if encoding is not None:
            actual_encoding = encoding
        else:
            actual_encoding = DataPersistenceFactory._DEFAULT_ENCODING
        
        return CSVDataPersistence(file_path, delimiter=actual_delimiter, encoding=actual_encoding)
    
    @staticmethod
    def create_all_persistence():
        
        return {
            'property': DataPersistenceFactory.create_property_persistence(),
            'owner': DataPersistenceFactory.create_owner_persistence(),
            'buyer': DataPersistenceFactory.create_buyer_persistence()
        }




if __name__ == "__main__":
    
    pass
    
    # print("TESTING DATAPERSISTENCEFACTORY CLASS ")
       
    
    # print("\nTesting Default Configuration:")
    
    # print(f"Default Data Directory: {DataPersistenceFactory.get_data_directory()}")
    # print(f"Default Delimiter: '{DataPersistenceFactory.get_default_delimiter()}'")
    # print(f"Default Encoding: {DataPersistenceFactory.get_default_encoding()}")
    
    # print("\nCreating Property Persistence:")
    
    # try:
    #     property_persistence = DataPersistenceFactory.create_property_persistence()
    #     print(f"Created property persistence")
    #     print(f"  Type: {type(property_persistence).__name__}")
    #     print(f"  Implements IDataPersistence: {isinstance(property_persistence, IDataPersistence)}")
    #     print(f"  File Path: {property_persistence.file_path}")
    #     print(f"  Delimiter: '{property_persistence.delimiter}'")
    # except Exception as e:
    #     print(f"Error: {e}")
    
    # print("\nCreating Owner Persistence:")
    
    # try:
    #     owner_persistence = DataPersistenceFactory.create_owner_persistence()
    #     print(f"Created owner persistence")
    #     print(f"  Type: {type(owner_persistence).__name__}")
    #     print(f"  Implements IDataPersistence: {isinstance(owner_persistence, IDataPersistence)}")
    #     print(f"  File Path: {owner_persistence.file_path}")
    #     print(f"  Delimiter: '{owner_persistence.delimiter}'")
    # except Exception as e:
    #     print(f"Error: {e}")
    
    # print("\nCreating Buyer Persistence:")
    
    # try:
    #     buyer_persistence = DataPersistenceFactory.create_buyer_persistence()
    #     print(f"Created buyer persistence")
    #     print(f"  Type: {type(buyer_persistence).__name__}")
    #     print(f"  Implements IDataPersistence: {isinstance(buyer_persistence, IDataPersistence)}")
    #     print(f"  File Path: {buyer_persistence.file_path}")
    #     print(f"  Delimiter: '{buyer_persistence.delimiter}'")
    # except Exception as e:
    #     print(f"Error: {e}")
    
    # print("\n Testing create_persistence() with Type String:")
    
    
    # try:
    #     prop_persist = DataPersistenceFactory.create_persistence('property')
    #     print(f" Created using 'property': {prop_persist.file_path}")
        
    #     owner_persist = DataPersistenceFactory.create_persistence('owner')
    #     print(f" Created using 'owner': {owner_persist.file_path}")
        
    #     buyer_persist = DataPersistenceFactory.create_persistence('buyer')
    #     print(f" Created using 'buyer': {buyer_persist.file_path}")
        
    #     # Test with plural forms
    #     props_persist = DataPersistenceFactory.create_persistence('properties')
    #     print(f" Created using 'properties': {props_persist.file_path}")
    # except Exception as e:
    #     print(f" Error: {e}")
    
    # print("\n Testing Invalid Persistence Type:")
  
    # try:
    #     invalid_persist = DataPersistenceFactory.create_persistence('invalid')
    #     print("ERROR: Should reject invalid type!")
    # except ValueError as e:
    #     print(f"Correctly rejected invalid type: {e}")
    
    # print("\nTesting create_all_persistence():")
    
    # try:
    #     all_persistence = DataPersistenceFactory.create_all_persistence()
    #     print(f"Created all persistence objects")
    #     print(f"  Keys: {list(all_persistence.keys())}")
    #     print(f"  Property file: {all_persistence['property'].file_path}")
    #     print(f"  Owner file: {all_persistence['owner'].file_path}")
    #     print(f"  Buyer file: {all_persistence['buyer'].file_path}")
    # except Exception as e:
    #     print(f"Error: {e}")
    
    # print("\nTesting Configuration Modification:")
    
    # print(f"Original directory: {DataPersistenceFactory.get_data_directory()}")
    
    # # Change configuration
    # DataPersistenceFactory.set_data_directory("custom_data")
    # print(f" Changed directory to: {DataPersistenceFactory.get_data_directory()}")
    
    # # Create new persistence with new config
    # new_prop_persist = DataPersistenceFactory.create_property_persistence()
    # print(f"  New property file path: {new_prop_persist.file_path}")
    
    # # Reset to original
    # DataPersistenceFactory.set_data_directory("D:/SFBU/CS500B/HW3/data")
    # print(f"Reset directory to: {DataPersistenceFactory.get_data_directory()}")
    
    # print("\n Testing Delimiter Configuration:")
    
    # print(f"Original delimiter: '{DataPersistenceFactory.get_default_delimiter()}'")
    
    
   
    

    
    # # print("\n\Testing Functional Usage with Factory:")
    
    
    # # Sample data
    # sample_properties = [
    #     {'address': '123 Main St', 'price': '250000', 'bedrooms': '3'},
    #     {'address': '456 Oak Ave', 'price': '350000', 'bedrooms': '4'}
    # ]
    
    # sample_owners = [
    #     {'full_name': 'John Smith', 'phone': '555-1234', 'email': 'john@email.com'},
    #     {'full_name': 'Jane Doe', 'phone': '555-5678', 'email': 'jane@email.com'}
    # ]
    
    # sample_buyers = [
    #     {'full_name': 'Alice Brown', 'phone': '555-9999', 'email': 'alice@email.com'},
    #     {'full_name': 'Bob Green', 'phone': '555-8888', 'email': 'bob@email.com'}
    # ]
    
    # try:
    #     # Create persistence objects using factory
    #     prop_persist = DataPersistenceFactory.create_property_persistence()
    #     owner_persist = DataPersistenceFactory.create_owner_persistence()
    #     buyer_persist = DataPersistenceFactory.create_buyer_persistence()
        
    #     # Save data
    #     prop_persist.save(sample_properties)
    #     print(f"Saved {len(sample_properties)} properties")
        
    #     owner_persist.save(sample_owners)
    #     print(f"Saved {len(sample_owners)} owners")
        
    #     buyer_persist.save(sample_buyers)
    #     print(f"Saved {len(sample_buyers)} buyers")
        
    #     # Load data
    #     loaded_properties = prop_persist.load()
    #     print(f"Loaded {len(loaded_properties)} properties")
        
    #     loaded_owners = owner_persist.load()
    #     print(f"Loaded {len(loaded_owners)} owners")
        
    #     loaded_buyers = buyer_persist.load()
    #     print(f"Loaded {len(loaded_buyers)} buyers")
        
    # except Exception as e:
    #     print(f"Error: {e}")
    
   
   
    
    
    
    # print("\nCleanup Test Files:")
    
    # test_files = [
    #     'D:/SFBU/CS500B/HW3/data/properties.csv',
    #     'D:/SFBU/CS500B/HW3/data/owners.csv',
    #     'D:/SFBU/CS500B/HW3/data/buyers.csv'
        
    # ]
    
    # for file_path in test_files:
    #     if os.path.exists(file_path):
    #         os.remove(file_path)
    #         print(f"✓ Removed {file_path}")
    
    # # Remove directories if empty
    # for directory in ['data', 'custom_data', 'custom_folder']:
    #     if os.path.exists(directory) and not os.listdir(directory):
            
    #         print(f"✓ Removed empty directory {directory}")