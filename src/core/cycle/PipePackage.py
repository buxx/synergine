from lib.process.processmanager import PipePackage as BasePipePackage

class PipePackage(BasePipePackage):
  
  def setMap(self, map):
    self._map = map
  
  def getMap(self):
    return self._map