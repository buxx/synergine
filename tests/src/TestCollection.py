from src.synergy.collection.SynergyCollection import SynergyCollection
from tests.src.event.TooMuchBeansListener import TooMuchBeansListener
from tests.src.event.MakeBeansProfitListener import MakeBeansProfitListener
from tests.src.event.LonelinessSuicideListener import LonelinessSuicideListener

class TestCollection(SynergyCollection):

  def __init__(self, configuration):
    super(TestCollection, self).__init__(configuration)
    # TODO: Construire dynamiquement les steps en fonction de dependences exprime dans le listener
    self._listeners_steps = [
      [MakeBeansProfitListener()],
      [TooMuchBeansListener()],
      [LonelinessSuicideListener()]
    ]
