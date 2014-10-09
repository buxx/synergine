class SynergyCollectionInterface():
  
  def getComputableObjects(self):
    raise NotImplementedError

  def cycle(self, context):
    raise NotImplementedError