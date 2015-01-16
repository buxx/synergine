from synergine.src.synergy.event.Action import Action
from module.traveller.event.DirectionChoosedEvent import DirectionChoosedEvent
from module.traveller.event.TurnFinishedAction import TurnFinishedAction


class MoveAction(Action):
    """
    Deplacement du traveller (garder la trace)
    """

    _listen = DirectionChoosedEvent
    _depend = [TurnFinishedAction]

    def run(self, obj, collection, context):
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