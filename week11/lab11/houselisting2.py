
 
from __future__ import annotations

from abc import ABC, abstractmethod


class Displayable(ABC):
    @abstractmethod
    def display():
        pass


class House(Displayable):
    def __init__(self, address, square_feet, num_rooms, price, city):
        self.__address = address
        self.__square_feet = square_feet
        self.__num_rooms = num_rooms
        self.__price = price
        self.__city = city
        
    @property
    def address(self):
        return self.__address
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value) -> None:
        if value > 0:
            self.__price = value

    # add some public properties here if necessary 
    def __str__(self) -> str:
        return f"Address: {self.__address}, Square Feet: {self.__square_feet}, Number of Rooms: {self.__num_rooms}, Price: {self.__price}"
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, House):
            return self.__address == value.__address
        return False
    

    def display(self):
        print(self)
        
    


class Contact(Displayable):
    def __init__(self, firstname, lastname, phone_number, email):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__email = email
        self.__phone_number = phone_number
    
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Contact):
            return self.__email == value.__email
        return False
    # add some public properties here if necessary 

    def __str__(self) -> str:
        return f" Last Name: {self.__lastname}, First Name: {self.__firstname}, Phone Number: {self.__phone_number}, Email: {self.__email}"

    def display(self):
        print(self)
        
    


class Owner(Contact):
    def __init__(self, lastname, firstname, phone_number, email):
        super().__init__(lastname, firstname, phone_number, email)
        self.__houses:  list[House] = []

    def add_house(self, house: House):
       if house not in self.__houses:
          self.__houses.append(house)
        
    def __str__(self) -> str:
        output = f"{super().__str__()}\n"
        output += "Owns the following houses:\n"
        for  house in self.__houses:
            output += str(house) + "\n"
        return output
    
            

    def display(self):
        print(self)
   

class Buyer(Contact):
    def __init__(self, lastname, firstname, phone_number, email):
        super().__init__(lastname, firstname, phone_number, email)
        self.__watch_list = []
        
    def intersted(self, house: House) -> bool:
         return house in self.__watch_list

    # @property
    # def watch_list(self):
    #     return self.__watch_list

    #  Save the house in his watch list 
    def save_to_watchlist(self, house):
        
        if house not in self.__watch_list:
            self.__watch_list.append(house)

    # Remove the house from his watch list
    def remove_from_watchlist(self, house):
        if house in self.__watch_list:
            self.__watch_list.remove(house)
        
    
    def __str__(self) -> str:
        output = f"{super().__str__()}\n"
        output += "Watching the following houses:\n"
        for  house in self.__watch_list:
            output += str(house) + "\n"
        return output

    def display(self):
        print(self)


class Company(Displayable):
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__owners: list[Owner] = []
        self.__buyers: list[Buyer] = []
        self.__agents: list[Agent] = []
        self.__houses: list[House] = []

    def add_owner(self, owner: Owner):
        if owner not in self.__owners:
            self.__owners.append(owner)

    def add_buyer(self, buyer: Buyer):
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)

    def add_agent(self, agent: Agent):
        if agent not in self.__agents:
            self.__agents.append(agent)

    def add_house_to_listing(self, house):
        if house not in self.__houses:
            self.__houses.append(house)

    def get_house_by_address(self, address: str):
         for house in self.__houses:
            if house.address == address:
                return house
         return None        

    def remove_house_from_listing(self, house):
        pass

    # Help to remove that house from all buyers' watch list.
    def remove_house_from_watchlist(self, house):
        pass

    def get_buyers_by_house(self, house) -> list[Buyer]:
        buyers: list[Buyer] = []
        for buyer in self.__buyers:
            if buyer.intersted(house) is True:
                buyers.append(buyer)
        return buyers

    
    def __str__(self) -> str:
        output = f"Comapny Name: {self.__companyName}\n"
        output += "=========================== The list of agents: ===================================\n"
        for agent in self.__agents:
            output += str(agent) + "\n"
        output += "=========================== The list of owners: ===================================\n"
        for owner in self.__owners:
            output += str(owner) + "\n"
        output += "=========================== The list of buyers: ===================================\n"
        for buyer in self.__buyers:
            output += str(buyer) + "\n"
        output += "=========================== The list of houses: ===================================\n"
        for house in self.__houses:
            output += str(house) + "\n"
        return output

    def display(self):
        print(self)


class Agent(Contact):
    def __init__(self, lastname, firstname, phone_number, email, position, company):
        super().__init__(lastname, firstname, phone_number, email)
        self.__position = position
        self.__company: Company = company

    def add_house_to_listing_for_owner(self, owner: Owner, house: House):
        self.__company.add_owner(owner)
        self.__company.add_house_to_listing(house)

    def help_buyer_to_save_to_watchlist(self, buyer: Buyer, house: House):
        self.__company.add_buyer(buyer)
        buyer.save_to_watchlist(house)

    def edit_house_price(self, address: str, new_price: str):
        house = self.__company.get_house_by_address(address)
        if house is not None:
            house.price = new_price

    def sold_house(self, house):
        self.__company.remove_house_from_listing(house)
        self.__company.remove_house_from_watchlist(house)

    # print all potential buyers who are interested in buying that house
    def display_potental_buyers(self, house):
        pass

    def display(self):
        pass


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000, 'Fremomt')
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000, 'San Jose')
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000, 'Mountain View')

    owner1.add_house(house1)
    owner2.add_house(house2)
    owner2.add_house(house3)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.add_agent(agent1)

    agent1.add_house_to_listing_for_owner(owner1, house1)
    agent1.add_house_to_listing_for_owner(owner2, house2)
    agent1.add_house_to_listing_for_owner(owner2, house3)

    agent1.help_buyer_to_save_to_watchlist(buyer1, house1)
    agent1.help_buyer_to_save_to_watchlist(buyer1, house2)
    agent1.help_buyer_to_save_to_watchlist(buyer1, house3)

    agent1.help_buyer_to_save_to_watchlist(buyer2, house2)
    agent1.help_buyer_to_save_to_watchlist(buyer2, house3)

    agent1.edit_house_price('2222 Mission Blvd', 1200000)

    company.display()

    print('\nAfter one house was sold ..........................')
    agent1.sold_house(house3)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.display_potental_buyers(house1)
    
    

if __name__ == "__main__":
    main()
    

