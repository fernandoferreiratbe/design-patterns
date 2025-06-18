from enum import Enum


class PaymentStatus(Enum):
    SUCCESS = "Success"
    FAILED = "Failed"
    PENDENT = "Pendent"
