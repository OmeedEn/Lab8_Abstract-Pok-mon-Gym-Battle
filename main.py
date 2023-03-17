# Omeed and Aramis
# CECS 277 - Sec 03 
# Lab 8 - Pokemon Gym Battle
# Date: 03/16/2023
# Create a pokemon and have it battle an opponent until the user or gym trainer wins!

import pokemon
import random
import fire
import water
import grass
import check_input


def main():

  #initialize variables
  waterPokemons = ['Vaporeon', 'Squirtle', 'Lapras']
  firePokemons = ['Charmander', 'Charizard', 'Arcanine']
  grassPokemons = ['Bulbasaur', 'Jigglypuff', 'Bellsprout']

  #have the gym leader select a random list and use those Pokemons
  gymLeaderPokeType = random.choice(["Fire", "Water", "Grass"])

  if gymLeaderPokeType == "Water":
    gymType = 1 #"WATER" MAKE SURE TO RECHECK THESE
    gymLeaderPokeNameList = waterPokemons
    
  elif gymLeaderPokeType == "Fire":
    gymType = 0 #"FIRE"
    gymLeaderPokeNameList = firePokemons
    
  elif gymLeaderPokeType == "Grass":
    gymType = 2 #"GRASS"
    gymLeaderPokeNameList = grassPokemons

  #initialize user and gym leader Pokemon
  gymLeaderPokeName = gymLeaderPokeNameList[0]
  userFirePokemonName = random.choice(firePokemons)
  userWaterPokemonName = random.choice(waterPokemons)
  userGrassPokemonName = random.choice(grassPokemons)
  
  print(f"PROF OAK: Hello Trainer!  Today you're off to fight your first gym battle of 1 vs. 3 {gymLeaderPokeType.upper()} pokemon. ")
  
  print(f"1. I choose you, {userFirePokemonName}")
  print(f"2. {userWaterPokemonName}!  GO!")
  print(f"3. We can do it, {userGrassPokemonName}")
  userChoice = check_input.get_int_range("Please choose a Pokemon: ", 1, 3) #check_input
  print("\n -- GYM BATTLE -- ")

  if userChoice == 1:
    userPokeType = 0 #"FIRE"
    userPokeName = userFirePokemonName
  elif userChoice == 2:
    userPokeType = 1 #"WATER"
    userPokeName = userWaterPokemonName
  elif userChoice == 3:
    userPokeType = 2 #"GRASS"
    userPokeName = userGrassPokemonName
    
  #create objects for gymLeader and user
  user_p = pokemon.Pokemon(userPokeName, userPokeType)
  gym_p = pokemon.Pokemon(gymLeaderPokeName, gymType)
  #type = int(input("Choose a type of pokemon \n 1. Fire \n 2. Water \n 3. Grass")) #when user selects Pokemon, have type associated with it
  count = 0 # counter for the number of pokemons chosen

  
  while count < 3:
  
    #print Gym Battle Header statement
    print("GYM LEADER: I choose...")
    
    print(f"\t{gymLeaderPokeName} HP: 25/25") #initialize gym leader hp with pokemon.py
    
    print(f"YOUR CHOICE:\n\t{userPokeName} HP: {user_p._hp}/25")
  
    #implementation of pokemon class: needs to print hp, needs to import functions in the pokemon class based on the choices
      
    while user_p.hp > 0 and gym_p.hp > 0:
      print("Choose a type of attack: \n 1. Normal move \n 2. Special move \n" )
      attackChoice = int(input("Enter attack type: "))

      #make gym pokemon attack
      # for future use, maybe make this random: gym_attack_choice = random.randint(1,2)
      
      # gym_p.attack(user_p, 1, 1)

      if attackChoice == 1:
        norm_menu = user_p.get_normal_menu()
        normal_attack_choice = int(input(norm_menu + "\nChoose a Normal Attack: "))
        user_p.attack(gym_p, attackChoice, normal_attack_choice)
        gym_p.attack(user_p, 1, 1)
        print(user_p)
        print(gym_p)
        print("\n")

        
        #SHOW IF ATTACK IS SLAM OR TACKLE 
      
      elif attackChoice == 2:
        
        if userPokeType == 0:
          f = fire.Fire(userPokeName)
          special_str = f.get_special_menu() #fire.Fire, water.Water, grass.Grass
          special_attack = int(input(special_str + "\nChoose a Special Attack: ")) #put check input later
          f._special_move(gym_p, special_attack)
          user_p.attack(gym_p, attackChoice, special_attack)
          gym_p.attack(user_p, 1, 1)
          
        elif userPokeType == 1:
          w = water.Water(userPokeName)
          special_str = w.get_special_menu() #fire.Fire, water.Water, grass.Grass
          special_attack = int(input(special_str + "\nChoose a Special Attack: "))
          w._special_move(gym_p, special_attack)
          user_p.attack(gym_p, attackChoice, special_attack)
          gym_p.attack(user_p, 1, 1)
          
        elif userPokeType == 2:
          g = grass.Grass(userPokeName)
          special_str = g.get_special_menu() #fire.Fire, water.Water, grass.Grass
          special_attack = int(input(special_str + "\nChoose a Special Attack: "))
          g._special_move(gym_p, special_attack)
          user_p.attack(gym_p, attackChoice, special_attack)
          gym_p.attack(user_p, 1, 1)
          
        print(user_p)
        print(gym_p)
        print("\n")
        
    if user_p.hp <= 0:
      print(user_p._name, "\nYou lose! The gym leader defeated you!")
      break;
      
    elif gym_p.hp <= 0 and count < 3:
      count += 1
      print("GYM LEADER: NOOOOOOOO! You defeated my pokemon!")
      gym_p = pokemon.Pokemon(gymLeaderPokeNameList[count], gymType)
      print(gym_p)
      
    if count > 2:      
      print("You win! You defeated the gym leader!")

main()