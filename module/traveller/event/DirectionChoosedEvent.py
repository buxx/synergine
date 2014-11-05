from synergine.src.synergy.event.Event import Event
from module.traveller.event.TownTasteMechanism import TownTasteMechanism
from module.traveller.synergy.Traveller import Traveller
from random import randint


class DirectionChoosedEvent(Event):
    """
    TODO: Renommer en TownChoosable si on laisse le choix a l'action
    Recupere les towns scores et fait un choix au hasard
    """

    def __init__(self, actions):
        super().__init__(actions)
        self._concerneds = [Traveller]
        self._mechanism = TownTasteMechanism

    def _object_match(self, obj, context, parameters={}):
        if super()._object_match(obj, context, parameters):
            parameters['choosed'] = self._get_random_town(parameters)
            return True
        return False

    def _get_random_town(self, parameters):
        towns_ranges = {}
        total_score = 0
        towns_scores = parameters['towns']
        for town in towns_scores:
            town_score = towns_scores[town]
            town_range_start = total_score
            total_score += town_score
            town_range_end = total_score
            towns_ranges[town] = (town_range_start, town_range_end)
        random_int = randint(0, total_score)
        for town in towns_ranges:
            town_range = towns_ranges[town]
            if town_range[0] <= random_int <= town_range[1]:
                return town
        raise Exception("Unable to choice town")