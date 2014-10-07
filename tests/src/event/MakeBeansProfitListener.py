from src.synergy.event.Listener import Listener
from tests.src.event.MakeBeansProfitEvent import MakeBeansProfitEvent

class MakeBeansProfitListener(Listener):

  _listen = MakeBeansProfitEvent

  def trigged(self, obj, context, parameters):
    # L'objet multiplie ses haricots
    obj.beans = obj.beans ** obj.coeff  # TODO: On doit avoir une Action (future) ici pour que ce soit traite en dehors du processus

