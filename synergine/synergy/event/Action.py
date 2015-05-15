class Action():
    """
    ``Action`` own the code intended for modify synergies objects.
    """

    _listen = None
    """The ``Event`` class to listen."""
    _depend = []
    """List of ``Action`` who need to be executed before this."""

    @classmethod
    def get_listened_class(cls):
        """

        :return: The listened ``Event`` class.
        :rtype: synergine.synergy.Event.Event
        """
        return cls._listen

    @classmethod
    def get_dependencies(cls):
        """

        :return: List of ``Action`` who need to be executed before this.
        :rtype: list (of ``Action``)
        """
        return cls._depend

    def __init__(self, object_id, parameters):
        self._object_id = object_id
        self._parameters = parameters

    def get_object_id(self):
        """

        :return: The concerned synergy object id
        :rtype: int
        """
        return self._object_id

    def run(self, obj, context, synergy_manager):
        """

        The execution code of ``Action`` have to be write in ``run`` method.

        :param obj: The synergy concerned object
        :param context: The Context
        :param synergy_manager: SynergyObjectManager
        :return:
        """
        raise NotImplementedError