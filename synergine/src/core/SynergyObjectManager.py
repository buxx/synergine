class SynergyObjectManager():
    #todo refactoriser getcoll
    #todo renommer en synergy manager

    def __init__(self, simulations):
        self._simulations = simulations

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