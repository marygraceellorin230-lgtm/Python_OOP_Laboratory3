from abc import ABC, abstractmethod


# Abstract Class
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


# Email Notification
class EmailNotification(Notification):

    def send(self, message):
        print(f"Sending Email: {message}")


# SMS Notification
class SMSNotification(Notification):

    def send(self, message):
        print(f"Sending SMS: {message}")


# App Notification
class AppNotification(Notification):

    def send(self, message):
        print(f"Sending App Notification: {message}")


# Create a list of notification objects
notifications = [
    EmailNotification(),
    SMSNotification(),
    AppNotification()
]


# Send the announcement
message = "Enrollment is now open!"

for notification in notifications:
    notification.send(message)