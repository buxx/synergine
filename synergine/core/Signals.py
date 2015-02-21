from synergine.core.Signal import Signal


class Signals:

    _signals = {}

    @classmethod
    def signal(cls, signal_id):
        try:
            return cls._signals[signal_id]
        except KeyError:
            cls._signals[signal_id] = Signal()
            return cls._signals[signal_id]

    @classmethod
    def reset(cls):
        cls._signals = {}