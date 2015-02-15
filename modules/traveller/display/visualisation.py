from xyworld.display.object.pygame.PygameImage import PygameImage
from traveller.synergy.Traveller import Traveller
from traveller.synergy.Town import Town
from os import getcwd


# TODO: Url relative au fichier
visualisation = {
    'windows': {},
    'objects': {
        Town: {
            'default': PygameImage.from_filepath(getcwd()+'/modules/traveller/display/town.png')
        },
        Traveller: {
            'default': PygameImage.from_filepath(getcwd()+'/modules/traveller/display/traveller.png')
        }
    }
}