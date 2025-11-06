

from __future__ import annotations

from abc import ABC, abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display() -> None:
        pass

class Observer(ABC):

    @abstractmethod
    def update(self, event: str, house: House) -> None:
        pass

class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, event: str, house: House) -> None:
        pass



class House(Displayable):
    def __init__(self, address: str, square_feet: int, num_rooms: int, price: float, city: str) -> None:
        self.__address = address
        self.__square_feet = square_feet
        self.__num_rooms = num_rooms
        self.__price = price
        self.__city = city

    @property
    def address(self) -> str:
        return self.__address

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value > 0:
            self.__price = value

    def __str__(self) -> str:
        return f"Address: {self.__address}, Square Feet: {self.__square_feet}, Number of Rooms: {self.__num_rooms}, Price: {self.__price}"

    def __eq__(self, value: object) -> bool:
        if isinstance(value, House):
            return self.__address == value.__address
        return False

    def display(self) -> None:
        print(self)



class Contact(Displayable):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str) -> None:
        self.__lastname = lastname
        self.__firstname = firstname
        self.__email = email
        self.__phone_number = phone_number


    def __eq__(self, value: object) -> bool:
        if isinstance(value, Contact):
            return self.__email == value.__email
        return False

    def __str__(self) -> str:
        return f"Last Name: {self.__lastname}, First Name: {self.__firstname}, Phone Number: {self.__phone_number}, Email: {self.__email}"

    def display(self) -> None:
        print(self)



class Owner(Contact, Observer):
    def __init__(self, lastname: str, firstname: str, phone_number: str, email: str) -> None:
        super().__init__(lastname, firstname, phone_number, email)
        self.__houses: list[House] = []

    def add_house(self, house: House) -> None:
        if house not in self.__houses:
            self.__houses.append(house)

    def belong(self, house: House) -> bool:
        return house in self.__houses

    def update(self, event: str, house: House) -> None:
        print(f"Owner notification: {event} - {house}")

    def __str__(self) -> str:
        output = f"{super().__str__()}\n"
        output += "Owns the following houses:\n"
        for house in self.__houses:
            output += str(house) + "\n"
        return output

    def display(self) -> None:
        print(self)


class Buyer(Contact, Observer):
    def __init__(self, lastname, firstname, phone_number, email) -> None:
        super().__init__(lastname, firstname, phone_number, email)
        self.__watch_list: list[House] = []

    def intersted(self, house: House) -> bool:
        return house in self.__watch_list

    def save_to_watchlist(self, house: House) -> None:
        if house not in self.__watch_list:
            self.__watch_list.append(house)

    def remove_from_watchlist(self, house):
        if house in self.__watch_list:
            self.__watch_list.remove(house)

    def update(self, event: str, house: House) -> None:
        print(f"Buyer notification: {event} - {house}")

    def __str__(self) -> str:
        output = f"{super().__str__()}\n"
        output += "Watching the following houses:\n"
        for house in self.__watch_list:
            output += str(house) + "\n"
        return output

    def display(self) -> None:
        print(self)


class Company(Subject):
    def __init__(self, companyName: str) -> None:
        self.__companyName = companyName
        self.__houses: list[House] = []
        self.__observers: list[Observer] = []

    def add_house_to_listing(self, house: House) -> None:
        if house not in self.__houses:
            self.__houses.append(house)
            self.notify("House added to listing", house)

    def get_house_by_address(self, address: str) -> House | None:
        for house in self.__houses:
            if house.address == address:
                return house
        return None

    def remove_house_from_listing(self, house: House) -> None:
        if house in self.__houses:
            self.__houses.remove(house)
            self.notify("House removed from listing", house)

    def get_owner_of_house(self, house: House) -> Owner | None:
        for observer in self.__observers:
            if isinstance(observer, Owner) and observer.belong(house):
                return observer
        return None

    def get_interested_buyers(self, house: House) -> list[Buyer]:
        buyers = []
        for observer in self.__observers:
            if isinstance(observer, Buyer) and observer.intersted(house):
                buyers.append(observer)
        return buyers

    def remove_house_from_all_buyers_watchlist(self, house: House) -> None:
        for observer in self.__observers:
            if isinstance(observer, Buyer):
                observer.remove_from_watchlist(house)

    def attach(self, observer: Observer) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify(self, event: str, house: House) -> None:
        owner = self.get_owner_of_house(house)
        interested_buyers = self.get_interested_buyers(house)

        for observer in self.__observers:
            if event == "House added to listing":
                if isinstance(observer, Agent) or observer == owner or isinstance(observer, Buyer):
                # notify everyone
                    observer.update(event, house)

            elif event == "House removed from listing":
                # notify agents and owner only
                if isinstance(observer, Agent) or observer == owner:
                    observer.update(event, house)

            elif event == "House price updated":
                # notify agents, owner, and interested buyers
                if isinstance(observer, Agent) or observer == owner or observer in interested_buyers:
                    observer.update(event, house)
            elif event == "House sold":
                # notify agents, owner, and interested buyers
                if isinstance(observer, Agent) or observer == owner or observer in interested_buyers:
                    observer.update(event, house)

    def display_houses(self) -> None:
        print(f"Company Name = {self.__companyName}")
        print("=========================== The house listing: ===============================")
        for house in self.__houses:
            print(house)


class Agent(Contact, Observer):
    def __init__(self, lastname: str, firstname: str, phone_number: str, email: str, position: str, company: Company) -> None:
        super().__init__(lastname, firstname, phone_number, email)
        self.__position = position
        self.__company: Company = company

    def update(self, event: str, house: House) -> None:
        print(f"Agent notification: {event} - {house}")

    def add_house_to_listing_for_owner(self, owner: Owner, house: House) -> None:
        owner.add_house(house)
        self.__company.attach(owner)
        self.__company.add_house_to_listing(house)

    def help_buyer_to_save_to_watchlist(self, buyer: Buyer, house: House) -> None:
        buyer.save_to_watchlist(house)
        self.__company.attach(buyer)

    def edit_house_price(self, address: str, new_price: float) -> None:
        house = self.__company.get_house_by_address(address)
        if house is not None:
            house.price = new_price
            self.__company.notify("House price updated", house)

    def sold_house(self, house: House) -> None:
        self.__company.notify("House sold", house)
        self.__company.remove_house_from_listing(house)
        self.__company.remove_house_from_all_buyers_watchlist(house)

    def display_potential_buyers(self, house: House) -> None:
        buyers = self.__company.get_interested_buyers(house)
        for buyer in buyers:
            buyer.display()

    def __str__(self) -> str:
        output = f"{super().__str__()}\n"
        output += f"Position = {self.__position}"
        return output

    def display(self) -> None:
        print(self)


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000, 'Fremont')
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000, 'San Jose')
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000, 'Mountain View')

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)

    # Attach agent as observer
    company.attach(agent1)

    print("========== Adding houses to listing ==========")
    agent1.add_house_to_listing_for_owner(owner1, house1)
    print()
    agent1.add_house_to_listing_for_owner(owner2, house2)
    print()
    agent1.add_house_to_listing_for_owner(owner2, house3)
    print()

    # Buyers saving houses to watchlist 
    agent1.help_buyer_to_save_to_watchlist(buyer1, house1)
    agent1.help_buyer_to_save_to_watchlist(buyer1, house2)
    agent1.help_buyer_to_save_to_watchlist(buyer1, house3)

    agent1.help_buyer_to_save_to_watchlist(buyer2, house2)
    agent1.help_buyer_to_save_to_watchlist(buyer2, house3)
    print()

    print("========== Editing house price ==========")
    agent1.edit_house_price('2222 Mission Blvd', 1200000)
    print()

    company.display_houses()
    print()

    print('========== After one house was sold ==========')
    agent1.sold_house(house3)
    print()

    company.display_houses()
    print()

    print('========== Displaying potential buyers for house 1 ==========')
    agent1.display_potential_buyers(house2)


if __name__ == "__main__":
    main()
