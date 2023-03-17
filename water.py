import pokemon
import random

class Water(pokemon.Pokemon):
  """ class for water attack and defensive encounters for each of the pokemon"""
  def __init__(self, name):
    # call super to set name and type
    super().__init__(name, 1)

  #Override the get_special_menu and _special_move methods
  def get_special_menu(self):
    return "Special moves: \n1. Water Gun \n2. Bubble Beam "

  def _special_move(self, opponent, move):
    choice = 0
    if move == 1:
      choice = self._water_gun(opponent) #call specialMove1
    elif move == 2:
      choice = self._bubble_beam(opponent) #call specialMove2
    return choice

  def _water_gun(self, opponent) -> str:
    r = random.randint(1, 5)
    effectiveness = self._battle_table[1][1]
    if self._type == 1 and opponent._type == 0:
      effectiveness = self._battle_table[1][0]
    elif self._type == 1 and opponent._type == 2:
      effectiveness = self._battle_table[1][2]
      
    damage = r * effectiveness
    description = f"{self._name} splashes {opponent._name} with WATER GUN for {damage} damage.\n"
    if effectiveness >= 2:
      description += "It was SUPER EFFECTIVE!"
    elif effectiveness <= 0.5:
      description += "It was not very effective."
    #else:
      #description += "neither effective or ineffective"
    opponent._take_damage(damage) #make sure this will be good
    print(description)
    return description
    

  def _bubble_beam(self, opponent) -> str:
    r = random.randint(3, 4)
    effectiveness = self._battle_table[1][1]
    if self._type == 1 and opponent._type == 0:
      effectiveness = self._battle_table[1][0]
    elif self._type == 1 and opponent._type == 2:
      effectiveness = self._battle_table[1][2]
      
    damage = r * effectiveness
    description = f"{self._name} beams {opponent._name} with BUBBLE BEAM and did {damage} damage.\n"
    if effectiveness >= 2:
      description += "effective!"
    elif effectiveness <= 0.5:
      description += "not very effective."
    #else:
      #description += "neither effective or ineffective"
    opponent._take_damage(damage) #make sure this will be good
    print(description)
    return description
    


    