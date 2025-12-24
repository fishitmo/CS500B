from __future__ import annotations
from state_machine import (State, Event, acts_as_state_machine,
                           after, before, InvalidStateTransition)


@acts_as_state_machine
class HouseBuyingProcess:
   

  
    Browse = State(initial=True)
    Selected = State()
    Viewing = State()
    Offer = State()
    CounterOffer = State()
    OfferAccepted = State()
    PreApproval = State()
    OfferRejected = State()
    Approved = State()
    Disapproved = State()
    Inspection = State()
    Closing = State()
    GetKeys = State()
    
    
    get_house_details = Event(from_states=(Browse,), to_state=Selected)
    list_houses = Event(from_states=(Viewing,  OfferRejected, Disapproved), to_state=Browse)
    schedule_viewing = Event(from_states=(Selected), to_state=Viewing)
    finish_viewing = Event(from_states=(Viewing), to_state=Offer)
    counter_offer = Event(from_states=(Offer), to_state=CounterOffer)
    offer_again = Event(from_states=(CounterOffer), to_state=Offer)
    accepted_offer = Event(from_states=(Offer), to_state=OfferAccepted)
    rejected_offer = Event(from_states=(Offer), to_state=OfferRejected)
    apply_pre_approval = Event(from_states=(OfferAccepted,), to_state=PreApproval)
    evaluate_loan = Event(from_states=(PreApproval,), to_state=Approved)
    disapprove_loan = Event(from_states=(PreApproval), to_state=Disapproved)
    inspect_house = Event(from_states=(Approved), to_state=Inspection)
    sign_closing_documents = Event(from_states=(Inspection), to_state=Closing)
    receive_house_keys = Event(from_states=(Closing), to_state=GetKeys)
    back_out = Event(from_states=(Inspection), to_state=Browse)

    def __init__(self, real_estate: RealEstate) -> None:
        self.__real_estate = real_estate

 
  

    @after("get_house_details")
    def after_get_house_details(self):
        print("House details retrieved!")

    @after("list_houses")
    def after_list_houses(self):
        print("Returning to browse available houses...")


    @after("schedule_viewing")
    def after_schedule_viewing(self):
        print("Viewing scheduled successfully!")

   
    @after("finish_viewing")
    def after_finish_viewing(self):
        print("Viewing completed. Ready to make an offer.")

  

    @after("counter_offer")
    def after_counter_offer(self):
        print("Counter offer created!")
        
    @after("offer_again")
    def after_offer_again(self):
        print("Offer resubmitted!")
    
    @after("apply_pre_approval")
    def after_apply_pre_approval(self):
        print("Applying for pre-approval...")
        
    @after("accepted_offer")
    def after_accepted_offer(self):
        print("Congratulations! Your offer has been accepted!")

    @after("rejected_offer")
    def after_rejected_offer(self):
        print("Unfortunately, your offer was rejected.")


   
    @after("apply_accepted_offer")
    def after_apply_accepted_offer(self):
        print("Applying for pre-approval...")

    @before("evaluate_loan")
    def before_evaluate_loan(self):
        return self.__real_estate.evaluate_loan_application()

    @after("evaluate_loan")
    def after_evaluate_loan(self):
        print("Loan approved! Moving forward with the purchase.")

    @after("disapprove_loan")
    def after_disapprove_loan(self):
        print("Loan application was disapproved. Please review your finances.")
        
        
        

    @after("inspect_house")
    def after_inspect_house(self):
        print("House inspection completed!")

    # Inspection state
    @after("sign_closing_documents")
    def after_sign_closing_documents(self):
        print("Closing documents signed!")

    # Closing state
    @after("receive_house_keys")
    def after_receive_house_keys(self):
        print("Congratulations! You received the keys to your new home!")

    @after("back_out")
    def after_back_out(self):
        print("browsing available houses")


class RealEstate:
    

    def __init__(self) -> None:
        self.__process = HouseBuyingProcess(self)
        self.__monthly_income = 0
        self.__house_price = 0
        self.__loan_interest_rate = 0
        self.__term_months = 0

      

    

    def evaluate_loan_application(self):
       
        try:
            
            self.__monthly_income = float(input("Enter your monthly income: $").strip())
            self.__loan_interest_rate = float(input("Enter loan interest rate (%): ").strip())
            self.__term_months = int(input("Enter loan term (months): ").strip())
            self.__house_price = float(input("Enter house price: $").strip())

            total_interest = (self.__house_price * self.__loan_interest_rate / 100)
            total_amount = self.__house_price + total_interest
            monthly_payment = total_amount / self.__term_months

            print(f"\nHouse Price: ${self.__house_price:,}")
            print(f"Total Interest: ${total_interest:,}")
            print(f"Monthly Payment Required: ${monthly_payment:,.2f}")
            print(f"Your Monthly Income: ${self.__monthly_income:,}")

            
            if self.__monthly_income > monthly_payment:
                print("\nYou qualify for the loan!")
                return True
            else:
                print("\nInsufficient income for loan approval.")
                return False

        except ValueError:
            print("Invalid input!")
            return False

  
    def get_house_details(self):
        self.__process.get_house_details()

    def list_houses(self):
        self.__process.list_houses()

    def schedule_viewing(self):
        self.__process.schedule_viewing()

    def finish_viewing(self):
        self.__process.finish_viewing()

    def counter_offer(self):
        self.__process.counter_offer()
        
    def offer_again(self):
        self.__process.offer_again()

    def apply_pre_approval(self):
        self.__process.apply_pre_approval()

    def accepted_offer(self):
        self.__process.accepted_offer()

    def rejected_offer(self):
        self.__process.rejected_offer()
    



    def evaluate_loan(self):
        self.__process.evaluate_loan()

    def disapprove_loan(self):
        self.__process.disapprove_loan()

    def inspect_house(self):
        self.__process.inspect_house()

    def sign_closing_documents(self):
        self.__process.sign_closing_documents()

    def receive_house_keys(self):
        self.__process.receive_house_keys()

    def back_out(self):
        self.__process.back_out()

    def get_current_state(self):
        return self.__process.current_state

    def set_current_state(self, state):
        self.__process.current_state = state



def show_menu():
    print()
    print("====== HOUSE BUYING PROCESS MENU ======")
    print("1.  Get House Details")
    print("2.  List Houses")
    print("3.  Schedule Viewing")
    print("4.  Finish Viewing")
    print("5.  Make Counter Offer")
    print("6.  Resubmit Offer")
    print("7.  Accept Offer")
    print("8.  Reject Offer")
    print("9.  Apply for Pre-Approval")
    print("10. Evaluate Loan Application")
    print("11. Disapprove Loan")
    print("12. Inspect House")
    print("13. Sign Closing Documents")
    print("14. Receive House Keys")
    print("15. Back Out")
    print("16. Show Current State")
    print("17. Exit")


def main():
    real_estate = RealEstate()

    while True:
        show_menu()
        print(f"Current State: {real_estate.get_current_state()}")

        try:
            choice = input("\nEnter your choice (1-17): ").strip()

            if choice == "1":
                real_estate.get_house_details()
            elif choice == "2":
                real_estate.list_houses()
            elif choice == "3":
                real_estate.schedule_viewing()
            elif choice == "4":
                real_estate.finish_viewing()
            elif choice == "5":
                real_estate.counter_offer()
            elif choice == "6":
                real_estate.offer_again()
            elif choice == "7":
                real_estate.accepted_offer()
            elif choice == "8":
                real_estate.rejected_offer()
            elif choice == "9":
                real_estate.apply_pre_approval()
            elif choice == "10":
                real_estate.evaluate_loan()
            elif choice == "11":
                real_estate.disapprove_loan()
            elif choice == "12":
                real_estate.inspect_house()
            elif choice == "13":
                real_estate.sign_closing_documents()
            elif choice == "14":
                real_estate.receive_house_keys()
            elif choice == "15":
                real_estate.back_out()
            elif choice == "16":
                print(f"\nCurrent State: {real_estate.get_current_state()}")
            elif choice == "17":
                print("\nThank you for using the House Buying Process System!")
                break
            else:
                print("\nInvalid choice! Please select a number between 1 and 17.")

        except InvalidStateTransition as e:
            print(f"\nInvalid state transition! {e}")
            print(f"Cannot perform this action from the current state: {real_estate.get_current_state()}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()










    
