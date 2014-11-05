from synergine.src.display.PygameDisplay import PygameDisplay
from module.traveller.synergy.Town import Town
import pygame


class TravellerDisplay(PygameDisplay):
    """
    afficher les relations entre les towns
    """

    def receive(self, synergy_object_manager):
        self._draw_town_links(synergy_object_manager.get_objects_by_type(Town))
        super().receive(synergy_object_manager)

    def _draw_town_links(self, towns):
        for town_a in towns:
            town_a_point = town_a.get_point()
            for town_b in towns:
                town_b_point = town_b.get_point()
                start_point = self._get_real_screen_point(town_a_point[1], town_a_point[2], town_a_point[0])
                end_point = self._get_real_screen_point(town_b_point[1], town_b_point[2], town_b_point[0])
                # TODO: Largeur en fonction de l'intensité des pheromones
                pygame.draw.line(self._screen, (55, 55, 55), (start_point[1], start_point[2]), (end_point[1], end_point[2]), 1)