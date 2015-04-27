import numpy as np


class MetaSpace():
    """
    TODO: Ce doit juste etre une surcharge de MetaCollection avec des methodes

    """
    def __init__(self):
        self._metas = {}

    def get_array(self, name):
        if name not in self._metas:
            self._metas[name] = np.array([])


