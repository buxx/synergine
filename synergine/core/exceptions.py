class EventException(Exception):
    pass


class NotConcernedEvent(EventException):
    pass


class UselessMechanism(EventException):
    pass