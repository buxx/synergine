from lib.process.processmanager import PipePackage as BasePipePackage

class PipePackage(BasePipePackage):
  
  def setContext(self, context):
    self._context = context
  
  def getContext(self):
    return self._context

  def setCurrentCollection(self, collection):
    self._collection = collection

  def getCurrentCollection(self):
    return self._collection