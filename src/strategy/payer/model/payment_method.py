from enum import Enum


class PaymentMethod(Enum):
    CreditCardPayment = "CreditCardPayment"
    DebitCardPayment = "DebitCardPayment"
    PixPayment = "PixPayment"

