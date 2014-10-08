from src.synergy.Simulation import Simulation
from module.lifegame.synergy.object.Cell import Cell

class LifeGameSimulation(Simulation):

  def __init__(self, collections):
    super(LifeGameSimulation, self).__init__(collections)

  def run_collection_cycle(self, collection, context):
    for cell in collection.getObjects():
      if cell.getWill() == 'die':
        cell.set_alive(False)
      elif cell.getWill() == 'born':
        cell.set_alive(True)

  def run_simulation_cycle(self, context):
    pass