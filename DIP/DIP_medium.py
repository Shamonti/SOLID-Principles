# 🎯 Medium Challenge: Payment System
# Create an interface PaymentGateway with method pay(amount).

# Implement:

# StripePayment

# PayPalPayment

# Create a CheckoutService that processes payments depending on PaymentGateway.

# Simulate paying with both Stripe and PayPal.

# ✅ Hint: Dependency Injection = pass the gateway to service constructor.


# 1. Abstract Interface
class PaymentGateway:
    def pay(self, amount):
        pass


# 2. Concrete implementation
class StripePayment(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Paying with Stripe: ${amount}"


class PayPalPayment(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Paying with PayPal: ${amount}"


# 3. High level service depends on implementation
class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def make_payment(self, amount):
        return self.payment_gateway.pay(amount)


stripe_payment = PaymentProcessor(StripePayment())
print(stripe_payment.make_payment("500"))
stripe_payment = PaymentProcessor(PayPalPayment())
print(stripe_payment.make_payment("500"))
