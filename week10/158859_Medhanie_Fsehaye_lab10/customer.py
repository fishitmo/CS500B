

from __future__ import annotations
class Customer:

    def __init__(self, account_no: int, lastname: str , firstname: str, address: str,balance: float) -> None:
        self.__account_no = account_no
        self.__lastname = lastname
        self.__firstname = firstname
        self.__address = address
        self.__balance = balance
        
        
    @property
    def account_no(self) -> int:
        return self.__account_no
    
    @property
    def firstname(self) -> str:
        return self.__firstname
    @firstname.setter
    def firstname(self, value: str) -> None:
        self.__firstname = value
        
    
    
    @property
    def lastname(self) -> str:
        return self.__lastname    
    
    @lastname.setter
    def lastname(self, value: str) -> None:
        self.__lastname = value
        
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    @balance.setter
    def balance(self, value: float) -> None:
        self.__balance = value
    
    @property
    def address(self) -> str:
        return self.__address
    
    @address.setter
    def address(self, value: str) -> None:
        self.__address = value
    
    def to_list(self) -> list[str]:
        
        output : list[str] = []
        output.append(str(self.__account_no))
        output.append(self.__lastname)
        output.append(self.__firstname)
        output.append(self.__address)
        output.append(str(self.__balance))
       
        
        return output
    
    
    @staticmethod
    def to_customer(row: list[str]) -> Customer:
        account_no = int(row[0])
        lastname = row[1]
        firstname = row[2]
        address = row[3]
        balance = float(row[4])
        customer = Customer(account_no, lastname , firstname, address , balance)
        return customer
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Customer):
            return self.__account_no == value.__account_no
        return False
    
    
    def to_list_str(self) -> list[str]:
        output: list[str] = []
        output.append(str(self.__account_no))
        output.append(self.__lastname)
        output.append(self.__firstname)
        output.append(self.__address)
        output.append(str(self.__balance))
        return output
    def __str__(self) -> str:
        return  f"Customer: \naccount_no {self.__account_no}: \nfirst_name {self.__firstname}, \nlast_name {self.__lastname}, \nbalance $ {self.__balance}, \naddress {self.__address}"

if __name__ == "__main__":
    customer = Customer(1111, "Lee", "Peter", "120 Mission Blvd, Fremont", 10000.0)
    print(customer)
