
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name,  contact_number, email, address) -> None:
    
        self.__name = name
        self.__contact_number = contact_number
        self.__email = email
        self.__address = address
    @property
    def name(self):
        return self.__name
    
    @property
    def contact_number(self):
        return self.__contact_number
    
    @property
    def email(self):
        return self.__email
    
    @property
    def address(self):
        return self.__address
    
    @name.setter
    def name(self, value):
        self.__name = value
    @email.setter
    def email(self, value):
        # set the person's email with validation 
        if not value or '@' not in value or '.' not in value:
            raise ValueError("Please provide a valid email address (e.g, user@example.com)")
        self.__email = value.strip().lower()
   
    def get_personal_info(self) -> str:
        
        return f"Name: {self.__name}\nContact Number: {self.__contact_number}\nEmail: {self.__email}\nAddress: {self.__address}"
    
    def update_contact(self, new_contact_number, new_email):
        # update the person's contact number and email
        self.__contact_number = new_contact_number
        self.email = new_email
    @abstractmethod
    def get_full_info(self) -> str:
        """
        abstract method to get complete information
        must be implemented by concrete subclasses.
        
        Returns: 
            str: Complete information specific to the subclass.
        """
        pass
    
    def __str__(self) -> str:
        return f"Person(name ='{self.__name}', email = '{self.__email}')"
    
    def __repr__(self) -> str:
        return f"Person(name ='{self.__name}', conact_number = '{self.__contact_number}',email = '{self.__email}', address = '{self.__address}')"
        
    
    def __eq__(self, other):
        
        if not isinstance(other, Person):
            return False
        return self.__email == other.__email
    
class  Applicant(Person):
    
    
    def __init__(self, name, contact_number, email, address) -> None:
        super().__init__(name, contact_number, email, address)
        
    
    def get_full_info(self) -> str:
        
        
        """
        Implementaion of abstract method from Person class.
        Returns complete application information.
        """
        
        return self.get_personal_info()
    
    def __str__(self) -> str:
        return f"Application(name ='{self.name}', email = '{self.email}')"
    
    def __repr__(self) -> str:
        return f"Application('{self.name}', '{self.contact_number}','{self.email}', '{self.address}')"
    
    
from datetime import datetime

class Education:
    
    """
    class representing a single education record.
    Each applicant can have multiple education entries (high school, undergraduate, graduate, etc.) 
    """
    
    def __init__(self, institution, degree_level, year_completed):
        
        self.__institution = institution
        self.__degree_level = degree_level
        self.__year_completed = year_completed
        self.__validate_year(year_completed)
    
    @property
    def institution(self):
        return self.__institution
    
    @property
    def degree_level(self):
        return self.__degree_level
    @property
    def year_completed(self):
        return self.__year_completed
    
    @year_completed.setter
    def year_completed(self, value):
        self.__validate_year(value)
        self.__year_completed = value
        
        
    def __validate_year(self, year):
        # private method to validate the year
        
        current_year = datetime.now().year
        
        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")
        
        if year < 1950 or year > current_year +5:
            raise ValueError(f"Year must be between 1950 and {current_year +5}.")
        
    def get_education_info(self) -> str:
        return f"{self.__degree_level} from {self.__institution}, completed in {self.__year_completed}"
    
    def is_completed(self) -> bool:
        # check if the education record is complete
        return self.__year_completed <= datetime.now().year
    
    def __str__(self) -> str:
        return f"Education(institution ='{self.__institution}', degree_level = '{self.__degree_level}', year_completed = '{self.__year_completed}')"
    
    def __repr__(self) -> str:
        return f"Education('{self.__institution}', '{self.__degree_level}', '{self.__year_completed}')"
    
    def __eq__(self, other):
        
        if not isinstance(other, Education):
            return False
        return (self.__year_completed == other.__year_completed and        
               self.__degree_level.lower() == other.__degree_level.lower() and 
               self.__institution.lower() == other.__institution.lower())
        
        

class ExtraCurricular:
    
    """
    class representing a single extracurricular activity.
    Each applicant can have multiple extracurricular entries  
    """
    
    def __init__(self, activity_name, description) -> None:
        
        self.__activity_name = activity_name
        self.__description = description
        
        
        
    
    @property
    def activity_name(self):
        return self.__activity_name
    
    @property
    def description(self):
        return self.__description
   
    def get_activity_info(self) -> str:
        return f"Activity: {self.__activity_name}\nDescription: {self.__description}"
    
    def __str__(self) -> str:
        return f"{self.__activity_name}"
    
    def __repr__(self) -> str:
        return f"ExtraCurricular('{self.__activity_name}', '{self.__description}')"
    
    def __eq__(self, other):
        
        if not isinstance(other, ExtraCurricular):
            return False
        return self.__activity_name.lower() == other.__activity_name.lower() and self.__description.lower() == other.__description.lower()
    

from enum import Enum

class ApplicationStatus(Enum):
    
    """
    Enumeration representing the possible states of an admission application.
    provides a controled set of valid status values. 
    """
    
    PENDING = "Pending"
    REVIEWED = "Reviewed" 
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    
    def __str__(self):
        return self.value
    
    def can_transition_to(self, new_status) -> bool:
        # define valid transitions
        allowed_transitions = {
            ApplicationStatus.PENDING: [ApplicationStatus.REVIEWED], 
            ApplicationStatus.REVIEWED: [ApplicationStatus.ACCEPTED, ApplicationStatus.REJECTED],
            ApplicationStatus.ACCEPTED: [],
            ApplicationStatus.REJECTED: []
        }
        return new_status in allowed_transitions.get(self, [])
    def is_final_status(self) -> bool:
        return self in [ApplicationStatus.ACCEPTED, ApplicationStatus.REJECTED]
    

class Application:
    
    def __init__(self, application_id: str, name: str, conatact_number: str, email: str, address: str, program_applied_for: str) -> None:
        self.__application_id = application_id
        self.__program_applied_for = program_applied_for
        self.__application_date = datetime.now()
        self._status = ApplicationStatus.PENDING # protected attribute
        
        self.__applicant = Applicant(name, conatact_number, email, address) # composition
        self.__educations = []
        self.__extracurriculars = []
        
    @property
    def application_id(self) -> str:
        return self.__application_id
        
    @property
    def program_applied_for(self) -> str:
        return self.__program_applied_for
    @property
    def applicant(self) -> Applicant:
        return self.__applicant
        
    @property
    def application_date(self) -> datetime:
        return self.__application_date
    @property
    def status(self) -> ApplicationStatus:
        return self._status
        
    @status.setter
    def status(self, new_status):
        if not isinstance(new_status, ApplicationStatus):
            raise ValueError("Status must be an ApplicationStatus enum value.")
        if not self._status.can_transition_to(new_status):
            raise ValueError(f"Can not transition from {self._status} to {new_status}.")
        self._status = new_status
        
    def add_education(self, institution, degree_level, year_completed):
        
        """
        add an education reacord by creating Educatioon object internally.
        """
        education = Education(institution, degree_level, year_completed)  # compostion
        
        if education not in self.__educations:
            self.__educations.append(education)
        else:
            raise ValueError("Duplicate education record.")
    
    def remove_education(self, institution, degree_level, year_completed):
        
        """
        remove an education record by matching criteria.
        
        """    
        education_to_remove = Education(institution, degree_level, year_completed)  # compostion
        
        if education_to_remove in self.__educations:
            i = 0
            while i < len(self.__educations):
                if self.__educations[i] == education_to_remove:
                    self.__educations[i] = self.__educations[-1]
                    self.__educations.pop()
                    break
                i += 1
        else:
            raise ValueError("No matching education record found.")
        

    def add_extracurricular(self, activity_name, description):
        
        """
        add an extracurricular activity by creating ExtraCurricular object internally.
        """ 
        extracurricular = ExtraCurricular(activity_name, description)  # compostion
        
        if extracurricular not in self.__extracurriculars:
            self.__extracurriculars.append(extracurricular)
        else:
            raise ValueError("Duplicate extracurricular record.")
        
    def remove_extracurricular(self, activity_name, description):
        
        """
        remove an extracurricular activity by matching criteria.
        """    
        extracurricular_to_remove = ExtraCurricular(activity_name, description)  # compostion
        
        if extracurricular_to_remove in self.__extracurriculars:
            i = 0
            while i < len(self.__extracurriculars):
                if self.__extracurriculars[i] == extracurricular_to_remove:
                    self.__extracurriculars[i] = self.__extracurriculars[-1]
                    self.__extracurriculars.pop()
                    break
                i += 1
        else:
            raise ValueError("No matching extracurricular record found.")
        
    def get_application_summary(self):
        
        """
        Get the summary of the application
        """
        
        return f"Application Summary:\nID: {self.__application_id}\nApplicant: {self.__applicant.name}\nProgram: {self.__program_applied_for}\nStatus: {self._status}\nApplied: {self.__application_date.strftime('%m-%d-%Y')}\nEducation Records: {len(self.__educations)}\nExtracurricular Activities: {len(self.__extracurriculars)}"
    
    
    def get_full_application(self):
        
        """
        get complete application details.
        """
        result = self.get_application_summary()
        result += "\n\n" + "="*50
        
        # applicant details
        result += "\n\nAPPLICATION INFORMATION\n"
        result += self.__applicant.get_personal_info()
        
        # Education details
        result += "\n\nEDUCATION HISTORY\n"
        if self.__educations:
            for education in self.__educations:
                result += f"\n  {education.get_education_info()}\n"
        else:
            result += "No education records provided.\n"
        
        # extracurricular details
        result += "\n\nEXTRACURRICULAR ACTIVITIES\n"
        if self.__extracurriculars:
            for extracurricular in self.__extracurriculars:
                result += f"\n  {extracurricular.get_activity_info()}\n"
        else:
            result += "No extracurricular activities provided.\n"
        
        
        return result
    
    def __str__(self):
        return f"Application({self.__applicant.name} --> {self.__program_applied_for}) [{self._status}]"
    
    def __repr__(self):
        return f"Application('{self.__application_id}', '{self.__applicant.name}', '{self.__program_applied_for}, '{self._status}')"
           
    def __eq__(self, other):
        
        # check equality based on application ID
        
        if not isinstance(other, Application):
            return False
        return self.__application_id == other.__application_id
    
    
           
class AdmissionSystem:
    
    """
    main system class that manages all admission applications. 
    
    """         
    def __init__(self):
        self.__applications = []
        self.__next_id = 1
    
    def __generate_application_id(self):
        
        # generate a unique application ID
        app_id = f"APP-{self.__next_id:03d}"
        self.__next_id += 1
        return app_id
    
    def add_application(self, application) -> bool:
        
        # add existing application to the system
        if not isinstance(application, Application):
            raise ValueError("Must provide an Application object")
        
        if self.get_application_by_id(application.application_id):
            print(f"Application with ID {application.application_id} already exists")
            return False
        self.__applications.append(application)
        return True
      
    def get_application_by_id(self, application_id):
        
        # find application by ID
        for app in self.__applications:
            if app.application_id == application_id:
                return app
        return None
    
    def search_applications(self, search_type, search_value):
        
        # search application based on criteria
        results = []
        search_value_lower = search_value.lower()
        
        for app in self.__applications:
            if search_type == "name" and search_value_lower in app.applicant.name.lower():
                results.append(app)
            elif search_type == "email" and search_value_lower in app.applicant.email.lower():
                results.append(app)
            elif search_type == "program" and search_value_lower in app.program_applied_for.lower():
                results.append(app)
            elif search_type == "status" and search_value_lower == str(app.status).lower():
                results.append(app)
                
        return results
    
    def update_application_status(self, application_id, new_status) -> bool:
        
        # update application status
        application = self.get_application_by_id(application_id)
        if application:
            try:
                application.status = new_status
                return True
            except ValueError as ve:
                print(f"Status update failed: {ve}")
                return False
        return False
    
    def get_applications_summary(self):
        
        # get summary statistics of applications
        summary = {
            "total": len(self.__applications),
            "pending": 0,
            "reviewed": 0,
            "accepted": 0,
            "rejected": 0
        }
        for app in self.__applications:
            status_str = str(app.status).lower()
            if status_str in summary:
                summary[status_str] += 1
        
        return summary
    def delete_application_by_id(self, application_id):
        
        # remove application from the system by ID
        
        application = self.get_application_by_id(application_id)
        
        if application:
            i = 0
            while i < len(self.__applications):
                if self.__applications[i].application_id == application_id:
                    self.__applications[i] = self.__applications[-1]
                    self.__applications.pop()
                    return True
                i += 1
        return False
    
    def display_all_applications(self):
        
        # dispaly summary of all applications 
        
        if not self.__applications:
            return "No applications found in the system."       
        
        result = f"TOTAL APPLICATIONS: {len(self.__applications)}\n"
        result += "=" * 60 + "\n"
        
        for app in self.__applications:
            result += f"ID: {app.application_id} | "
            result += f"Name: {app.applicant.name} | "
            result += f"Program: {app.program_applied_for} | "
            result += f"Status: {app.status}\n"
        
        return result
    
    def get_applications_by_status(self, status):
        
        # get all aplications with specific status
        result = []
        for app in self.__applications:
            if app.status == status:
                result.append(app)
        return result
    
    def get_total_applications(self):
        
        # get total number of applications
        return len(self.__applications)
    
    def update_personal_info(self, application_id, name=None, contact_number=None, email=None, address=None):
        
        # update personal info of an application
        application = self.get_application_by_id(application_id)
        if application:
            if name:
                application.applicant.name = name
            if contact_number:
                application.applicant.contact_number = contact_number
            if email:
                application.applicant.email = email
            if address:
                application.applicant.address = address
            return True
        return False
    
    def add_education_to_application(self, application_id, institution, degree_level, year_completed):
        
        # add education record to an existing application
        
        application = self.get_application_by_id(application_id)
        if application:
            application.add_education(institution, degree_level, year_completed)
            return True
        return False
    
    def remove_education_from_application(self, application_id, institution, degree_level, year_completed):
        
        # remove education record from an existing application
        
        application = self.get_application_by_id(application_id)
        if application:
           application.remove_education(institution, degree_level, year_completed)
           return True
        return False
    
    def add_extracurricular_to_application(self, application_id, activity_name, description):
        
        # add extracurricular activity to an existing application 
        
        application = self.get_application_by_id(application_id)
        if application:
            application.add_extracurricular(activity_name, description)
            return True
        return False
    
    def remove_extracurricular_from_application(self, application_id, activity_name, description):
        
        # remove extracurricular activity from an existing application 
        
        application = self.get_application_by_id(application_id)
        if application:
            application.remove_extracurricular(activity_name, description)
            return True
                
        return False
    
    def create_application(self, name, contact_number, email, address, program_applied_for):
        """
        Helper method to create and add application in one step.
        Creates Application externally, then adds it to system.

        """
        app_id = self.__generate_application_id()
        application = Application(app_id, name, contact_number, email, address, program_applied_for)
        self.add_application(application)
        return application





class MenuInterface:
    """
    User interface class for the Admission Application System.
    Provides menu-driven interaction for administrators.
    """
    
    def __init__(self):
        """Initialize the menu interface with an admission system."""
        self.system = AdmissionSystem()
    
    def display_main_menu(self):
        """Display the main menu options."""
        print("\n" + "="*60)
        print("ADMISSION APPLICATION SYSTEM".center(60))
        print("="*60)
        print("1. Add New Application")
        print("2. Search Applications")
        print("3. Update Application")
        print("4. Delete Application")
        print("5. Display All Applications")
        print("6. Display Application Details")
        print("7. Get System Summary")
        print("8. Exit")
        print("="*60)
    
    def get_input(self, prompt):
        """
        Get user input with a prompt.
        
        """
        return input(prompt).strip()
    
    def add_application_menu(self):
        """Menu for adding a new application."""
        print("\n--- ADD NEW APPLICATION ---")
        
        # Get applicant information
        name = self.get_input("Enter applicant name: ")
        contact = self.get_input("Enter contact number: ")
        email = self.get_input("Enter email address: ")
        address = self.get_input("Enter address: ")
        program = self.get_input("Enter program applied for: ")
        
        # Generate ID and create application
        app_id = f"APP-{self.system.__next_id:03d}"
        self.system.__next_id += 1
        
        try:
            application = Application(app_id, name, contact, email, address, program)
            
            # Add education records
            print("\n--- ADD EDUCATION RECORDS ---")
            while True:
                add_edu = self.get_input("Add education record? (y/n): ").lower()
                if add_edu != 'y':
                    break
                
                institution = self.get_input("Institution name: ")
                degree = self.get_input("Degree/Level: ")
                year = int(self.get_input("Year completed: "))
                application.add_education(institution, degree, year)
                print("Education record added!")
            
            # Add extracurricular activities
            print("\n--- ADD EXTRACURRICULAR ACTIVITIES ---")
            while True:
                add_activity = self.get_input("Add extracurricular activity? (y/n): ").lower()
                if add_activity != 'y':
                    break
                
                activity_name = self.get_input("Activity name: ")
                description = self.get_input("Description: ")
                application.add_extracurricular(activity_name, description)
                print("Activity added!")
            
            # Add to system
            self.system.add_application(application)
            print(f"\n✓ Application {app_id} added successfully!")
            
        except Exception as e:
            print(f"\n✗ Error adding application: {e}")
    
    def search_applications_menu(self):
        """Menu for searching applications."""
        print("\n--- SEARCH APPLICATIONS ---")
        print("1. Search by Name")
        print("2. Search by Email")
        print("3. Search by Program")
        print("4. Search by Status")
        
        choice = self.get_input("Enter choice (1-4): ")
        
        search_type = ""
        if choice == "1":
            search_type = "name"
        elif choice == "2":
            search_type = "email"
        elif choice == "3":
            search_type = "program"
        elif choice == "4":
            search_type = "status"
        else:
            print("Invalid choice!")
            return
        
        search_value = self.get_input(f"Enter {search_type} to search: ")
        
        results = self.system.search_applications(search_type, search_value)
        
        if results:
            print(f"\nFound {len(results)} application(s):")
            for app in results:
                print(f"  - ID: {app.application_id} | Name: {app.applicant.name} | Program: {app.program_applied_for} | Status: {app.status}")
        else:
            print("\nNo applications found.")
    
    def update_application_menu(self):
        """Menu for updating application details."""
        print("\n--- UPDATE APPLICATION ---")
        app_id = self.get_input("Enter Application ID: ")
        
        application = self.system.get_application_by_id(app_id)
        if not application:
            print(f"Application {app_id} not found!")
            return
        
        print("\nWhat would you like to update?")
        print("1. Personal Information")
        print("2. Application Status")
        print("3. Add Education")
        print("4. Remove Education")
        print("5. Add Extracurricular")
        print("6. Remove Extracurricular")
        
        choice = self.get_input("Enter choice (1-6): ")
        
        if choice == "1":
            self.update_personal_info(app_id)
        elif choice == "2":
            self.update_status(app_id)
        elif choice == "3":
            self.add_education(app_id)
        elif choice == "4":
            self.remove_education(app_id)
        elif choice == "5":
            self.add_extracurricular(app_id)
        elif choice == "6":
            self.remove_extracurricular(app_id)
        else:
            print("Invalid choice!")
    
    def update_personal_info(self, app_id):
        """Update personal information."""
        print("\n--- UPDATE PERSONAL INFORMATION ---")
        print("(Leave blank to keep current value)")
        
        name = self.get_input("New name: ")
        contact = self.get_input("New contact number: ")
        email = self.get_input("New email: ")
        address = self.get_input("New address: ")
        
        success = self.system.update_personal_info(
            app_id,
            name if name else None,
            contact if contact else None,
            email if email else None,
            address if address else None
        )
        
        if success:
            print("✓ Personal information updated successfully!")
        else:
            print("✗ Update failed!")
    
    def update_status(self, app_id):
        """Update application status."""
        print("\n--- UPDATE APPLICATION STATUS ---")
        print("Available statuses:")
        print("1. Pending")
        print("2. Reviewed")
        print("3. Accepted")
        print("4. Rejected")
        
        choice = self.get_input("Enter status choice (1-4): ")
        
        status_map = {
            "1": ApplicationStatus.PENDING,
            "2": ApplicationStatus.REVIEWED,
            "3": ApplicationStatus.ACCEPTED,
            "4": ApplicationStatus.REJECTED
        }
        
        if choice in status_map:
            success = self.system.update_application_status(app_id, status_map[choice])
            if success:
                print("✓ Status updated successfully!")
            else:
                print("✗ Status update failed!")
        else:
            print("Invalid choice!")
    
    def add_education(self, app_id):
        """Add education record."""
        print("\n--- ADD EDUCATION RECORD ---")
        institution = self.get_input("Institution name: ")
        degree = self.get_input("Degree/Level: ")
        year = int(self.get_input("Year completed: "))
        
        success = self.system.add_education_to_application(app_id, institution, degree, year)
        if success:
            print("✓ Education record added!")
        else:
            print("✗ Failed to add education!")
    
    def remove_education(self, app_id):
        """Remove education record."""
        print("\n--- REMOVE EDUCATION RECORD ---")
        institution = self.get_input("Institution name: ")
        degree = self.get_input("Degree/Level: ")
        year = int(self.get_input("Year completed: "))
        
        success = self.system.remove_education_from_application(app_id, institution, degree, year)
        if success:
            print("✓ Education record removed!")
        else:
            print("✗ Failed to remove education!")
    
    def add_extracurricular(self, app_id):
        """Add extracurricular activity."""
        print("\n--- ADD EXTRACURRICULAR ACTIVITY ---")
        activity = self.get_input("Activity name: ")
        description = self.get_input("Description: ")
        
        success = self.system.add_extracurricular_to_application(app_id, activity, description)
        if success:
            print("✓ Activity added!")
        else:
            print("✗ Failed to add activity!")
    
    def remove_extracurricular(self, app_id):
        """Remove extracurricular activity."""
        print("\n--- REMOVE EXTRACURRICULAR ACTIVITY ---")
        activity = self.get_input("Activity name: ")
        description = self.get_input("Description: ")
        
        success = self.system.remove_extracurricular_from_application(app_id, activity, description)
        if success:
            print("✓ Activity removed!")
        else:
            print("✗ Failed to remove activity!")
    
    def delete_application_menu(self):
        """Menu for deleting an application."""
        print("\n--- DELETE APPLICATION ---")
        app_id = self.get_input("Enter Application ID to delete: ")
        
        application = self.system.get_application_by_id(app_id)
        if not application:
            print(f"Application {app_id} not found!")
            return
        
        confirm = self.get_input(f"Delete application {app_id} ({application.applicant.name})? (y/n): ").lower()
        if confirm == 'y':
            removed = self.system.delete_application_by_id(app_id)
            if removed:
                print(f"✓ Application {app_id} deleted successfully!")
            else:
                print("✗ Deletion failed!")
        else:
            print("Deletion cancelled.")
    
    def display_all_menu(self):
        """Display all applications."""
        print("\n--- ALL APPLICATIONS ---")
        print(self.system.display_all_applications())
    
    def display_details_menu(self):
        """Display detailed application information."""
        print("\n--- APPLICATION DETAILS ---")
        app_id = self.get_input("Enter Application ID: ")
        
        application = self.system.get_application_by_id(app_id)
        if application:
            print("\n" + application.get_full_application())
        else:
            print(f"Application {app_id} not found!")
    
    def display_summary_menu(self):
        """Display system summary."""
        print("\n--- SYSTEM SUMMARY ---")
        summary = self.system.get_applications_summary()
        
        print(f"Total Applications: {summary['total']}")
        print(f"Pending: {summary['pending']}")
        print(f"Reviewed: {summary['reviewed']}")
        print(f"Accepted: {summary['accepted']}")
        print(f"Rejected: {summary['rejected']}")
    
    def run(self):
        """Main loop to run the menu interface."""
        print("\nWelcome to the Admission Application System!")
        
        while True:
            self.display_main_menu()
            choice = self.get_input("Enter your choice (1-8): ")
            
            if choice == "1":
                self.add_application_menu()
            elif choice == "2":
                self.search_applications_menu()
            elif choice == "3":
                self.update_application_menu()
            elif choice == "4":
                self.delete_application_menu()
            elif choice == "5":
                self.display_all_menu()
            elif choice == "6":
                self.display_details_menu()
            elif choice == "7":
                self.display_summary_menu()
            elif choice == "8":
                print("\nThank you for using the Admission Application System!")
                print("Goodbye!")
                break
            else:
                print("\n✗ Invalid choice! Please enter 1-8.")


    
def main():
    
#     applicant = Applicant(
#         name = "John Doe",
#         contact_number = "123-456-7890",
#         email = "WQyHs@example.com",
#         address = "123 Main St, Anytown, USA"
#     )
#    # test the methods
#     print("---- Appliant Testing----")
#     print("String reprsentation:", applicant)
#     print("Developer reprsentation:", repr(applicant))
    
#     print("\n--PERSONAL INFO--")
#     print(applicant.get_personal_info())
    
#     print("\n--FULL INFO--")
#     print(applicant.get_full_info())
    
#     print("\n--PROPERTY ACCESS--")
#     print("Name:", applicant.name)
#     print("email:", applicant.email)
    
#     print("\n--Email Validation Test--")
#     # try:
#     #     applicant.email = "newemail@example.com"
#     #     print("Updated email:", applicant.email)    
#     # except ValueError as ve:
#     #     print("Error:", ve)
#     try:
#         applicant.email = "invalidemail"
#         print("Updated email:", applicant.email)
#     except ValueError as ve:
#         print("Error:", ve)

    # print("\n---- EDUCATION CLASS TESTING ----")
    
    # # create education records
    # high_school = Education("Anytown High School", "High School Diploma", 2010)
    # bachelor = Education("State University", "Bachelor's Degree in Computer Science", 2014)
    
    # print("Education 1: ", high_school)
    # print("Education 2: ", bachelor)
    
    # print("\n -- DETAILED INFORMATION --")
    # print(high_school.get_education_info())
    # print()
    # print(bachelor.get_education_info())
    
    # print("\n-- COMPLETION STATUS --")
    # print(f"High School Completed: {high_school.is_completed()}")
    # print(f"Bachelor  Completed: {bachelor.is_completed()}")
    
    # print("\n-- PROPERTY ACCESS --")
    # print(f"Institution: {bachelor.institution}")
    # print(f"Degree : {bachelor.degree_level}")
    # print(f"Year: {bachelor.year_completed}")
    
    # print("\n-- VALIDATION TESTING --")
    
    # # try: 
    # #     future_eduction = Education("Future University", "PhD", 2030)
    # #     print("Future Education Created successfully:")
    # # except ValueError as ve:
    # #     print("Vlidation working :", ve)
        
    # try:
    #     invalid_year = Education("Test University", "Degree", "not_a_year")
    #     print("This shouldn't print:")
    # except ValueError as ve:
    #     print("Validation working:", ve)
    
    # print("\n---- EXTRACURRICULAR CLASS TESTING ----")
    
    # soccer = ExtraCurricular("Soccer Team", "Captain of varsity soccer team for 2 years")
    # debate = ExtraCurricular("Debate Club", "Member of the debate club, participated in state competitions")
    # volunteer = ExtraCurricular("Community Service", "Volunteered at local food bank every weekend")
    
    # print("Activity 1:", soccer)
    # print("Activity 2:", debate)
    # print("Activity 3:", volunteer)
    
    # print("\n-- DETAILED INFORMATION --")
    # print(soccer.get_activity_info())
    # print()
    # print(debate.get_activity_info())
    # print()
    # print(volunteer.get_activity_info())
    
    # print("\n-- PROPERTY ACCESS --")
    # print(f"Activity Name: {debate.activity_name}")
    # print(f"Description: {debate.description}")
    
    # print("\n-- EQUALITY TESTING --")
    # same_soccer = ExtraCurricular("Soccer Team", "Captain of varsity soccer team for 2 years")
    # print(f"soccer == same_soccer: {soccer == same_soccer}")  # Should be True
    # print(f"soccer == debate: {soccer == debate}")  # Should be False   
    
    # print("\n---- APPLICATION STATUS TESTING ----")
    
    # pending = ApplicationStatus.PENDING
    # reviewed = ApplicationStatus.REVIEWED
    # accepted = ApplicationStatus.ACCEPTED
    # rejected = ApplicationStatus.REJECTED
    
    # print("\nStatus Values:")
    # print(f"Pending: {pending}")
    # print(f"Reviewed: {reviewed}")
    # print(f"Accepted: {accepted}")          
    # print(f"Rejected: {rejected}")
    
    # print("\n---- APPLICATION CLASS TESTING ----")
    
    # # Create an application with applicant info directly 
    # app = Application("APP-001", "John Doe", "555-123-4567", "john@email.com", 
    #               "123 Main St", "Computer Science")
    
    # # Add education records (objects created internally)
    # app.add_education("Central High School", "High School Diploma", 2020)
    # app.add_education("State University", "Bachelor of Science", 2024)
    
    # # Add extracurricular activities (objects created internally)
    # app.add_extracurricular("Soccer Team", "Team captain for 2 years")
    # app.add_extracurricular("Coding Club", "Python programming projects")
    
    # # View application
    # print(app.get_full_application())
    
    # # Update status
    # app.status = ApplicationStatus.REVIEWED
    # app.status = ApplicationStatus.ACCEPTED
    # print(f"Final status: {app.status}")
    
    
    # # Remove an education record
    # app.remove_education("Central High School", "High School Diploma", 2020)
    
    # print(app.get_full_application())
    
    # # Remove an activity
    # app.remove_extracurricular("Soccer Team", "Team captain for 2 years")
    # print(app.get_full_application())
    
    
    
    # print("=== ADMISSION SYSTEM TESTING (AGGREGATION) ===")
    # system = AdmissionSystem()
    # print("1. Creating applications externally (independent existence)...")
    
    # # create Application objects independently
    # app1 = Application("APP-001", "John Doe", "555-0001", "john@email.com", 
    #                   "123 Main St", "Computer Science")
    # app2 = Application("APP-002", "Jane Smith", "555-0002", "jane@email.com", 
    #                   "456 Oak Ave", "Mathematics")
    
    # app3 = Application("APP-003", "Bob Wilson", "555-0003", "bob@email.com",
    #                   "789 Pine St", "Computer Science")
    
    # print("Applications exist before being added to system!")
    # print(f"Created: {app1}")
    # print(f"Created: {app2}")
    # print(f"Created: {app3}")
    
    # print("\n2. Adding applications to system...")
    # system.add_application(app1)
    # system.add_application(app2)
    # system.add_application(app3)
    # print("All applications added successfully")
    
    # print("\n3. Adding education records to applications...")
    # system.add_education_to_application("APP-001", "Central High School", "High School Diploma", 2020)
    # system.add_education_to_application("APP-001", "State University", "Bachelor of Science", 2024)
    # system.add_education_to_application("APP-002", "Lincoln High", "High School Diploma", 2019)
    # print("Education records added")
    
    # print("\n4. Adding extracurricular activities...")
    # system.add_extracurricular_to_application("APP-001", "Soccer Team", "Captain for 2 years")
    # system.add_extracurricular_to_application("APP-001", "Coding Club", "Member and mentor")
    # system.add_extracurricular_to_application("APP-002", "Debate Club", "State competition participant")
    # print("Extracurricular activities added")
    
    # print("\n5. Displaying all applications:")
    # print(system.display_all_applications())
    
    # print("\n6. Searching applications...")
    # # Search by name
    # print("Searching by name 'John':")
    # results = system.search_applications("name", "John")
    # for app in results:
    #     print(f"  - {app}")
    
    # # Search by email
    # print("\nSearching by email 'jane@email.com':")
    # results = system.search_applications("email", "jane")
    # for app in results:
    #     print(f"  - {app}")
    
    # # Search by status
    # print("\nSearching by status 'Pending':")
    # results = system.search_applications("status", "Pending")
    # for app in results:
    #     print(f"  - {app}")
    
    # print("\n7. Modifying existing application details...")
    
    # # Update personal information
    # print("Updating personal info for APP-001...")
    # success = system.update_personal_info("APP-001", name="John David Doe", 
    #                                      email="john.doe@newmail.com")
    # print(f"Personal info update: {'Success' if success else 'Failed'}")
    
    # # Update application status
    # print("\nUpdating application status for APP-001...")
    # success = system.update_application_status("APP-001", ApplicationStatus.REVIEWED)
    # print(f"Status update to REVIEWED: {'Success' if success else 'Failed'}")
    
    # success = system.update_application_status("APP-001", ApplicationStatus.ACCEPTED)
    # print(f"Status update to ACCEPTED: {'Success' if success else 'Failed'}")
    
    # print("\nUpdating application status for APP-002...")
    # success = system.update_application_status("APP-002", ApplicationStatus.REVIEWED)
    # print(f"Status update to REVIEWED: {'Success' if success else 'Failed'}")
    
    # # Add more education
    # print("\nAdding additional education to APP-002...")
    # success = system.add_education_to_application("APP-002", "Community College", 
    #                                               "Associate Degree", 2022)
    # print(f"Education addition: {'Success' if success else 'Failed'}")
    
    # # Remove an education record
    # print("\nRemoving education from APP-001...")
    # success = system.remove_education_from_application("APP-001", "Central High School", 
    #                                                    "High School Diploma", 2020)
    # print(f"Education removal: {'Success' if success else 'Failed'}")
    
    # # Remove an extracurricular
    # print("\nRemoving extracurricular from APP-001...")
    # success = system.remove_extracurricular_from_application("APP-001", "Coding Club", 
    #                                                          "Member and mentor")
    # print(f"Extracurricular removal: {'Success' if success else 'Failed'}")
    
    
    # print("\n8. Viewing updated application details:")
    # app = system.get_application_by_id("APP-001")
    # if app:
    #     print(app.get_full_application())
    
    # print("\n9. Getting applications by status:")
    # pending_apps = system.get_applications_by_status(ApplicationStatus.PENDING)
    # reviewed_apps = system.get_applications_by_status(ApplicationStatus.REVIEWED)
    # accepted_apps = system.get_applications_by_status(ApplicationStatus.ACCEPTED)
    
    # print(f"Pending applications: {len(pending_apps)}")
    # print(f"Reviewed applications: {len(reviewed_apps)}")
    # print(f"Accepted applications: {len(accepted_apps)}")
    
    # print("\n10. Getting system summary:")
    # summary = system.get_applications_summary()
    # print(f"Total applications: {summary['total']}")
    # print(f"Pending: {summary['pending']}")
    # print(f"Reviewed: {summary['reviewed']}")
    # print(f"Accepted: {summary['accepted']}")
    # print(f"Rejected: {summary['rejected']}")
    
    
   
    
    # print("\n12. Final application list:")
    # print(system.display_all_applications())
    
    
    
    
    
    
    
   
   print("Starting Admission Application System...")
   try:
        menu = MenuInterface()
        menu.run()
   except NameError as e:
        print(f"\n✗ ERROR: {e}")
        print("\nRequired imports:")
        print("  - AdmissionSystem")
        print("  - Application")
        print("  - ApplicationStatus")
        print("  - Applicant")
        print("  - Education")
        print("  - Extracurricular")
   
if __name__ == "__main__":
    main()
    
              
    
    