from synergine.src.display.PygameDisplay import PygameDisplay
from module.traveller.synergy.Town import Town
from module.traveller.synergy.Traveller import Traveller
import pygame


class TravellerDisplay(PygameDisplay):
    """
    afficher les relations entre les towns
    """

    def receive(self, synergy_object_manager):
        self._draw_town_links(synergy_object_manager.get_objects_by_type(Town))
        self._draw_traveller_routes(synergy_object_manager.get_objects_by_type(Traveller))
        super().receive(synergy_object_manager)

    def _draw_town_links(self, towns):
        for town_a in towns:
            for town_b in towns:
                self._draw_line_between_towns(town_a, town_b)

    def _draw_line_between_towns(self, town_a, town_b, color=(55, 55, 55)):
        town_a_point = town_a.get_point()
        town_b_point = town_b.get_point()
        start_point = self._get_real_screen_point(town_a_point[1], town_a_point[2], town_a_point[0])
        end_point = self._get_real_screen_point(town_b_point[1], town_b_point[2], town_b_point[0])
        # TODO: Largeur en fonction de l'intensité des pheromones
        pygame.draw.line(self._screen, color, (start_point[1], start_point[2]), (end_point[1], end_point[2]), 1)

    def _draw_traveller_routes(self, travellers):
        for traveller in travellers:
            traveller_visited_towns = traveller.get_towns()
            previous_visited_town = None
            for traveller_visited_town in traveller_visited_towns:
                if previous_visited_town:
                    self._draw_line_between_towns(previous_visited_town, traveller_visited_town, (128, 128, 0))
                previous_visited_town = traveller_visited_town
