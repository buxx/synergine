from synergine.src.synergy.Simulation import Simulation
from module.traveller.synergy.Town import Town
from module.traveller.synergy.Traveller import Traveller


class TravellerSimulation(Simulation):
    """
    Problème du voyageur de commerce: Trouver le chelin le plus court entre x villes

    - L'obj part d'un ville A
    - L'obj ne peux passer lors de sa boucle, qu'un fois par ville
    - La ville "suivante" est choisi au hasard, plus une ville est loin moins elle a de chance
      d'être choisis
    - Plus il y a de "pheromones" entre la ville "actuelle" et la ville "a choisir" est forte
      plus la ville "a choisir" a de chance d'être choisis
    - Une fois la boucle effectué, si le trajet a été court (plus qu'une fois précédente) plus il y a
      de phéromones
    - A chaque fin de "tour" (chaque obj a fait une boucle) les piste de phéromones perdent en intensités

    TODOS:
     * PyGame: tracer une ligne
    """

    def __init__(self, collections):
        super().__init__(collections)
        self._cycle_count = 0

    def end_cycle(self, context):
        # TODO: Il ne faut le faire que si tout les traveller ont finis leurs tour !
        self._cycle_count += 1
        towns = context.get_objects_by_type(Town)
        if self._cycle_count % len(towns) == 0:
            # travellers = context.get_objects_by_type(Traveller)
            # all_finisheds = True
            # for traveller in travellers:
            #     if not traveller.visited_towns(towns):
            #         all_finisheds = False

            context.reduce_pheromons_intensitys()