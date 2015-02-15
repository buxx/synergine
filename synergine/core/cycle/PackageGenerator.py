from synergine.core.cycle.Package import Package


class PackageGenerator():

  def __init__(self):
    self._data_list = []
    self._data_length = 0
    self._current_index = 0
    self._step_length = 0

  def _load(self, data_list, nb_proc):
    self._data_list = data_list
    self._data_length = len(self._data_list)
    self._current_index = 0
    self._step_length = len(data_list) // nb_proc

  def get_packages(self, data_list, nb_proc, package_common):
    self._load(data_list, nb_proc)
    while self._is_stay_data_to_package():
      slice_start = self._current_index
      yield Package(self._data_list[slice_start:slice_start+self._step_length], package_common)
      self._current_index += self._step_length

  def _is_stay_data_to_package(self):
    return self._current_index < len(self._data_list)