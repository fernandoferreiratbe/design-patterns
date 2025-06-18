import logging

from src.strategy.interface.notification_strategy import NotificationProvider

logger = logging.getLogger(__name__)



class WhatsappNotificationServiceProvider(NotificationProvider):
    """This class will be used to send a notification to the user via whatsapp"""
    
    def notify(self, message: str) -> None:
        """This method will notify the user with the given message"""
        logger.info(f"Sending whatsapp notification to the user with the message: {message}")

