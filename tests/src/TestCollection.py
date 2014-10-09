from src.synergy.collection.SynergyCollection import SynergyCollection
from tests.src.event.TooMuchBeansAction import TooMuchBeansAction
from tests.src.event.MakeBeansProfitAction import MakeBeansProfitAction
from tests.src.event.LonelinessSuicideAction import LonelinessSuicideAction

class TestCollection(SynergyCollection):

  def __init__(self, configuration):
    super(TestCollection, self).__init__(configuration)
    # TODO: Construire dynamiquement les steps en fonction de dependences exprime dans le action
    self._actions_steps = [
      [MakeBeansProfitAction],
      [TooMuchBeansAction],
      [LonelinessSuicideAction]
    ]
