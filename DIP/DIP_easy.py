# 🎯 Easy Challenge: EmailSender + SMSSender
# Create an abstract class MessageSender with a method send_message.

# Implement two classes:

# EmailSender

# SMSSender

# Write a Notification class that depends on MessageSender (not specific Email/SMS).

# Test both Email and SMS without changing Notification.

# ✅ Hint: Like the DIP Email example earlier.


# 1. Abstract Interface
class MessageSender:
    def send_message(self, message):
        pass


# 2. Concrete Implementation
class EmailSender(MessageSender):
    def send_message(self, message):
        return f"Email Message: {message}"


class SMSSender(MessageSender):
    def send_message(self, message):
        return f"SMS Message: {message}"


# 3. High level service depends on implementation
class Notification:
    def __init__(self, message_sender: MessageSender):
        self.message_sender = message_sender

    def notify(self, message):
        return self.message_sender.send_message(message)


email_notification = Notification(EmailSender())
print(email_notification.notify("Welcome to my Email!"))

sms_notification = Notification(SMSSender())
print(sms_notification.notify("Welcome to my SMS!"))
