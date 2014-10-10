from src.synergy.collection.SynergyCollectionInterface import SynergyCollectionInterface
from src.synergy.object.SynergyObject import SynergyObject

class SynergyCollection(SynergyCollectionInterface):

    def __init__(self, configuration):
        self._configuration = configuration
        self._objects = self._configuration.get_start_objects()
        self._actions = []

    def get_actions(self):
        return self._actions

    def get_objects(self):
        return self._objects

    def set_objects(self, objects):
        self._objects = objects

    def remove_object(self, object):
        self._objects.remove(object)

    def get_object_by_key(self, key):
        return self._objects[key]

    def get_computable_objects(self):
        return self._objects

    def get_objects_to_display(self):

        #import pdb; pdb.set_trace()
        return self._objects
