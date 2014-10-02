from src.synergy.collection.SynergyCollection import SynergyCollection

class TestCollection(SynergyCollection):
  
  def compute(self, context):
    super(TestCollection, self).compute(context)

    # Suppression des morts
    new_objects = []
    for obj in self.getObjects():
      if obj.getWill() != 'die':
        new_objects.append(obj)
    self._objects = new_objects

    # Confiscation des haricots
    for obj in self.getObjects():
      if obj.beans > 10000000:
        obj.beans = 0