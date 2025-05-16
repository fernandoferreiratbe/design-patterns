"""This service will be used to notify the user with the given message and a messager type"""

logger = logging.getLogger(__name__)


class NotificationService:
    """ This implementation has too much if statements, and it's not scalable.
    We should use the strategy pattern to avoid this problem.
    """
    
    def notify(self, message: str, channel: str) -> None:
        """This method will notify the user with the given message and a messager type"""
        if channel == "email":
            logger.info(f"Sending email notification to the user with the message: {message}")
        elif channel == "whatsapp":
            logger.info(f"Sending whatsapp notification to the user with the message: {message}")
        elif channel == "telegram":
            logger.info(f"Sending telegram notification to the user with the message: {message}")
        elif channel == "discord":
            logger.info(f"Sending discord notification to the user with the message: {message}")
        elif channel == "slack":
            logger.info(f"Sending slack notification to the user with the message: {message}")
        elif channel == "instagram":
            logger.info(f"Sending instagram notification to the user with the message: {message}")
        elif channel == "twitter":
            logger.info(f"Sending twitter notification to the user with the message: {message}")
        else:
            raise ValueError(f"Invalid channel: {channel}")
