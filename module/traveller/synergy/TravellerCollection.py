from synergine.src.synergy.collection.SynergyCollection import SynergyCollection
from module.traveller.event.MoveAction import MoveAction
from module.traveller.event.TurnFinishedAction import TurnFinishedAction


class TravellerCollection(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        # TODO: Ajouter une action qui réduit l'intensité des traces chaque tour
        self._actions = [MoveAction, TurnFinishedAction]
