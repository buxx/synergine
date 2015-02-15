from synergine.synergy.event.Action import Action
from traveller.event.DirectionChoosedEvent import DirectionChoosedEvent
from traveller.event.TurnFinishedAction import TurnFinishedAction


class MoveAction(Action):
    """
    Deplacement du traveller (garder la trace)
    """

    _listen = DirectionChoosedEvent
    _depend = [TurnFinishedAction]

    def run(self, obj, collection, context, synergy_manager):
        """

        :param collection:
        :param context:
        :return:
        """
        # TODO: deplacer le traveller (set_town, et set_trace/point)
        # TODO traveller: garder historique towns
        choosed_town = self._parameters['choosed']
        if not choosed_town:
            raise Exception("Can't continue without town")
        obj.add_town(choosed_town, self._parameters['distance'])