from src.synergy.collection.SynergyCollection import SynergyCollection

class TestCollection(SynergyCollection):
  
  def compute(self, context):
    super(TestCollection, self).compute(context)
    for obj in self.getObjects():
      if obj.beans > 10000000:
        obj.beans = 0