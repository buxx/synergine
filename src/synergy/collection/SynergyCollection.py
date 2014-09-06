class SynergyCollection(object):
  
  def __init__(self):
    self._objects = ['Foo', 'Bar']
  
  def getComputableObjects(self):
    return self._objects