from synergine.src.synergy.collection.SynergyCollectionInterface import SynergyCollectionInterface
from synergine.src.synergy.object.SynergyObject import SynergyObject
from synergine.src.core.config.ConfigurationManager import ConfigurationManager


class SynergyCollection(SynergyCollectionInterface):
    """
    Object containing list of SynergyObject and some logical actions listing what
    concern this collection.
    """

    def __init__(self, configuration: ConfigurationManager):
        self._configuration = configuration
        self._objects = self._configuration.get_start_objects()
        self._actions = []

    def get_actions(self) -> list:
        return self._actions

    def get_objects(self) -> list:
        return self._objects

    def set_objects(self, objects: list):
        self._objects = objects

    def remove_object(self, obj: SynergyObject):
        self._objects.remove(obj)

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
