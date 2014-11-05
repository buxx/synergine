from synergine.src.synergy.event.Action import Action
from module.traveller.event.DirectionChoosedEvent import DirectionChoosedEvent

class MoveAction(Action):
    """
    Deplacement du traveller (garder la trace)
    """

    _listen = DirectionChoosedEvent

    def run(self, collection, context):
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
        self._obj.add_town(choosed_town)