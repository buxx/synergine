class EventException(Exception):
    """

    Event related Exception

    """
    pass


class NotConcernedEvent(EventException):
    """

    Exception raised when concerned ``SynergyObject`` is not concerned by Event.

    """
    pass


class UselessMechanism(EventException):
    """
    Exception raised when concerned ``SynergyObject`` is not concerned by this Mechanism.
    """
    pass