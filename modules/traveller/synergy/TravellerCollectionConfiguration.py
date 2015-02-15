from synergine.synergy.collection.Configuration import Configuration
from traveller.synergy.Traveller import Traveller
from traveller.synergy.Town import Town
import random


class TravellerCollectionConfiguration(Configuration):

    def get_start_objects(self, collection):

        objects = []

        # TODO: nombre de maison en config
        for town_number in range(5):
            town = Town()
            town.set_position((0, round(random.randint(0,  700)/20), round(random.randint(0, 500)/20)))
            objects.append(town)

        town_1 = objects[0]

        # TODO: nombre de traveller en config
        for town_number in range(5):
            traveller = Traveller()
            traveller.add_town(town_1)
            objects.append(traveller)

        return objects