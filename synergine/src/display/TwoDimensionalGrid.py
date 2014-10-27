class TwoDimensionalGrid:

    def __init__(self, cell_size):
        self._cell_size = cell_size

    def set_cell_size(self, cell_size):
        self._cell_size = cell_size

    def get_real_pixel_point(self, three_dimensional_point):
        return (three_dimensional_point[1]*self._cell_size, three_dimensional_point[2]*self._cell_size)