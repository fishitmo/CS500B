

from __future__ import annotations
class Customer:

    def __init__(self, account_no: int, firstname: str, balance: float) -> None:
        self.__account_no = account_no
        self.__firstname = firstname
        self.__balance = balance
        
    def __str__(self) -> str:
        return  f"Customer: account_no {self.__account_no}: first_name {self.__firstname},  balance $ {self.__balance}"

    def to_list(self) -> list[str]:
        
        output = []
        
        output.append(str(self.__account_no))
        output.append(self.__firstname)
        output.append(str(self.__balance))
        return output
    
    
    @staticmethod
    def to_customer(row: list[str]) -> Customer:
        account_no = int(row[0])
        firstname = str(row[1])
        balance = float(row[2])
        customer = Customer(account_no, firstname, balance)
        return customer