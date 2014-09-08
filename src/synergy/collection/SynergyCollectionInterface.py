class SynergyCollectionInterface(object):
  
  def __init__(self):
    self._objects = []
  
  def getComputableObjects(self):
    raise NotImplementedError