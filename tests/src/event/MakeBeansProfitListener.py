from src.synergy.event.Listener import Listener
from tests.src.event.MakeBeansProfitEvent import MakeBeansProfitEvent

class MakeBeansProfitListener(Listener):

  _listen = MakeBeansProfitEvent

  def run(self, collection, context):
    self._obj.beans = self._obj.beans ** self._obj.coeff

