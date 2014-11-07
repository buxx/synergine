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
        # TODO: Reinitialiser towns de traveller
        foo = 'bar'

        route_towns = self._obj.get_towns()
        pheromon_intensity_to_depose = self._obj.get_last_pheromon_intensity()
        if self._obj.is_distance_shorter_than_previous():
            pheromon_intensity_to_depose += 1

        context.add_pheromon_trace(route_towns, pheromon_intensity_to_depose)
        self._obj.reinit_travel()