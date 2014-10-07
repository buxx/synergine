
class Simulation(object):

  def __init__(self, collections):
    self._collections = collections
    self._object_listeners = []
    self._global_listeners = []

  def getCollections(self):
    return self._collections

  def run_object_cycle(self, object, context):
    raise NotImplementedError

  def run_collection_cycle(self, collection, context):
    raise NotImplementedError

  def run_simulation_cycle(self, context):
    raise NotImplementedError

  def get_object_listeners(self):
    return self._object_listeners

  def get_global_listeners(self):
    return self._global_listeners