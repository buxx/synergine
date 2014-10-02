from src.synergy.object.SynergyObject import SynergyObject

class TestSynergyObject(SynergyObject):
  
  # TODO: Une méthode setUp parente pour normaliser ?
  def setUp(self, name, beans, coeff):
    self.name = name
    self.beans = beans
    self.coeff = coeff
  
  def cycle(self, context):
    # Si il n'a plus aucun ami avec des haricots, il se suicide
    friends_with_beans_count = 0
    for collection in context.getCollections():
      for friend in collection.getObjects():
        if friend.beans > 1:
          friends_with_beans_count += 1
    if friends_with_beans_count == 0:
      self.setWill('die')

    # L'objet multiplie ses haricots
    self.beans = self.beans ** self.coeff