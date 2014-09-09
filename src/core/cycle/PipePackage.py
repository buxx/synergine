from lib.process.processmanager import PipePackage as BasePipePackage

class PipePackage(BasePipePackage):
  
  def setContext(self, context):
    self._context = context
  
  def getContext(self):
    return self._context