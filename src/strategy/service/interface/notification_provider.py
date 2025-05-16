from abc import ABC, abstractmethod

class NotificationProvider(ABC):
    """This interface will define the abstract behavior of a notification strategy""" 

    @abstractmethod
    def notify(self, message: str) -> None:
        """This method will notify the user with the given message"""
        ...
