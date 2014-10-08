from lib.process.processmanager import PipePackage as BasePipePackage

class PipePackage(BasePipePackage):
  
  def setContext(self, context):
    self._context = context
  
  def getContext(self):
    return self._context

  def setMechanisms(self, mechanisms):
    self._mechanisms = mechanisms

  def getMechanisms(self):
    return self._mechanisms