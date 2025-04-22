# Medium Build a Notification base class with EmailNotification, SMSNotification, and SlackNotification. Ensure none of them break if substituted.
class Notification:
  def send(self):
    raise NotImplementedError

class EmailNotification(Notification):
  def send(self):
    return "I send emails."

class SMSNotification(Notification):
  def send(self):
    return "I send sms."

class SlackNotification(Notification):
  def send(self):
    return "I send slack messages."

def send_notification(notification: Notification):
  print(notification.send())

send_notification(SMSNotification())
send_notification(SlackNotification())
send_notification(EmailNotification())