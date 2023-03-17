import random
import abc

class Pokemon:
  """ Abstract Class that defines a general Pokemon.
  Attributes:

  1. Name (str) - name of Pokemon (ex: Charizard, Squirtle, Bulbasaur)

  2. Poke_type (int) - type of Pokemon (ex: 0 (Fire), 1 (Water), 2(Grass))

  3. hp (int) - default 25

  4. Battle Table (2D List) - Damage Multiplier
  
  """

  def __init__(self, name, type):
    """ Initializes the name and type of Pokemon using the parameters. 
    Assign the battle table (2D List) and set the hp to 25. """
    self._name = name #str
    self._type = type #int
    self._hp = 25 # <<get>> _hp: int
    self._battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]]
    # Battle table represents the multiplier of damage each type of Pokemon has against another type
    #For example, Fire (list #1 in 2D list) deals normal damage to other fire types, half damage to water types (list #2), and double damage to grass types (list #3)

  @property
  def hp(self):
    """ Accesses the hp property"""
    return self._hp # maybe return just "_hp" <<get>> _hp: int

  def get_normal_menu(self):
    """ Returns a string with the menu options for the normal moves: slam and tackle """
    return "Normal moves: \n1. Slam \n2. Tackle"

  def _normal_move(self, opponent, move):
    """ Use the move parameter to choose to call either slam or tackle method.
    Returns the string returned from those methods. """
    
    #initialize move, the variable that is taken from a user/gym leader input to call slam/tackle 
    self.move = move 

    # associate attack type with move selection
    if move == 1:
      return self._slam(opponent) #call slam
    elif move == 2:
      return self._tackle(opponent) #call tackle
    

  def _slam(self, opponent):
    """ Randomizes some damage (values 1 - 8) for slam. Returns a string decription of the move. """
    dmg = random.randint(1, 8)
    multiplier = self._battle_table[self._type][opponent._type]
    total_dmg = int(dmg*multiplier)
    opponent._take_damage(total_dmg)
    print(f"{self._name} SLAMS {opponent._name} for {total_dmg} damage. ")
    return f"{self._name} SLAMS {opponent._name} for {total_dmg} damage. "

  def _tackle(self, opponent):
    """ Randomizes some damage (values 3 - 6) for tackle. Returns a string decription of the move. """
    dmg = random.randint(3, 6)
    multiplier = self._battle_table[self._type][opponent._type]
    total_dmg = int(dmg*multiplier)
    opponent._take_damage(total_dmg)
    print(f"{self._name} TACKLES {opponent._name} for {total_dmg} damage. ")
    return (f"{self._name} TACKLES {opponent._name} for {total_dmg} damage. ")

  @abc.abstractclassmethod
  def get_special_menu(self):
    """ Abstract method (overriden in subclasses). Returns the menu for the special moves of each type. """
    # return "Normal moves: \n1.Special 1 \n2. Special 2. " #fix later
    pass

  @abc.abstractmethod
  def _special_move(self, opponent, move):
    """ Abstract method (overriden in subclasses). 
    Uses the move parameter to choose to call either of the special moves for that type."""
    pass 
    #raise NotImplementedError("Must be implemented in subclasses")

  
  def attack(self, opponent, type, move):
    """ Use the type parameter to choose to call either _normal_move or _special_move. 
        Type = normal move (1) or special move (2)
          For normal move type (1), the move parameter corresponds to: 
            1. Slam
            2. Tackle 
          For special move type (2), the move parameter corresponds to its elemental attacks
    """

    if type == 1:
      return self._normal_move(opponent, move)
    
    elif type == 2:
      return self._special_move(opponent, move)
      
  
  def __str__(self):
    """ Displays the pokemon's name and hp in the format "Name: hp/25 """
    return f"{self._name}: {self._hp}/25"
  
  def _take_damage(self, dmg):
    """ Damage the pokemon takes. Subtracts damage (dmg) from Pokemon's hp. 
    Also checks that the Pokemon's hp doesn't go past zero --> if negative, it resets it to 0. """
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0
      