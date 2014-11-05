from synergine.src.core.simulation.mechanism.Mechanism import Mechanism
from module.traveller.synergy.Town import Town
from module.traveller.synergy.Traveller import Traveller


class TownTasteMechanism(Mechanism):
    """
    Pour chaque traveller, fabriquer les scores des towns:
    * distance = score (+0 à 100 pts)
    * intensite pheromones (+force pherom. pts)

    TODO: Les données de pheromone doivent être qqpart, dans le contexte ?
    ===> qui devra être accessible au Display
    """

    def _get_object_event_parameters(self, obj, context):
        # TODO: Il faut reflechir a un filtre en amont
        if not isinstance(obj, Traveller):
            return {}

        towns = context.get_objects_by_type(Town)
        town_tastes = self._get_towns_tastes(obj, towns)
        return {'towns': town_tastes}

    def _get_towns_tastes(self, obj, towns):
        town_tastes = {}
        for town in towns:
            try:
                obj.get_towns().index(town)
            except ValueError:
                town_tastes[town] = self._get_town_taste(obj, town, towns)
        return town_tastes

    def _get_town_taste(self, obj, town, towns):
        object_point = obj.get_point()
        distance_score = self._get_distance_score(object_point, town, towns)
        object_town = obj.get_town()
        pheromone_score = self._get_pheromon_score(object_town, town, towns)
        return round(distance_score + pheromone_score / 2)

    def _get_distance_score(self, reference_point, tested_town, towns):
        """
        Sur une echelle de 100 points, une Town a 10% de distance de la ville
        la plus loi gagne 90 pts.
        :param reference_point:
        :param tested_town: Town
        :param towns: list of Town
        :return: int
        """

        # TODO: calculer ça qu'un fois ...
        farest_distance = 0
        for town in towns:
            town_point = town.get_point()
            route_distance = abs((reference_point[1]-town_point[1]+reference_point[2]-town_point[2])/2)
            if route_distance > farest_distance:
                farest_distance = route_distance

        tested_town_point = tested_town.get_point()
        tested_town_distance = abs((reference_point[1]-tested_town_point[1]+reference_point[2]-tested_town_point[2])/2)

        score = 100 - (tested_town_distance * 100 / farest_distance)

        return score

    def _get_pheromon_score(self, start_town, goal_town, towns):
        """
        Sur une echellede 100 points, une route qui a 25% d'intensité (i 50) de phéromone
        de la route la plus forte (200) gagne 25 pts
        TODO: Changer ce bareme pour que les pheromones prennent le dessus ?
        :param start_town:
        :param goal_town:
        :return:
        """
        return 0