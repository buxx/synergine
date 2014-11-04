from synergine.src.synergy.Simulation import Simulation


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
