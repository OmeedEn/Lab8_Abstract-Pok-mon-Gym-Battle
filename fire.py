import pokemon
import random

class Fire(pokemon.Pokemon):
  """ class for fire attack and defensive encounters for each of the pokemon"""
  
  def __init__(self, name):
    # call super to set name and type
    super().__init__(name, 0)

  #Override the get_special_menu and _special_move methods
  def get_special_menu(self):
    return "Special moves: \n1. Ember \n2. Fire Blast "

  def _special_move(self, opponent, move):
    choice = 0
    if move == 1:
      choice = self._ember(opponent) #call specialMove1
    elif move == 2:
      choice = self._fire_blast(opponent) #call specialMove2      
    return choice

  def _ember(self, opponent) -> str:
    r = random.randint(1, 5)
    effectiveness = self._battle_table[0][0]
    if self._type == 0 and opponent._type == 1:
      effectiveness = self._battle_table[0][1]
    elif self._type == 0 and opponent._type == 2:
      effectiveness = self._battle_table[0][2]
      
    damage = r * effectiveness
    description = f"{self._name} engulfs {opponent._name} with EMBERS for {damage} damage "
    if effectiveness >= 2:
      description += "It was SUPER EFFECTIVE!"
    elif effectiveness <= 0.5:
      description += "It was not very effective."
    #else:
      #description += "it was neither effective or ineffective"
    opponent._take_damage(damage)
    print(description)
    return description
    

  def _fire_blast(self, opponent) -> str:
    r = random.randint(3, 4)
    effectiveness = self._battle_table[0][0]
    if self._type == 0 and opponent._type == 1:
      effectiveness = self._battle_table[0][1]
    elif self._type == 0 and opponent._type == 2:
      effectiveness = self._battle_table[0][2]
      
    damage = r * effectiveness
    description = f"{self._name} blasts {opponent._name} with FIRE BLAST with {damage} damage "
    if effectiveness >= 2:
      description += "it was effective!"
    elif effectiveness <= 0.5:
      description += "it was not very effective."
    # else:
    #   description += "it was neither effective or ineffective"
    opponent._take_damage(damage)
    print(description)
    return description
    


    