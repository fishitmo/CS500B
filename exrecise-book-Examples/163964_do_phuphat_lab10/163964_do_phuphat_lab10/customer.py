from __future__ import annotations


class Customer:
    def __init__(self, account_number: int, last_name: str, first_name: str, address: str, balance: float) -> None:
        self.__account_number = account_number
        self.__last_name = last_name
        self.__first_name = first_name
        self.__address = address
        self.__balance = balance

    def __str__(self) -> str:
        output = "Customer: "
        output += f"account={self.__account_number}, "
        output += f"name={self.__first_name} {self.__last_name}, "
        output += f"address={self.__address}, "
        output += f"balance=${self.__balance:,.2f}"
        return output

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Customer):
            return self.__account_number == value.__account_number
        return False

    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self.__last_name = value

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self.__first_name = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        self.__balance = value

    @staticmethod
    def from_list_str(row: list[str]) -> Customer:
        account_number = int(row[0])
        last_name = row[1]
        first_name = row[2]
        address = row[3]
        balance = float(row[4])
        customer = Customer(account_number, last_name, first_name, address, balance)
        return customer

    def to_list_str(self) -> list[str]:
        output: list[str] = []
        output.append(str(self.__account_number))
        output.append(self.__last_name)
        output.append(self.__first_name)
        output.append(self.__address)
        output.append(str(self.__balance))
        return output


if __name__ == "__main__":
    customer = Customer(1111, "Lee", "Peter", "120 Mission Blvd, Fremont", 10000.0)
    print(customer)
