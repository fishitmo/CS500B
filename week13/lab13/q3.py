from abc import ABC, abstractmethod

class PayPalPaymentGateway(ABC):
    @abstractmethod
    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        pass
    

# Adaptee

class LegacyPaymentGateway:
    def process_credit_card_payment(self, credit_card_number: str, expiration_date: str, cvv: str, amount: float) -> bool:
        print("Simulates processing a credit card payment")
        return True
    
class PaypalPaymentAdapter(PayPalPaymentGateway):
    def __init__(self, obj: LegacyPaymentGateway) -> None:
        self.__obj = obj
        
    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
       
       credit_card_number = self.get_credit_card_number(email_address)
       expiration_date = self.get_expiration_date(email_address)
       cvv = self.get_cvv(email_address)
       return  self.__obj.process_credit_card_payment(credit_card_number, expiration_date, cvv, amount)
         
    def get_credit_card_number(self, email_address: str) -> str:
        return "5555-2222-7777-8888"
    
    def get_expiration_date(self, email_address: str) -> str:
        return "11/27"
    
    def get_cvv(self, email_address: str) -> str:
        return "721"
    
class PayPalPaymentFactory:
    
    @staticmethod
    def get_getway() -> PayPalPaymentGateway:
        return PaypalPaymentAdapter(LegacyPaymentGateway())
    
def main():
    
    gateway = PayPalPaymentFactory.get_getway()
    gateway.process_paypal_payment("fish@gmail.com", 2000)
    
if __name__ =="__main__":
    main()


# question-2 part two and question-4