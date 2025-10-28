

import re

class ContactInfo:
    def __init__(self, phone: str, email: str, address: str) -> None:
        self.__email = email
        self.__phone = phone
        self.__address = address
        
        
    @property
    def phone(self) -> str:
        return self.__phone
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def address(self) -> str:
        return self.__address
    
    def _validate_phone(self, phone: str) -> bool:
        digits_only = re.sub(r'[\s\-\(\)\.]+', '', phone)
        
        if len(digits_only) >= 10 and len(digits_only) <= 11 and digits_only.isdigit():
            return True
        
        return False
    
    def _valiidate_email(self, email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(email_regex, email):
            return True
        
        return False
    
    def validate(self) -> bool:
        
        return self._validate_phone(self.__phone) and self._valiidate_email(self.__email) and bool(self.__address)
    
    
    def to_dict(self) -> dict:
        
        return {
            "phone": self.__phone,
            "email": self.__email,
            "address": self.__address
        }
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value, ContactInfo):
            return (self.__phone == value.__phone and
                    self.__email == value.__email and
                    self.__address == value.__address)
        return False
    

    def __str__(self) -> str:
        
        return f"Contact Information:\n  Phone: {self.__phone}\n  Email: {self.__email}\n  Address: {self.__address}"
    
    
   
    
    
    
if __name__ == "__main__":
    contact1 = ContactInfo("(555) 123-4567", "john.doe@email.com", "123 Main St, City, State")
    
    
    print(contact1)
    
    contact2 = ContactInfo("555-987-6543", "newemail@example.com", "456 Elm St, City, State")
    
    print(contact2)
    
    contact3 = ContactInfo("5551234567", "info@realestate.com", "789 Pine Rd")
    
    print(contact3)
    
    print(f"Phone: {contact1.phone}")
    
    print(f"Email: {contact1.email}")

    print(f"Address: {contact1.address}")
    
    contact_dict = contact1.to_dict()
    print(contact_dict)
    
    
    print(type(contact_dict))
    
    print("Testing validation:")
    print(f"Contact 1 valid: {contact1.validate()}")
    print(f"Contact 2 valid: {contact2.validate()}")
    print(f"Contact 3 valid: {contact3.validate()}")    
    
    invalid_contact = ContactInfo("12345", "invalidemail", "")
    print(f"Invalid contact valid: {invalid_contact.validate()}")

    print("Testing invalid phone number:")
    invalid_phone_contact = ContactInfo("12345", "valid.email@example.com", "123 Main St")
    print(f"Invalid phone contact valid: {invalid_phone_contact.validate()}")
    
    print("Testing email case sensitivity: ")
    case_sensitive_email_contact = ContactInfo("555-123-4567", "o0N3o@example.com", "123 Main St")
    print(f"Case-sensitive email contact valid: {case_sensitive_email_contact.validate()}")
    
    
    
    