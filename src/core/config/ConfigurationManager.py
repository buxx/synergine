class ConfigurationManager(object):
  
  def __init__(self, config):
    self._configs = config
  
  def getInitialCollectionsClasss(self):
    return self._configs['simulation']['collections']