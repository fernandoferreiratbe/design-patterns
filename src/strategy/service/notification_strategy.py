from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class NotificationStrategy(ABC):
    """Abstract base class defining the strategy interface for notifications"""
    
    @abstractmethod
    def notify(self, message: str) -> None:
        """Send notification with the given message"""
        pass

class EmailNotification(NotificationStrategy):
    def notify(self, message: str) -> None:
        logger.info(f"Sending email notification to the user with the message: {message}")

class WhatsAppNotification(NotificationStrategy):
    def notify(self, message: str) -> None:
        logger.info(f"Sending whatsapp notification to the user with the message: {message}")

class TelegramNotification(NotificationStrategy):
    def notify(self, message: str) -> None:
        logger.info(f"Sending telegram notification to the user with the message: {message}")

class DiscordNotification(NotificationStrategy):
    def notify(self, message: str) -> None:
        logger.info(f"Sending discord notification to the user with the message: {message}")

class SlackNotification(NotificationStrategy):
    def notify(self, message: str) -> None:
        logger.info(f"Sending slack notification to the user with the message: {message}")

class InstagramNotification(NotificationStrategy):
    def notify(self, message: str) -> None:
        logger.info(f"Sending instagram notification to the user with the message: {message}")

class TwitterNotification(NotificationStrategy):
    def notify(self, message: str) -> None:
        logger.info(f"Sending twitter notification to the user with the message: {message}") 