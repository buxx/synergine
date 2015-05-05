from synergine.core.config.ConfigurationManager import ConfigurationManager
from synergine.core.Signals import Signals
from synergine.lib.eint import IncrementedNamedInt


class SynergyCollection:
    """
    Object containing list of SynergyObject and some logical actions listing what
    concern this collection.
    """

    SIGNAL_ADD_OBJECT = 'collection.add_object'
    SIGNAL_REMOVE_OBJECT = 'collection.remove_object'

    def __init__(self, configuration: ConfigurationManager):
        self._configuration = configuration
        self._objects = []
        self._actions = []
        self._id = IncrementedNamedInt.get(self)

    def get_id(self):
        return self._id

    def initialize_objects(self, context):
        self.set_objects(self._configuration.get_start_objects(self, context))
        for obj in self._objects:
            obj.initialize()

    def get_actions(self) -> list:
        return self._actions

    def get_objects(self) -> list:
        return self._objects

    def set_objects(self, objects: list):
        for obj in objects:
            try:
                self._objects.index(obj)
            except ValueError:
                Signals.signal(self.SIGNAL_ADD_OBJECT).send(collection=self, obj=obj)
                self._objects.append(obj)

    def remove_object(self, obj):
        Signals.signal(self.SIGNAL_REMOVE_OBJECT).send(collection=self, obj=obj)
        self._objects.remove(obj)

    def add_object(self, obj):
        self._objects.append(obj)
        Signals.signal(self.SIGNAL_ADD_OBJECT).send(collection=self, obj=obj)

    def get_computable_objects(self) -> list:
        """
        TODO: Implementer un processus generique pour que les SynergyObject
        puissent n'etre execute que tous les x cycles
        :return: object who are computable
        """
        return self._objects

    def get_objects_to_display(self) -> list:
        """
        :return: object to display by Display object
        """
        return self._objects
