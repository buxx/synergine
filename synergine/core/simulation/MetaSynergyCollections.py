from synergine.lib.eint import IncrementedNamedInt


class MetaSynergyCollections():
    COLS = IncrementedNamedInt.get('synergine.cols')

    def __init__(self, list):
        self._list = list

    def get(self, col_name, allow_empty=False):
        return self._list.get(self.COLS, col_name, allow_empty=allow_empty)

    def add_remove(self, object_id, add_col_name, remove_col_name):
        self._list.add(self.COLS, add_col_name, object_id)
        self._list.remove(self.COLS, remove_col_name, object_id)

    def add_remove_lists(self, object_id, add_cols_names, remove_cols_names, allow_empty=False):
        for add_col_name in add_cols_names:
            self._list.add(self.COLS, add_col_name, object_id)
        for remove_col_name in remove_cols_names:
            self._list.remove(self.COLS, remove_col_name, object_id, allow_empty=allow_empty)

    def add(self, object_id, col_name):
        self._list.add(self.COLS, col_name, object_id)

    def add_list(self, object_id, col_names):
        for col_name in col_names:
            self.add(object_id, col_name)

    def remove(self, object_id, col_name, allow_not_in=False):
        self._list.remove(self.COLS, col_name, object_id, allow_not_in=allow_not_in)

    def remove_list(self, object_id, col_names, allow_not_in=False):
        for col_name in col_names:
            self.remove(object_id, col_name, allow_not_in=allow_not_in)
