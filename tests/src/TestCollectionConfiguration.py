from src.synergy.collection.Configuration import Configuration
from tests.src.TestSynergyObject import TestSynergyObject

class TestCollectionConfiguration(Configuration):
  
  def getStartObjects(self):
    objs_setup = (
      ('john', 2, 2),
      ('boby', 2, 5),
      ('cora', 2, 10),
      ('mara', 2, 20),
    )
    
    objects = []
    for obj_setup in objs_setup:
      obj = TestSynergyObject()
      obj.setUp(obj_setup[0], obj_setup[1], obj_setup[2])
      objects.append(obj)
    
    return objects