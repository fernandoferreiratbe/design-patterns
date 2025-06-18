from src.strategy.payer.factory.payment_method_factory import PaymentMethodFactory
from src.strategy.payer.model.models import Bill
from src.strategy.payer.model.payment_method import PaymentMethod
from src.strategy.payer.payment_executor import PaymentExecutor


payment_executor = PaymentExecutor()
payment_factory = PaymentMethodFactory()

for payment_method in PaymentMethod:
    payment_service = payment_factory.payment_by(payment_method=payment_method)
    payment_executor.execute_payment(payment_service=payment_service, bill=Bill(value=29.9, description="Test"))

