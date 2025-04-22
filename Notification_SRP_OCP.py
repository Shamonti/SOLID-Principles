from abc import ABC, abstractmethod

class Notification:
  def __init__(self, message="Hello, user!"):
    self.message = message

class NotificationSender(ABC):
  @abstractmethod
  def send(self, message: str):
    pass

class EmailSender(NotificationSender):
  def send(self, message: str):
    print(f"Sending email: {message}")
    return f"Email sent: {message}"

class NotificationDisplay:
  def display(self, sender: NotificationSender, message: str):
    result = sender.send(message)
    print(f"Displayed: {result}")

notification = Notification("Hello, user!")
email_sender = EmailSender()
display = NotificationDisplay()
display.display(email_sender, notification.message)
