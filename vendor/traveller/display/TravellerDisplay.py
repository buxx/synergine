from xyworld.display.PygameDisplay import PygameDisplay
from traveller.synergy.Town import Town
from traveller.synergy.Traveller import Traveller
import pygame


class TravellerDisplay(PygameDisplay):
    """
    afficher les relations entre les towns
    """

    def receive(self, synergy_object_manager, context):
        self._draw_town_links(synergy_object_manager.get_objects_by_type(Town), context)
        self._draw_traveller_routes(synergy_object_manager.get_objects_by_type(Traveller))

        # Test
        for town in synergy_object_manager.get_objects_by_type(Town):
            town_point = town.get_point()
            screen_point = self._get_real_screen_point(town_point[1], town_point[2])
            label = self._default_font.render(str(town).replace('<traveller.synergy.Town.Town object at', '').replace('>', ''), 1, (255,255,0))
            self._screen.blit(label, (screen_point[1], screen_point[2]))

        for traveller in synergy_object_manager.get_objects_by_type(Traveller):
            traveller_point = traveller.get_point()
            screen_point = self._get_real_screen_point(traveller_point[1], traveller_point[2])
            label = self._default_font.render(str(traveller).replace('<traveller.synergy.Traveller.Traveller object at', '').replace('>', ''), 1, (255,255,0))
            self._screen.blit(label, (screen_point[1], screen_point[2]+20))

        super().receive(synergy_object_manager, context)

    def _draw_town_links(self, towns, context):
        for town_a in towns:
            for town_b in towns:
                intensity = context.get_road_intensity(town_a, town_b)
                self._draw_line_between_towns(town_a, town_b, intensity)

    def _draw_line_between_towns(self, town_a, town_b, intensity=1, color=(0, 155, 155)):
        town_a_point = town_a.get_point()
        town_b_point = town_b.get_point()
        start_point = self._get_real_screen_point(town_a_point[1], town_a_point[2], town_a_point[0])
        end_point = self._get_real_screen_point(town_b_point[1], town_b_point[2], town_b_point[0])
        # TODO: Largeur en fonction de l'intensité des pheromones
        if intensity > 20:
            intensity = 6
        pygame.draw.line(self._screen, color, (start_point[1], start_point[2]), (end_point[1], end_point[2]), intensity)

    def _draw_traveller_routes(self, travellers):
        for traveller in travellers:
            traveller_visited_towns = traveller.get_towns()
            previous_visited_town = None
            for traveller_visited_town in traveller_visited_towns:
                if previous_visited_town:
                    self._draw_line_between_towns(previous_visited_town, traveller_visited_town, 1, (128, 128, 0))
                previous_visited_town = traveller_visited_town
