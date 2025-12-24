from __future__ import annotations

from state_machine import (State, Event, acts_as_state_machine,
                           after, before, InvalidStateTransition)


@acts_as_state_machine
class OrderProcess:
    # define 7 states
    CheckOut = State(initial=True)
    SelectPizza = State()
    PlaceOrder = State()
    PreparingOrder = State()
    MakingOrder = State()
    ReadyForPickupOrder = State()
    CompletedOrder = State()


    # define 8 events

    select_pizza = Event(from_states=(CheckOut), to_state=SelectFlavor)
    cancel_order = Event(from_states=(SelectFlavor, PlaceOrder), to_state=CheckOut)
    check_inventory = Event(from_states=(SelectFlavor), to_state=PlaceOrder)
    place_order = Event(from_states=(PlaceOrder), to_state=PreparingOrder)
    making_ice_cream = Event(from_states=(PreparingOrder), to_state=MakingOrder)
    finish_ice_cream = Event(from_states=(MakingOrder), to_state=ReadyForPickupOrder)
    pick_up_order = Event(from_states=(ReadyForPickupOrder), to_state=CompletedOrder)
    ready_to_order = Event(from_states=(CompletedOrder), to_state=CheckOut)




    def __init__(self, store: IceCreameStore) -> None:
        self.__store = store

    @before("select_flavor")
    def before_select_flavor(self):
        self.__store.choose_flavor()
    
    @after("select_flavor")
    def after_select_flavor(self):
        print("Flavor selected!")
    
    @after("cancel_order")
    def after_cancel_order(self):
        print("Order cancelled!")
    
    @before("check_inventory")
    def before_check_inventory(self):
        return self.__store.is_enough_inventory()

    @after("check_inventory")
    def after_check_inventory(self):
        print("Inventory checked!")


class IceCreameStore:
    def __init__(self) -> None:
        self.__process = OrderProcess(self)
        self.__flavor = ""
        self.__size = ""
        self.__inventory = {"Vanilla": 5, "Chocolate": 2, "Strawberry": 1}
        self.__recipe_required = {"Large": 1, "Medium": .5, "Small": .25}
