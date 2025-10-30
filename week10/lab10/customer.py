from __future__ import annotations

class Customer:
    def __init__(self, account_no: int,lasname: str, firstname: str, address: str, balance: float) -> None:
        
        self.__account_no = account_no
        self.__lasname = lasname
        self.__firstname = firstname
        self.__address = address
        self.__balance = balance
        
        
    @property
    def account_no(self) -> int:
        return self.__account_no
    
    @property
    def lasname(self) -> str:
        return self.__lasname
    
    @property
    def firstname(self) -> str:
        return self.__firstname
    
    @property
    def address(self) -> str:
        return self.__address
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    @account_no.setter
    def account_no(self, value: int) -> None:
        self.__account_no = value
        
    @lasname.setter
    def lasname(self, value: str) -> None:
        self.__lasname = value
        
    @firstname.setter
    def firstname(self, value: str) -> None:
        self.__firstname = value
        
    @address.setter
    def address(self, value: str) -> None:
        self.__address = value
        
    @balance.setter
    def balance(self, value: float) -> None:
        self.__balance = value
        
        
    def to_list(self) -> list[str]:
        output : list[str] = []
        output.append(str(self.__account_no))
        output.append(self.__lasname)
        output.append(self.__firstname)
        output.append(self.__address)
        output.append(str(self.__balance))
        return output
    
    
    @staticmethod
    def to_customer(row: list[str]) -> Customer:
        account_no = int(row[0])
        lasname = row[1]
        firstname = row[2]
        address = row[3]
        balance = float(row[4])
        customer = Customer(account_no, lasname , firstname, address , balance)
        return customer
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Customer):
            return self.__account_no == value.account_no
        return False
    
    
    def __str__(self) -> str:
        print("Cutommer information:")
        
        output = ""
        output += f"Account number: {self.__account_no}\n"
        output += f"Last name: {self.__lasname}\n"
        output += f"First name: {self.__firstname}\n"
        output += f"Address: {self.__address}\n"
        output += f"Balance: {self.__balance}\n"
        return output
    
    
if __name__ == "__main__":
    customer = Customer(1, "Doe", "John", "123 Main St", 1000.0)
    print(customer)