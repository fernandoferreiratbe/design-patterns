"""This service will be used to notify the user with the given message using different notification strategies"""

from typing import Dict, Type
from .notification_strategy import (
    NotificationStrategy,
    EmailNotification,
    WhatsAppNotification,
    TelegramNotification,
    DiscordNotification,
    SlackNotification,
    InstagramNotification,
    TwitterNotification
)

class NotificationService:
    """NotificationService using the strategy pattern to handle different notification channels"""
    
    def __init__(self):
        # Initialize the available strategies
        self._strategies: Dict[str, Type[NotificationStrategy]] = {
            "email": EmailNotification,
            "whatsapp": WhatsAppNotification,
            "telegram": TelegramNotification,
            "discord": DiscordNotification,
            "slack": SlackNotification,
            "instagram": InstagramNotification,
            "twitter": TwitterNotification
        }
    
    def notify(self, message: str, channel: str) -> None:
        """
        Notify using the specified channel
        
        Args:
            message: The message to send
            channel: The notification channel to use
        
        Raises:
            ValueError: If the channel is not supported
        """
        try:
            # Get the strategy class for the channel
            strategy_class = self._strategies[channel]
            # Create an instance of the strategy
            strategy = strategy_class()
            # Use the strategy to send the notification
            strategy.notify(message)
        except KeyError:
            raise ValueError(f"Invalid channel: {channel}") 