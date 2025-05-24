""" This class will be used to manage the notification service """

from src.strategy.service.provider.email_notification_service_provider import EmailNotificationServiceProvider
from src.strategy.service.provider.whatsapp_notification_service_provider import WhatsappNotificationServiceProvider
from src.strategy.service.provider.discord_notification_service_provider import DiscordNotificationServiceProvider
from src.strategy.service.provider.slack_notification_service_provider import SlackNotificationServiceProvider
from src.strategy.service.provider.instragram_notification_service_provider import InstagramNotificationServiceProvider
from src.strategy.service.provider.telegram_notification_service_provider import TelegramNotificationServiceProvider

class NotificationServiceStrategy:
    """ This class will be used to manage the notification service """
    
    def __init__(self):
        self.notification_providers = {
            "email": EmailNotificationServiceProvider(),
            "whatsapp": WhatsappNotificationServiceProvider(),
            "discord": DiscordNotificationServiceProvider(),
            "slack": SlackNotificationServiceProvider(),
            "instagram": InstagramNotificationServiceProvider(),
            "telegram": TelegramNotificationServiceProvider(),
        }

    def send_notification(self, message: str, channel: str) -> None:
        """This method will send a notification to the user via the given channel"""
        if channel not in self.notification_providers:
            raise ValueError(f"Invalid channel: {channel}")
        
        self.notification_providers[channel].notify(message)
