from abc import ABC, abstractmethod

from src.strategy.payer.model.models import Bill
from src.strategy.payer.model.payment_status import PaymentStatus


class Payment(ABC):

    @abstractmethod
    def pay(self, bill: Bill) -> PaymentStatus:
        ...
