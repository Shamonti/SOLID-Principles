# ❌ Bad Design: Without DIP
# class EmailSender:
#     def send_email(self, message):
#         return f"Sending email: {message}"


# class NotificationService:
#     def __init__(self):
#         self.sender = EmailSender()  # tightly coupled

#     def notify(self, message):
#         return self.sender.send_email(message)


# # Usage
# service = NotificationService()
# print(service.notify("Welcome!"))


# ✅ Good Design: With DIP
# 1. Abstract Interface
class NotificationSender:
    def send(self, message):
        pass


# 2. Concrete implementation
class EmailSender(NotificationSender):
    def send(self, message):
        return f"Sending email: {message}"


class SMSSender(NotificationSender):
    def send(self, message):
        return f"Sending sms: {message}"


# High level service depends on implementation
class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message):
        return self.sender.send(message)


email_service = NotificationService(EmailSender())
print(email_service.notify("Welcome to my Email!"))

sms_service = NotificationService(SMSSender())
print(sms_service.notify("Welcome to my SMS!"))
