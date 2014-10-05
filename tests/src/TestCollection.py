from src.synergy.collection.SynergyCollection import SynergyCollection

class TestCollection(SynergyCollection):

  def objectCycle(self, obj, context):
    # Si il n'a plus aucun ami avec des haricots, il se suicide
    friends_with_beans_count = 0
    for collection in context.getCollections():
      for friend in collection.getObjects():
        if friend.beans > 1:
          friends_with_beans_count += 1
    if friends_with_beans_count == 0:
      obj.setWill('die')

    # L'objet multiplie ses haricots
    obj.beans = obj.beans ** obj.coeff

  def cycle(self, context):
    super(TestCollection, self).cycle(context)

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