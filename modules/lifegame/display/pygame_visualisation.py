from xyworld.display.object.pygame.PygameImage import PygameImage
from lifegame.synergy.object.Cell import Cell
from os import getcwd

image_cell_full = PygameImage.from_filepath(getcwd()+'/modules/lifegame/display/pygame/cha3.png')
image_cell_medium = PygameImage.from_filepath(getcwd()+'/modules/lifegame/display/pygame/cha2.png')
image_cell_small = PygameImage.from_filepath(getcwd()+'/modules/lifegame/display/pygame/cha.png')
image_cell_dead = PygameImage.from_filepath(getcwd()+'/modules/lifegame/display/pygame/cha0.png')


def alive_render(cell, context):
    """

    :param cell: Cell
    :param context: Context object
    :return: The image render
    :rtype: PygameImage
    """
    if cell.is_alive():
        if cell.get_is_alive_since() < 1:
            return image_cell_small
        elif cell.get_is_alive_since() == 1:
            return image_cell_medium
        else:
            return image_cell_full
    else:
        return image_cell_dead

visualisation = {
    'objects': {
        Cell: {
            'default': image_cell_small,
            'callbacks': [alive_render]
        }
    }
}