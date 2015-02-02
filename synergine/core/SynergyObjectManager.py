from synergine.core.Map import Map
from synergine.core.Signals import Signals
from synergine.synergy.collection.SynergyCollection import SynergyCollection


class SynergyObjectManager():
    #todo refactoriser getcoll
    #todo renommer en synergy manager

    def __init__(self, simulations):
        self._simulations = simulations
        for simulation in self._simulations:
            for collection in simulation.get_collections():
                collection.initialize_objects()
        self._map = Map()
        self._initialize_map()
        Signals.signal(SynergyCollection.SIGNAL_ADD_OBJECT).connect(self._collection_add_object)
        Signals.signal(SynergyCollection.SIGNAL_REMOVE_OBJECT).connect(self._collection_remove_object)

    def _initialize_map(self):
        for obj in self.get_objects():
            self._map.add_object(obj)

    def _collection_add_object(self, collection, obj):
        self._map.add_object(obj)

    def _collection_remove_object(self, collection, obj):
        self._map.remove_object(obj)

    def get_simulations(self):
        return self._simulations

    def get_collections(self):
        collections = []
        for simulation in self._simulations:
            for collection in simulation.get_collections():
                collections.append(collection)
        return collections

    def get_computable_objects(self):
        computable_objects = []
        for simulation in self._simulations:
            for collection in simulation.get_collections():
                for collection_computable_object in collection.get_computable_objects():
                    computable_objects.append(collection_computable_object)
        return computable_objects

    def get_objects(self):
        objects = []
        for simulation in self._simulations:
            for collection in simulation.get_collections():
                for collection_object in collection.get_objects():
                    objects.append(collection_object)
        return objects

    def get_objects_by_type(self, type):
        objects_filtereds = []
        for obj in self.get_objects():
            if isinstance(obj, type):
                objects_filtereds.append(obj)
        return objects_filtereds

    def getObjectActions(self):
        actions = []
        for simulation in self._simulations:
            for action in simulation.get_object_actions():
                actions.append(action)
        return actions

    def getGlobalActions(self):
        actions = []
        for simulation in self._simulations:
            for action in simulation.get_global_actions():
                actions.append(action)
        return actions

    # todo: la func ci-dessous sont-elles a leurs place ?
    def get_objects_to_display(self):
        objects_to_display = []
        for simulation in self._simulations:
            for collection in simulation.get_collections():
                for collection_object_to_display in collection.get_objects_to_display():
                    objects_to_display.append(collection_object_to_display)
        return objects_to_display

    def get_map(self):
        return self._map