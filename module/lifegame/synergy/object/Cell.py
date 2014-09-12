from src.synergy.object.SynergyObject import SynergyObject

class Cell(SynergyObject):
  
  def addTrace(self, point):
    """
    Cell have only one point length
    """
    self._trace = [point]
  
  def getPoint(self):
    return self.getTrace()[0]
  
  
  def cycle(self, context):
    self._will = None
    # TODO: deleguer changement de position (genre self.will_do(machin) ?) 
    map = context.getMap()
    arround_points = self.getArroundPoints()
    count_arround = 0
    
    arrounds = []
    for arround_point in arround_points:
      if arround_point in map:
        if isinstance(map[arround_point], Cell) or True: # or True: isinstance repond False arf ||| c'est une liste gors beta !
          count_arround += 1
          arrounds.append(map[arround_point])
    print(self.getPoint() )
    #if self.getPoint() == (0, 23, 20):
    #  import pdb; pdb.set_trace()
    if count_arround < 2 or count_arround > 3:
      self._will = 'die'
  
  
  
  def getArroundPoints(self):
    pos = self.getPoint()
    pz = pos[0]
    px = pos[1]
    py = pos[2]
    return (
      (pz, px-1, py-1),
      (pz, px,   py-1),
      (pz, px+1, py+1),
      (pz, px-1, py  ),
      (pz, px+1, py  ),
      (pz, px-1, py+1),
      (pz, px,   py+1),
      (pz, px+1, py-1)
    )