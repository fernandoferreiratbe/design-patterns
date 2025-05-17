from src.strategy.interface.notification_strategy import NotificationProvider


class TelegramNotificationServiceProvider(NotificationProvider):
    """This class will be used to send a notification to the user via telegram"""
    
    def notify(self, message: str) -> None:
        """This method will notify the user with the given message"""
        logger.info(f"Sending telegram notification to the user with the message: {message}")
