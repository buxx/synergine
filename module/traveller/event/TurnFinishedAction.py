from synergine.src.synergy.event.Action import Action
from module.traveller.event.AllTownVisitedEvent import AllTownVisitedEvent


class TurnFinishedAction(Action):
    """
    Depose la trace de pheromone sur le parcour:
    Trace plus forte si le parcour est plus rapide que le précedent
    """

    _listen = AllTownVisitedEvent

    def run(self, collection, context):
        """

        :param collection:
        :param context:
        :return:
        """
        # TODO: Manipuler Context pour mettre les intensités de pheromones
        pass