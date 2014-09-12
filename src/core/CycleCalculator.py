from lib.process.processmanager import KeepedAliveProcessManager
from src.core.cycle.PipePackage import PipePackage

# TODO: tmp ...
from os import getpid

class CycleCalculator(object):
  
  def __init__(self, force_main_process = False):
    # TODO: nbprocess
    self._force_main_process = force_main_process
    self._process_manager = KeepedAliveProcessManager(nb_process=2, target=self._process_compute)
  
  def computeCollections(self, collections, context):
    for collection in collections:
      pipe_package = self._getPipePackageForCollection(collection, context)
      if not self._force_main_process:
        computeds_objects = self._process_manager.get_their_work(pipe_package)
      else:
        computeds_objects = self._process_compute(pipe_package)
      collection.setObjects(computeds_objects)
      
    for collection in collections:
      #import pdb; pdb.set_trace()
      collection.compute(context)
      #map = context.getMap()
      #for map_coo in map:
      #  if len(map[map_coo]) > 1:
      #    import pdb; pdb.set_trace()
      #    raise Exception('Plus dun !')
      #  obj = map[map_coo][0]
      #  print('map object will: ', obj.getWill())
      for obj in collection.getObjects():
        print('col object will: ', obj.getWill())
        if obj.getWill() == 'die':
          # HACK: On ne devrait avoir AUCUN oject qui dit qu'il va mourrir.
          # car la collection doit avoir fait son menage dans ses objets.
          # trouver pk !
          #pass
          collection._objects.remove(obj)
  
  def _getPipePackageForCollection(self, collection, context):
    # FUTURE: test si garder le package en attribut de core ameliore les perfs (attention a l'index de current_process)
    pipe_package = PipePackage(collection.getComputableObjects())
    pipe_package.setContext(context)
    return pipe_package
  
  def _process_compute(self, pipe_package):
    objects_to_compute = pipe_package.getChunkedObjects()
    for object in objects_to_compute:
      object.cycle(pipe_package.getContext())
      object.test = getpid()
    return objects_to_compute
      
  def end(self):
    self._process_manager.stop()