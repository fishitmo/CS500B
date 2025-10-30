
from real_estate_manager import RealEstateManager
from data_persisitence_factory import DataPersistenceFactory
from property_type import PropertyType
from property_status import PropertyStatus


class UserInterface:
    """Console-based menu-driven user interface"""
    
    def __init__(self):
        self.__manager = None
        self.__running = True
    
    def run(self):
        print("\n" + "="*70)
        print(" REAL ESTATE MANAGEMENT SYSTEM ")
       
        print("\nWelcome! Loading system...")
        
        # Initialize manager
        self.__manager = RealEstateManager()
        
        # Setup persistence
        persistence = DataPersistenceFactory.create_all_persistence()
        self.__manager.set_persistence_objects(
            persistence['property'],
            persistence['owner'],
            persistence['buyer']
        )
        
        print(" System initialized successfully!")
        
        while self.__running:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip()
            self.process_choice(choice)
    
    def display_menu(self):
        print("\n" + "-"*70)
        print(" MAIN MENU ".center(70))
        print("-"*70)
        print("\n--- PROPERTY MANAGEMENT ---")
        print("1.  Add New Property")
        print("2.  Update Property Information")
        print("3.  Delete Property")
        print("4.  Search Property by Owner Name")
        print("5.  View All Properties")
        
        print("\n--- OWNER MANAGEMENT ---")
        print("6.  List All Owners (Alphabetically)")
        
        print("\n--- BUYER MANAGEMENT ---")
        print("7.  Register New Buyer")
        print("8.  Add Buyer Interest to Property")
        print("9.  View Buyer Information")
        print("10. View Interested Buyers for a Property")
        
        print("\n--- DATA MANAGEMENT ---")
        print("11. Save All Data")
        
        print("\n--- SYSTEM ---")
        print("0.  Exit Application")
        print("-"*70)
    
    def process_choice(self, choice):
        if choice == '1':
            self.add_property_ui()
        elif choice == '2':
            self.update_property_ui()
        elif choice == '3':
            self.delete_property_ui()
        elif choice == '4':
            self.search_property_ui()
        elif choice == '5':
            self.view_all_properties_ui()
        elif choice == '6':
            self.list_owners_ui()
        elif choice == '7':
            self.add_buyer_ui()
        elif choice == '8':
            self.add_interest_ui()
        elif choice == '9':
            self.get_buyer_info_ui()
        elif choice == '10':
            self.show_interested_buyers_ui()
        elif choice == '11':
            self.save_data_ui()
        elif choice == '0':
            self.exit_application()
        else:
            print("\nInvalid choice! Please enter a number from 0 to 11.")
    
    def add_property_ui(self):
        print("\n" + "="*70)
        print(" ADD NEW PROPERTY ".center(70))
        print("="*70)
        
        try:
            address = input("Enter property address: ").strip()
            price = float(input("Enter property price ($): "))
            sqft = int(input("Enter square footage: "))
            beds = int(input("Enter number of bedrooms: "))
            owner_fname = input("Enter owner's first name: ").strip()
            owner_lname = input("Enter owner's last name: ").strip()
            
            print("\n--- Property Type ---")
            print("1. HOUSE")
            print("2. APARTMENT")
            print("3. CONDO")
            print("4. TOWNHOUSE")
            type_choice = input("Select property type (1-4): ").strip()
            
            property_types = {
                '1': PropertyType.HOUSE,
                '2': PropertyType.APARTMENT,
                '3': PropertyType.CONDO,
                '4': PropertyType.TOWNHOUSE
            }
            
            property_type = property_types.get(type_choice, PropertyType.HOUSE)
            
            self.__manager.add_property(address, price, sqft, beds, owner_fname, owner_lname, property_type)
            
            print("\n Property added successfully!")
            print(f"   Address: {address}")
            print(f"   Price: ${price:,.2f}")
            print(f"   Owner: {owner_fname} {owner_lname}")
            
        except ValueError as e:
            print(f"\n Error: {e}")
        except Exception as e:
            print(f"\n Error: {e}")
    
    def update_property_ui(self):
        print("\n" + "="*70)
        print(" UPDATE PROPERTY ".center(70))
        print("="*70)
        
        address = input("Enter property address to update: ").strip()
        
        print("\nWhat would you like to update?")
        print("1. Price")
        print("2. Status")
        
        choice = input("Enter choice: ").strip()
        
        try:
            if choice == '1':
                new_price = float(input("Enter new price: $"))
                if self.__manager.update_property(address, price=new_price):
                    print(f"\nPrice updated to ${new_price:,.2f}")
                else:
                    print("\nProperty not found!")
            elif choice == '2':
                print("\n1. AVAILABLE")
                print("2. PENDING")
                print("3. SOLD")
                print("4. WITHDRAWN")
                status_choice = input("Select status: ").strip()
                statuses = {
                    '1': PropertyStatus.AVAILABLE,
                    '2': PropertyStatus.PENDING,
                    '3': PropertyStatus.SOLD,
                    '4': PropertyStatus.WITHDRAWN
                }
                new_status = statuses.get(status_choice, PropertyStatus.AVAILABLE)
                if self.__manager.update_property(address, status=new_status):
                    print(f"\n Status updated to {new_status.value}")
                else:
                    print("\n Property not found!")
        except Exception as e:
            print(f"\n Error: {e}")
    
    def delete_property_ui(self):
        print("\n" + "="*70)
        print(" DELETE PROPERTY ".center(70))
        print("="*70)
        
        address = input("Enter property address to delete: ").strip()
        confirm = input(f"Are you sure you want to delete '{address}'? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            if self.__manager.delete_property(address):
                print(f"\n Property deleted successfully!")
            else:
                print(f"\n Property not found!")
        else:
            print("\n Deletion cancelled.")
    
    def search_property_ui(self):
        print("\n" + "="*70)
        print(" SEARCH BY OWNER NAME ".center(70))
        print("="*70)
        
        owner_name = input("Enter owner's name: ").strip()
        properties = self.__manager.search_by_name(owner_name)
        
        if properties:
            print(f"\n Found {len(properties)} property(ies)")
            for prop in properties:
                print(f"\n  Address: {prop.address}")
                print(f"  Price: ${prop.price:,.2f}")
                print(f"  Bedrooms: {prop.num_bedrooms}")
                print(f"  Type: {prop.property_type.value}")
        else:
            print("\n No properties found for this owner.")
    
    def view_all_properties_ui(self):
        print("\n" + "="*70)
        print(" ALL PROPERTIES ".center(70))
        print("="*70)
        
        properties = self.__manager.get_all_properties()
        
        if properties:
            print(f"\n Total Properties: {len(properties)}")
            for idx, prop in enumerate(properties, 1):
                print(f"\n{idx}. {prop.address}")
                print(f"   Price: ${prop.price:,.2f}")
                print(f"   {prop.num_bedrooms} bed, {prop.square_footage} sqft")
                print(f"   Owner: {prop.owner.full_name}")
                print(f"   Status: {prop.status.value}")
        else:
            print("\n No properties in the system.")
    
    def list_owners_ui(self):
        print("\n" + "="*70)
        print(" ALL OWNERS (ALPHABETICALLY) ".center(70))
        print("="*70)
        
        owners = self.__manager.get_all_sorted()
        
        if owners:
            print(f"\n Total Owners: {len(owners)}")
            for idx, owner in enumerate(owners, 1):
                print(f"\n{idx}. {owner.full_name}")
                print(f"   Properties: {owner.get_property_count()}")
        else:
            print("\n No owners in the system.")
    
    def add_buyer_ui(self):
        print("\n" + "="*70)
        print(" REGISTER NEW BUYER ".center(70))
        print("="*70)
        
        try:
            fname = input("Enter buyer's first name: ").strip()
            lname = input("Enter buyer's last name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            
            self.__manager.add_buyer(fname, lname, phone, email)
            
            print("\n Buyer registered successfully!")
            print(f"   Name: {fname} {lname}")
            print(f"   Phone: {phone}")
            print(f"   Email: {email}")
            
        except ValueError as e:
            print(f"\n Error: {e}")
    
    def add_interest_ui(self):
        print("\n" + "="*70)
        print(" ADD BUYER INTEREST ".center(70))
        print("="*70)
        
        buyer_name = input("Enter buyer's full name: ").strip()
        property_address = input("Enter property address: ").strip()
        
        if self.__manager.add_buyer_interest(buyer_name, property_address):
            print(f"\n Interest added successfully!")
        else:
            print(f"\n Buyer or property not found!")
    
    def get_buyer_info_ui(self):
        print("\n" + "="*70)
        print(" BUYER INFORMATION ".center(70))
        print("="*70)
        
        buyer_name = input("Enter buyer's full name: ").strip()
        buyer = self.__manager.get_buyer_info(buyer_name)
        
        if buyer:
            print(f"\n✓ Buyer Details:")
            print(f"   Name: {buyer.full_name}")
            print(f"   Phone: {buyer.phone_number}")
            print(f"   Email: {buyer.email}")
            
            properties = buyer.interested_properties
            if properties:
                print(f"\n   Interested Properties ({len(properties)}):")
                for prop in properties:
                    print(f"   • {prop.address} - ${prop.price:,.2f}")
            else:
                print(f"\n   No interested properties.")
        else:
            print(f"\n Buyer not found!")
    
    def show_interested_buyers_ui(self):
        print("\n" + "="*70)
        print(" INTERESTED BUYERS FOR PROPERTY ".center(70))
        print("="*70)
        
        property_address = input("Enter property address: ").strip()
        buyers = self.__manager.get_interested_buyers(property_address)
        
        if buyers:
            print(f"\n✓ Interested Buyers ({len(buyers)}):")
            for idx, buyer in enumerate(buyers, 1):
                print(f"\n{idx}. {buyer.full_name}")
                print(f"   Phone: {buyer.phone_number}")
                print(f"   Email: {buyer.email}")
        else:
            print(f"\n No interested buyers for this property.")
    
    def save_data_ui(self):
        print("\n" + "="*70)
        print(" SAVE DATA ".center(70))
        print("="*70)
        
        if self.__manager.save_all_data():
            print("\n All data saved successfully to CSV files!")
        else:
            print("\n Error saving data!")
    
    def exit_application(self):
        print("\n" + "="*70)
        
        save = input("Do you want to save data before exiting? (yes/no): ").strip().lower()
        
        if save == 'yes':
            self.__manager.save_all_data()
            print("\n Data saved successfully!")
        
        print("\nThank you for using Real Estate Management System!")
        print("Goodbye!")
        print("="*70 + "\n")
        self.running = False