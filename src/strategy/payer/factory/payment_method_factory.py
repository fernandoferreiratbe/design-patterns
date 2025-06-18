from src.strategy.payer.model.payment_method import PaymentMethod
from src.strategy.payer.service.credit_card_payment_service import CreditCardPaymentService
from src.strategy.payer.service.debit_card_payment_service import DebitCardPaymentService
from src.strategy.payer.service.pix_payment_service import PixPaymentService


class PaymentMethodFactory:

    def __init__(self):
        self.payment_methods = {
            PaymentMethod.PixPayment: PixPaymentService(),
            PaymentMethod.DebitCardPayment: DebitCardPaymentService(),
            PaymentMethod.CreditCardPayment: CreditCardPaymentService()
        }

    def payment_by(self, payment_method):
        if payment_method not in self.payment_methods:
            raise ValueError(f"Payment method {payment_method} informed is invalid!")

        return self.payment_methods.get(payment_method)