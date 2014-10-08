from src.synergy.Simulation import Simulation

class TestSimulation(Simulation):

  def __init__(self, collections):
    super(TestSimulation, self).__init__(collections)

  def run_object_cycle(self, obj, context):
    # Si il n'a plus aucun ami avec des haricots, il se suicide
    # friends_with_beans_count = 0
    # for collection in context.getCollections():
    #   for friend in collection.getObjects():
    #     if friend.beans > 1:
    #       friends_with_beans_count += 1
    # if friends_with_beans_count == 0:
    #   obj.setWill('die')

    # L'objet multiplie ses haricots
    #obj.beans = obj.beans ** obj.coeff
    pass

  def run_collection_cycle(self, collection, context):
    # Suppression des morts
    new_objects = []
    for obj in collection.getObjects():
      if obj.getWill() != 'die':
        new_objects.append(obj)
    collection._objects = new_objects  # TODO: setObjects sur collection

    # # Confiscation des haricots
    # for obj in collection.getObjects():
    #   if obj.beans > 10000000:
    #     obj.beans = 0

  def run_simulation_cycle(self, context):
    pass