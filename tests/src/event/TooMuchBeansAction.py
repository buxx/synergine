from src.synergy.event.Action import Action
from tests.src.event.TooMuchBeansEvent import TooMuchBeansEvent

class TooMuchBeansAction(Action):

  _listen = TooMuchBeansEvent

  def run(self, collection, context):
    self._obj.beans = 0
