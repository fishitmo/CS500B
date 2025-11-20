from abc import ABC, abstractmethod

class NewNotificationSystem(ABC):
    @abstractmethod
    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        pass
    
    @abstractmethod
    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        pass
    
    @abstractmethod
    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        pass


# Adaptee

class LegacyNotificationSystem:
    def send_sms_notification(self, phoneNumber: str, message: str) -> None:
        print(f"Simulating sending an SMS notification")
        

class NotificationAdapter(NewNotificationSystem):
    def __init__(self, obj: LegacyNotificationSystem) -> None:
        self.__obj = obj
        
    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        # transform email notification to SMS notification
        phoneNumber = self.get_phone_number_from_email(emailAddress)
        message = self.format_email_as_sms(subject, body)
        self.__obj.send_sms_notification(phoneNumber, message)
        
    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        # transform push notification to SMS notification
        phoneNumber = self.get_phone_number_from_device_token(deviceToken)
        sms_message = self.format_push_as_sms(title, message)
        self.__obj.send_sms_notification(phoneNumber, sms_message)
        
    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        # transform social media update to SMS notification
        phoneNumber = self.get_phone_number_for_social_media(social_media_platform)
        sms_message = self.format_social_media_as_sms(social_media_platform, postContent)
        self.__obj.send_sms_notification(phoneNumber, sms_message)
        
    def get_phone_number_from_email(self, emailAddress: str) -> str:
        return "+1-555-0100"
    
    def get_phone_number_from_device_token(self, deviceToken: str) -> str:
        return "+1-555-0200"
    
    def get_phone_number_for_social_media(self, social_media_platform: str) -> str:
        return "+1-555-0300"
    
    def format_email_as_sms(self, subject: str, body: str) -> str:
        return f"Email - {subject}: {body[:100]}"
    
    def format_push_as_sms(self, title: str, message: str) -> str:
        return f"Push - {title}: {message}"
    
    def format_social_media_as_sms(self, platform: str, postContent: str) -> str:
        return f"{platform} - {postContent}"
    

class NotificationFactory:
    
    @staticmethod
    def get_notification_system() -> NewNotificationSystem:
        return NotificationAdapter(LegacyNotificationSystem())
    

def main():
    
    notification_system = NotificationFactory.get_notification_system()
    
    notification_system.send_email_notification(
        "user@example.com", 
        "Welcome", 
        "Welcome to our service! We're glad to have you."
    )
    
    notification_system.sendPushNotification(
        "device_token_12345", 
        "New Message", 
        "You have a new message from John"
    )
    
    notification_system.send_social_media_update(
        "Twitter", 
        "Just launched our new product! Check it out at our website. #ProductLaunch #Innovation"
    )
    
if __name__ == "__main__":
    main()