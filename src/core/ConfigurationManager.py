class ConfigurationManager(object):
  
  def __init__(self):
    self._configs = {
      'simulation' : {
        'synergies': [
          {
            'class': 'BaseSynergyCollection'
          }
        ]
      }
    }