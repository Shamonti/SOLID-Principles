# Medium: Build a Payment system following ISP
# You need to create a payment system with three different payment types:

# CashPayment

# CreditCardPayment

# BitcoinPayment

# Each payment type has different methods:

# Cash needs only pay()

# CreditCard needs pay() + validate_card()

# Bitcoin needs pay() + check_wallet_balance()

# Tasks:

# Design it in a way that no class is forced to implement unnecessary methods.

# ✅ Follow ISP by splitting responsibilities.


class PaymentProcessor:
    def process_payment(self):
        pass


class CardValidator:
    def validate_card(self):
        pass


class WalletBalanceChecker:
    def check_wallet_balance(self):
        pass


class CashPayment(PaymentProcessor):
    def process_payment(self):
        return "Paying"


class CreditCardPayment(PaymentProcessor, CardValidator):
    def process_payment(self):
        return "Paying"

    def validate_card(self):
        return "Validating card"


class BitcoinPayment(PaymentProcessor, WalletBalanceChecker):
    def pay(self):
        return "Paying"

    def check_wallet_balance(self):
        return "Checking wallet balance"


print(BitcoinPayment().check_wallet_balance())
