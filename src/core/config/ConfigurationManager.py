class ConfigurationManager(object):
  
  def __init__(self, config):
    self._configs = config
  
  # TODO: systeme de recupe avec simulation.collections
  def getInitialCollectionsClasss(self):
    return self._configs['simulation']['collections']
  
  # TODO: systeme de recupe avec engine.maxfps
  def getMaxFpsEngine(self):
    return self._configs['engine']['fpsmax']
  
  # TODO: systeme de recupe avec display.displays
  def getDisplayClasss(self):
    return self._configs['display']['displays']