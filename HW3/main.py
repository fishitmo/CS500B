

from user_interface import UserInterface

def main():
  
    try:
        # Create and run the user interface
        ui = UserInterface()
        ui.run()
    except KeyboardInterrupt:
        print("\n\n Application interrupted by user.")
        print("Goodbye!")
    except Exception as e:
        print(f"\n\n Fatal Error: {e}")
        print("Please report this issue to the system administrator.")


if __name__ == "__main__":
    print(""" WELCOME TO REAL ESTATE LISTING MANAGEMENT APPLICATION """)
    
    # Run the application
    main()
    
    
