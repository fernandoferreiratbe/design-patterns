from src.strategy.payer.interface.payment_abstraction import Payment
from src.strategy.payer.model.models import Bill
from loguru import logger

from src.strategy.payer.model.payment_status import PaymentStatus


class CreditCardPaymentService(Payment):

    def pay(self, bill: Bill) -> PaymentStatus:
        logger.info("Executing Credit Card Payment Service...")
        return PaymentStatus.PENDENT
