from src.strategy.payer.interface.payment_abstraction import Payment
from src.strategy.payer.model.models import Bill
from src.strategy.payer.model.payment_status import PaymentStatus


class PaymentExecutor:

    @staticmethod
    def execute_payment(payment_service: Payment, bill: Bill) -> PaymentStatus:
        return payment_service.pay(bill=bill)
