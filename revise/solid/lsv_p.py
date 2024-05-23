from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class ContactInfo:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    contact = ContactInfo(name='Huynh Phuc', email='john@test.com', phone='0972-123-123')

    email_notify = Email(contact.email)
    sms_notify = SMS(contact.phone)

    notification_manager = NotificationManager(sms_notify)
    notification_manager.send('Hello Phuc')

    notification_manager.notification = email_notify
    notification_manager.send('Hi Phuc')
