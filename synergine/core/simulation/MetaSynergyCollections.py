from synergine.lib.eint import IncrementedNamedInt

class MetaSynergyCollections():

    COLS = IncrementedNamedInt.get('synergine.cols')

    def __init__(self, list):
        self._list = list

    def get(self, col_name):
        return self._list.get(self.COLS, col_name)

    def add_remove(self, object_id, add_col_name, remove_col_name):
        self._list.add(self.COLS, add_col_name, object_id)
        self._list.remove(self.COLS, remove_col_name, object_id)

    def add_remove_lists(self, object_id, add_cols_names, remove_cols_names):
        for add_col_name in add_cols_names:
            self._list.add(self.COLS, add_col_name, object_id)
        for remove_col_name in remove_cols_names:
            self._list.remove(self.COLS, remove_col_name, object_id)

    def add(self, object_id, col_name):
        self._list.add(self.COLS, col_name, object_id)

    def remove(self, object_id, col_name):
        self._list.remove(self.COLS, col_name, object_id)
