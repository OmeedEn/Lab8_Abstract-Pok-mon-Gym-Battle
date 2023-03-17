import pokemon
import random

class Grass(pokemon.Pokemon):
  """ class for grass attack and defensive encounters for each of the pokemon"""
  def __init__(self, name):
    # call super to set name and type
    super().__init__(name, 2)

  #Override the get_special_menu and _special_move methods
  def get_special_menu(self):
    return "Special moves: \n1. Razor Leaf \n2. Solar Beam "

  def _special_move(self, opponent, move):
    choice = 0
    if move == 1:
      choice = self._razor_leaf(opponent) #call specialMove1
    elif move == 2:
      choice = self._solar_beam(opponent) #call specialMove2
    return choice


  def _razor_leaf(self, opponent) -> str:
    r = random.randint(1, 5)
    effectiveness = self._battle_table[2][2]
    if self._type == 2 and opponent._type == 0:
      effectiveness = self._battle_table[2][0]
    elif self._type == 2 and opponent._type == 1:
      effectiveness = self._battle_table[2][1]
      
    damage = r * effectiveness
    description = f"{self._name} slices {opponent._name} with RAZOR sharp LEAVES for {damage} damage.\n"
    if effectiveness >= 2:
      description += "It was SUPER EFFECTIVE!"
    elif effectiveness <= 0.5:
      description += "It was not very effective."
    #else:
      #description += "neither effective or ineffective"
    opponent._take_damage(damage)
    print(description)
    return description
    

  def _solar_beam(self, opponent) -> str:
    r = random.randint(3, 4)
    effectiveness = self._battle_table[2][2]
    if self._type == 2 and opponent._type == 0:
      effectiveness = self._battle_table[2][0]
    elif self._type == 2 and opponent._type == 1:
      effectiveness = self._battle_table[2][1]
      
    damage = r * effectiveness
    description = f"{self._name} blasts {opponent._name} with SOLAR BEAM for {damage} damage.\n"
    if effectiveness >= 2:
      description += "It was effective!"
    elif effectiveness <= 0.5:
      description += "It was not very effective."
    # else:
    #   description += "It was neither effective or ineffective"
    opponent._take_damage(damage)
    print(description)
    return description


    