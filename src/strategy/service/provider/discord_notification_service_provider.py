from src.strategy.interface.notification_strategy import NotificationProvider


class DiscordNotificationServiceProvider(NotificationProvider):
    """This class will be used to send a notification to the user via discord"""
    
    def notify(self, message: str) -> None:
        """This method will notify the user with the given message"""
        logger.info(f"Sending discord notification to the user with the message: {message}")
