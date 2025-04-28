# Hard: In Django, design a UserNotification system
# Imagine you have different user notification types:

# EmailNotification

# SMSNotification

# PushNotification

# Problem:
# Different notification types need different setup:

# Email needs setup_smtp_server()

# SMS needs setup_sms_gateway()

# Push notification needs setup_push_service()

# Tasks:

# How would you design it to follow ISP, so that a PushNotification class isn't forced to implement setup_smtp_server()?

# ✅ Your design should allow adding new notification types later without modifying existing ones.


class SMTPServerConfigInterface:
    def setup_smtp_server(self):
        pass


class SMSGatewayConfigInterface:
    def sms_gateway_processor(self):
        pass


class PushServiceConfigInterface:
    def setup_push_service(self):
        pass


class EmailNotification(SMTPServerConfigInterface):
    def setup_smtp_server(self):
        return "Configuring SMTP server"


class SMSNotification(SMSGatewayConfigInterface):
    def sms_gateway_processor(self):
        return "Configuring sms gateway server."


class PushNotification(PushServiceConfigInterface):
    def setup_push_service(self):
        return "Configuring push server."


print(PushNotification().setup_push_service())
