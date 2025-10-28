import sys

class UserInterface:
    def __init__(self):
        self.__manager = None 
        self.__input_validator = None
        self.__display_foramtter = None
        self.__running = True
        
        
    def run(self):
        # Main entry point displays menu and processes user choices
        
        print("\n" + "="*60)
        print(f"{'Real Estate Management System':^60}")    
        print("="*60)
        
        while self.__running:
            try:
                self.display_menu()
                choice = input("\nEnter your choice: ").strip()
                self.process_choice(choice)
            except KeyboardInterrupt:
                print("\nOperation cancelled by user. Terminating program.")
                sys.exit()
            except EOFError:
                print("\nNo input received. Terminating program.")
                sys.exit()
            except Exception as e:
                # Catch-all to prevent crashes; log type and message
                print(type(e), e)
                print("Returning to main menu...")
            
    def display_menu(self):
        # Display the main menu options to the user
        print("-"*60)
        print(f"{'Main Menu':^60}")
        print("-"*60)
        print("\n---PROPERTY MANAGEMENT---")
        print("1. Add New Property")
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
        
        print("\n--- ADVANCED SEARCH ---")
        print("11. Advanced Property Search")
        
        print("\n--- DATA MANAGEMENT ---")
        print("12. Save All Data")
        print("13. Load All Data")
        
        print("\n--- SYSTEM ---")
        print("0.  Exit Application")
        print("-"*60)
        
    def process_choice(self, choice):
        """Process user's menu choice"""
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
            self.advanced_search_ui()
        elif choice == '12':
            self.save_data_ui()
        elif choice == '13':
            self.load_data_ui()
        elif choice == '0':
            self.exit_application()
        else:
            print("\nInvalid choice! Please enter a number from 0 to 13.")
            
    def add_property_ui(self):
        # user interface for adding a new property
        print("\n"+"="*60)
        print(f"{'ADD NEW PROPERTY':^60}")
        print("="*60)
        
        try:
            address = self.get_input("Enter property address: ")
            if not address:
                print("\nInvalid input. Address cannot be empty.")
                return

            price_str = self.get_input("Enter property price ($): ")
            try:
                price = float(price_str)
            except ValueError:
                print("\nInvalid float. Please enter a valid price.")
                return
            if price <= 0:
                print("\nPrice must be greater than 0.")
                return

            sqft_str = self.get_input("Enter square footage: ")
            try:
                sqft = int(sqft_str)
            except ValueError:
                print("\nInvalid integer. Please enter a whole number for square footage.")
                return
            if sqft <= 0:
                print("\nSquare footage must be greater than 0.")
                return

            beds_str = self.get_input("Enter number of bedrooms: ")
            try:
                beds = int(beds_str)
            except ValueError:
                print("\nInvalid integer. Please enter a whole number for bedrooms.")
                return
            if beds < 0:
                print("\nNumber of bedrooms cannot be negative.")
                return

            owner_fname = self.get_input("Enter owner's first name: ")
            if not owner_fname:
                print("\nOwner's first name cannot be empty.")
                return

            owner_lname = self.get_input("Enter owner's last name: ")
            if not owner_lname:
                print("\nOwner's last name cannot be empty.")
                return

            print("\n--- Property Type ---")
            print("1. HOUSE")
            print("2. APARTMENT")
            print("3. CONDO")
            print("4. TOWNHOUSE")
            type_choice = self.get_input("Select property type (1-4): ")

            property_types = {
                '1': 'HOUSE',
                '2': 'APARTMENT',
                '3': 'CONDO',
                '4': 'TOWNHOUSE'
            }

            property_type = property_types.get(type_choice, 'HOUSE')
            # Call manager to add property (will be implemented in business layer)
            # property = self.manager.add_property(address, price, sqft, beds, owner_fname, owner_lname, property_type)

            print("\nProperty added successfully!")
            print(f"   Address: {address}")
            print(f"   Price: ${price:,.2f}")
            print(f"   Square Footage: {sqft}")
            print(f"   Bedrooms: {beds}")
            print(f"   Owner: {owner_fname} {owner_lname}")
            print(f"   Type: {property_type}")

        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Returning to main menu.")
        except ValueError as e:
            # Specific value errors not caught above
            print("\nInvalid input.")
            print(type(e), 'message =', e)
        except Exception as e:
            # Catch-all for unforeseen errors
            print(type(e), 'message =', e)
            print("An unexpected error occurred while adding the property.")
        finally:
            pass
        
    def  update_property_ui(self):
        # user interface fot upaditing property inforamtion
        print("\n"+"="*60)
        print(f"{'UPDATE PROPERTY INFORMATION':^60}")
        print("="*60)
        
        try:
            address = self.get_input("Enter property address to update: ")
            if not address:
                print("\n Address cannot be empty!")
                return
            # Check if property exists (will use manager)
            # property = self.manager.get_property_by_address(address)
            
            print("\nWhat would you like to update?")
            print("1. Price")
            print("2. Square Footage")
            print("3. Number of Bedrooms")
            print("4. Property Status")
            print("5. Property Type")
            print("0. Cancel")
            
            update_choice = self.get_input("Select an option (0-5): ")
            
            if update_choice == '0':
                print("\nUpdate cancelled.")
                return
            
            elif update_choice == '1':
                new_price_str = self.get_input("Enter new price ($): ")
                new_price = float(new_price_str)
                if new_price <= 0:
                    print("\n Price must be greater than 0!")
                    return
                # self.manager.update_property(address, price=new_price)
                print(f"\n Property price updated to ${new_price:,.2f}")
                
            elif update_choice == '2':
                new_sqft = int(self.get_input("Enter new square footage: "))
                if new_sqft <= 0:
                    print("\n Square footage must be greater than 0!")
                    return
                # self.manager.update_property(address, square_footage=new_sqft)
                print(f"\n Property square footage updated to {new_sqft}")
                
            elif update_choice == '3':
                new_beds = int(self.get_input("Enter new number of bedrooms: "))
                if new_beds < 0:
                    print("\n Number of bedrooms cannot be negative!")
                    return
                # self.manager.update_property(address, num_bedrooms=new_beds)
                print(f"\n Property bedrooms updated to {new_beds}")
                
            elif update_choice == '4':
                print("\n--- Property Status ---")
                print("1. AVAILABLE")
                print("2. PENDING")
                print("3. SOLD")
                print("4. WITHDRAWN")
                status_choice = self.get_input("Select new status (1-4): ")
                statuses = {
                    '1': 'AVAILABLE',
                    '2': 'PENDING',
                    '3': 'SOLD',
                    '4': 'WITHDRAWN'
                }
                new_status = statuses.get(status_choice, 'AVAILABLE')
                # self.manager.update_property(address, status=new_status)
                print(f"\n Property status updated to {new_status}")
                
            elif update_choice == '5':
                print("\n--- Property Type ---")
                print("1. HOUSE")
                print("2. APARTMENT")
                print("3. CONDO")
                print("4. TOWNHOUSE")
                type_choice = self.get_input("Select property type (1-4): ")
                
                types = {
                    '1': 'HOUSE',
                    '2': 'APARTMENT',
                    '3': 'CONDO',
                    '4': 'TOWNHOUSE'
                }
                new_type = types.get(type_choice, 'HOUSE')
                # self.manager.update_property(address, property_type=new_type)
                print(f"\n Property type updated to {new_type}")
                
            else:
                print("\nInvalid choice! Please select a valid option.")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Returning to main menu.")
        except ValueError as e:
            print("\nInvalid input.")
            print(type(e), 'message =', e)
        except Exception as e:
            print(type(e), 'message =', e)
            print("An unexpected error occurred while updating the property.")
        finally:
            pass
        
    def delete_property_ui(self):
        # user interface for deleting a property
        print("\n"+"="*60)
        print(f"{'DELETE PROPERTY':^60}")
        print("="*60)
        
        try:
            address = self.get_input("Enter property address to delete: ")
            if not address:
                print("\n Address cannot be empty!")
                return
            
            if self.confirm_action(f"Are you sure you want to delete the property at '{address}'? ")
            # success = self.manager.delete_property(address)
                # if success:
                     print(f"\n Property at '{address}' has been deleted.")
                # else:
                #     print(f"\n No property found at '{address}'. Deletion failed.")
            else:
                print("\n Deletion cancelled.")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Returning to main menu.")
        except Exception as e:
            print(type(e), 'message =', e)
            print("An unexpected error occurred while deleting the property.")
        finally:
            pass    
        
    def search_property_ui(self):
        # User interface for searching property by owner name
        print("\n"+"="*60)
        print(f"{'SEARCH PROPERTY BY OWNER NAME':^60}")
        print("="*60)
        
        try:
            owner_name = self.get_input("Enter owner's full name (First Last) to search: ")
            if not owner_name:
                print("\n Owner name cannot be empty!")
                return
            # properties = self.manager.search_property_by_owner(owner_name)
            
            print(f"\n-- Properties owned by '{owner_name}': --")
            print("-"*60)
            
            # Simulated output - will be replaced with actual data
            print(f"\nNo properties for this owner.")
            # self.display_properties(properties)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Returning to main menu.")
        except Exception as e:
            print(type(e), 'message =', e)
            print("An unexpected error occurred while searching for properties.")
        finally:
            pass
        
    def view_all_properties_ui(self):
        # user interface for viewing all properties
        print("\n"+"="*60)
        print(f"{'VIEW ALL PROPERTIES':^60}")
        print("="*60)
        
        try:
            # properties = self.manager.get_all_properties()
            
            # Simmulate output 
            print("\n Total Properties: 0")
            print("-"*60)
            print(f"\nNo properties in the system.")
            # self.display_properties(properties)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Returning to main menu.")
        except Exception as e:
            print(type(e), 'message =', e)
            print("An unexpected error occurred while retrieving all properties.")
        finally:
            pass
    
    def list_owners_ui(self):
        # user interface for listing all owners alphabetically
        print("\n"+"="*60)
        print(f"{'LIST ALL OWNERS (ALPHABETICALLY)':^60}")
        print("="*60)
        
        try:
            # owners = self.manager.get_all_owners_alphabetically()
            
            # Simulate output
            print("\n Total Owners: 0")
            print("-"*60)

            print(f"\nNo owners in the system.")
            # Example of what will be displayed
            # for idx, owner in enumerate(owners, 1):
            #     print(f"\n{idx}. {owner.get_full_name()}")
            #     print(f"   Properties: {owner.get_property_count()}")
            
            
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Returning to main menu.")
        except Exception as e:
            print(type(e), 'message =', e)
            print("An unexpected error occurred while listing owners.")
        finally:
            pass
        
    def add_buyer_ui(self):
        # User interface for registering a new buyer 
        print("\n"+"="*60)
        print(f"{'REGISTER NEW BUYER':^60}")
        print("="*60)        
        try:
            fname = self.get_input("Enter buyer's first name: ")
            if not fname:
                print("\n First name cannot be empty!")
                return
            lname = self.get_input("Enter buyer's last name: ")
            if not lname:
                print("\n Last name cannot be empty!")
                return
            phone = self.get_input("Enter buyer's phone number: ")  
            if not phone:
                print("\n Phone number cannot be empty!")
                return
            email = self.get_input("Enter buyer's email address: ")
            if not email:
                print("\n Email address cannot be empty!")
                return
            # Validate email format
            if "@" not in email or "." not in email:
                print("\n Invalid email format!")
                return
            # buyer = self.manager.add_buyer(fname, lname, phone, email)
            print(f"\n Buyer '{fname} {lname}' registered successfully!")
            print(f"   Phone: {phone}")
            print(f"   Email: {email}")
        except KeyboardInterrupt:    
            print("\nOperation cancelled by user. Returning to main menu.")
        except ValueError as e:
            print("\nInvalid input.")
            print(type(e), 'message =', e)
        except Exception as e:
            print(type(e), 'message =', e)
            print("An unexpected error occurred while registering the buyer.")
        finally:
            pass    
    
    def add_interest_ui(self):
        pass
    
    def get_buyer_info_ui(self):
        pass
    
    def show_interested_buyers_ui(self):
        pass
    
    def advanced_search_ui(self):
        pass
    
    def save_data_ui(self):
        pass
    
    def load_data_ui(self):
        pass
    
    def exit_application(self):
        pass
    
    def get_input(self, prompt: str) -> str:
        # get user input with prompt
        def trim_whitespace(s: str) -> str:
            start = 0
            end = len(s) - 1
            while s[start] == ' ':
                start += 1
            while s[end] == ' ':
                end -= 1
            return s[start:end + 1]
        return trim_whitespace(input(prompt))
    
    def dispaly_properties(self, properties: list):
        pass
    
    def confirm_action(self, prompt: str) -> bool:
        pass
    
    
    


if __name__ == "__main__":
    print("\n" + "="*60)
    print(f"{'PRESENTATION LAYER - USER INTERFACE':^60}")
    print("="*60)
    
    print("This is the UserInterface class for the Presentation Layer.")
    print("="*60 + "\n")

    ui = UserInterface()
    
    # Display sample menu (without running the full application)
    print("\n--- SAMPLE MENU DISPLAY ---")
    ui.display_menu()