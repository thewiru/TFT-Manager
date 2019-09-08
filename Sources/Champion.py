
class Champion:

  def __init__(self, name, cost, traits):
    self.name = name
    self.cost = cost
    self.traits = traits
    self.appeared = 0
    self.image = "Images\\" + self.name + "Square.png"

aatrox = Champion ("Aatrox", 3, ["Demon", "Blademaster"])
