from itertools import combinations
import random

class Pokemon:
  # To create a Pokemon, it should have a name, at least one type, a level, and health based on level. The level will default to 5 as with all starters and it will not be knocked out. 
  def __init__(self, name, type, level = 5):
    self.name = name
    self.type = type
    self.level = level
    self.health = level * 5
    self.max_health = level * 5
    self.is_knocked_out = False

  def __repr__(self):
    # This will describe the pokemon, showing the name, level, and remaining HP
    return 'The level {level} {name} has {health} HP remaining. They are a {type} type Pokemon.'.format(level = self.level, name= self.name, health = self.health, type = self.type)
  
  def revive(self):
    # Reviving a knocked out Pokemon will change its status to False
    self.is_knocked_out = False
    # Using a Revive will set the Pokemon to half max health, rounded up.
    if self.health == 0:
      self.health = round(self.max_health / 2)
    print("{name} was revived!".format(name = self.name))

  def knock_out(self):
    # When a Pokemon is reduced to 0 health, it will be knocked out, setting its status to True
    self.is_knocked_out = True
    # A knocked out Pokemon will always have 0 health.
    if self.health != 0:
      self.health = 0
    print("{name} was knocked out!".format(name = self.name))
  
  def lose_health(self, amount):
    # When damaged, a Pokemons health will go down, and print remaining health
    self.health -= amount
    if self.health <= 0:
      # Health will always bottom out at 0, where the Pokemon is knocked out
      self.health = 0
      self.knock_out()
    else:
      print("{name} was hit!\nIt\'s health is now {health}.".format(name = self.name, health = self.health))
    
  def gain_health(self, amount):
    # Restores a Pokemon's health
    # If knocked out, a Revive must be used instead.
    if self.health == 0:
      print("{name} is knocked out, it must be revived first!")
    # Prevent health from going over max health
    if self.health >= self.max_health:
      self.health = self.max_health
    print("{name} now has {health} HP".format(name = self.name, health = self.health))

  def attack(self, other_pokemon):
    # Make sure Pokemon isn't knocked out
    if self.is_knocked_out:
      print("{name} can't attack because it is knocked out!".format(name = self.name))
      return
    # Create basic logic for checking type matchups
    # fire_advantage 
    # fire_strong_against = ["Grass", "Ice", "Bug", "Steel"]
    # fire_weak_against = ["Fire", "Water", "Rock", "Dragon"]
    # If there's a type mismatch, the Pokemon will deal damage equal to half it's level
    if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Fire" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Water"):
      print("{my_pokemon} attacked {opponent_pokemon} for {damage} damange.".format(my_pokemon = self.name, opponent_pokemon = other_pokemon.name, damage = round(self.level * 0.5)))
      print("It\'s not very effective.")
      other_pokemon.lose_health(round(self.level * 0.5))
    # If there is a neutral type matchup, the attack will deal normal damage
    if (self.type != "Normal" and other_pokemon.type == "Normal") or (self.type == "Normal" and other_pokemon.type != "Normal") or (self.type == "Normal" and other_pokemon.type == "Normal"):
      print("{my_pokemon} attacked {opponent_pokemon} for {damage}".format(my_pokemon = self.name, opponent_pokemon = other_pokemon.name, damage = self.level))
      other_pokemon.lose_health(self.level)
    # If the attacking Pokemon has a type advantage, it will deal double damge
    if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
      print("{my_pokemon} attacked {opponent_pokemon} for {damage}".format(my_pokemon = self.name, opponent_pokemon = other_pokemon.name, damage = self.level * 2))
      print("It\'s super effective!")
      other_pokemon.lose_health(self.level * 2)

class Trainer:
  # A trainer has a list of up to 3 Pokemon, a number of potions, a number of revives, and a name. When the trainer is created, the first Pokemon in their list is the active Pokemon (number 0)
  def __init__(self, pokemon_list, potions, revives, name):
    self.name = name
    self.potions = potions
    self.pokemons = pokemon_list
    self.revives = revives
    self.current_pokemon = 0
  
  def __repr__(self):
    # PRints the name of hte trainer, the Pokemon they have, and the current active Pokemon.
    print("Trainer {name} has the following Pokemon:".format(name = self.name))
    for pokemon in self.pokemons:
      print(pokemon)
    return "The current active Pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)

  def switch_active_pokemon(self, new_active):
    # Switches the active pokemon to the number given as a parameter
    # First check the number is valid (between 0 and length of list)
    if new_active < len(self.pokemons) and new_active >= 0:
      # You can't switch to a pokemon that is knocked out
      if self.pokemons[new_active].is_knocked_out:
        print("{name} is knocked out, you can\'t switch to it now".format(name = self.pokemons[new_active].name))
      # You can't switch to your current active pokemon
      elif new_active == self.current_pokemon:
        print("{name} is already out".format(name = self.pokemons[new_active].name))
      # switches the pokemon
      else:
        self.current_pokemon = new_active
        print("Go {name}, you\'ve got this!".format(name =self.pokemons[self.current_pokemon].name))
      
  def use_potion(self):
    #Uses a potion on the active Pokemon, assuming you have one
    if self.potions > 2:
      print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
      # A potion restores 20 health
      self.pokemons[self.current_pokemon].gain_health(20)
      self.potions -= 1
    elif self.potions == 2:
      print("You used a potion on {name}.\nYou have 1 left.".format(name = self.pokemons[self.current_pokemon].name))
      # A potion restores 20 health
      self.pokemons[self.current_pokemon].gain_health(20)
      self.potions -= 1
    elif self.potions == 1:
      print("You used a potion on {name}.\nThat\'s your last one!".format(name = self.pokemons[self.current_pokemon].name))
      # A potion restores 20 health
      self.pokemons[self.current_pokemon].gain_health(20)
      self.potions -= 1
    else:
      print("You don\'t have any more potions!")

  def use_revive(self):
    # Revive a pokemon back to half health if it's knocked out
    if self.revives > 2:
      self.pokemons[self.current_pokemon].revive
      print("You used a Revive on {name}.".format(name = self.pokemons[self.current_pokemon].name))
      self.revives -= 1
    elif self.revives == 2:
      self.pokemons[self.current_pokemon].revive
      print("You used a Revive on {name}.\nYou have 1 left.".format(name = self.pokemons[self.current_pokemon].name))
      self.revives -= 1
    elif self.revives == 1:
      self.pokemons[self.current_pokemon].revive
      print("You used a revive on {name}.]nThat\'s your last one!".format(name = self.pokemons[self.current_pokemon].name))
      self.revives -= 1
    else:
      print("You don\'t have any more Revives.")

  def attack_other_trainer(self, other_trainer):
    # Your current POkemon attacks the other trainers current pokemon
    my_pokemon = self.pokemons[self.current_pokemon]
    their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
    my_pokemon.attack(their_pokemon)
# Make 12 Pokemon with different levels, if no level is given, it's level 5
charmander = Pokemon("Charmander", "Fire", 7)
squirtle = Pokemon("Squirtle", "Water", 6)
bulbasaur = Pokemon("Bulbasaur", "Grass")
rattata = Pokemon("Rattata", "Normal", 4)
cyndaquil = Pokemon("Cyndaquil", "Fire", 6)
totodile = Pokemon("Totodile", "Water")
chikorita = Pokemon("Chikorita", "Grass", 7)
sentret = Pokemon("Sentret", "Normal", 6)
torchic = Pokemon("Torchic", "Fire")
mudkip = Pokemon("Mudkip", "Water", 7)
treecko = Pokemon("Treecko", "Grass", 6)
zigzagoon = Pokemon("Zigzagoon", "Normal")

pokemons = [charmander, squirtle, bulbasaur, rattata, cyndaquil, totodile, chikorita, sentret, torchic, mudkip, treecko, zigzagoon]
# pokemon_pairs = list(combinations(pokemons, 2))
# random.shuffle(pokemon_pairs)
# for pokemon in pokemon_pairs:
while len(pokemons) > 6:
  pokemon_1 = random.choice(pokemons)
  pokemons.remove(pokemon_1)
  pokemon_2 = random.choice(pokemons)
  pokemons.remove(pokemon_2)
  pokemon_3 = random.choice(pokemons)
  pokemons.remove(pokemon_3)
  pokemon_4 = random.choice(pokemons)
  pokemons.remove(pokemon_4)
  pokemon_5 = random.choice(pokemons)
  pokemons.remove(pokemon_5)
  pokemon_6 = random.choice(pokemons)
  pokemons.remove(pokemon_6)
print(pokemon_1.is_knocked_out)
print(pokemon_2.is_knocked_out)
print(pokemon_3.is_knocked_out)
print(pokemon_4.is_knocked_out)
print(pokemon_5.is_knocked_out)
print(pokemon_6.is_knocked_out)

# Take input for the trainer names and let them select the pokemon they want.
trainer_one_name = input("Hello! Welcome to the world of Pokemon. Please tell me your name.\n")
trainer_two_name = input("Hi, " + trainer_one_name +"!\nThis is your neighbor, could you remind me of their name? \n")

choice = input("Now, let's pick our Pokemon!\n" + trainer_one_name + ", would you like a level {level_1} {name_1} or a level {level_2} {name_2}?\n".format(level_1 = pokemon_1.level, name_1 = pokemon_1.name, level_2 = pokemon_2.level, name_2 = pokemon_2.name) + trainer_two_name + " will get the other.\n")
#+ " or a " + pokemon_2 + "?")
print(choice)
while choice != pokemon_1.name and choice != pokemon_2.name:
  choice = input("Whoops! It looks like you didn't choose {name_1} or {name_2}!\nTry selecting one again.\n".format(name_1 = pokemon_1.name, name_2 = pokemon_2.name))
trainer_one_pokemon = []
trainer_two_pokemon = []
if choice == pokemon_1.name:
  trainer_one_pokemon.append(pokemon_1)
  trainer_two_pokemon.append(pokemon_2)
else:
  trainer_one_pokemon.append(pokemon_2)
  trainer_two_pokemon.append(pokemon_1)

choice = input("Let's choose our second Pokemon\n" + trainer_two_name +", would you like a level {level_3} {name_3} or a level {level_4} {name_4}?\n".format(level_3 = pokemon_3.level, name_3 = pokemon_3.name, level_4=pokemon_4.level, name_4 = pokemon_4.name) + trainer_one_name + " will get the other.\n")
while choice != pokemon_3.name and choice != pokemon_4.name:
  choice = input("Whoops! It looks like you didn't choose {name_3} or {name_4}!\nTry selecting one again.\n".format(name_3 = pokemon_3.name, name_4 = pokemon_4.name))
if choice == pokemon_3.name:
  trainer_one_pokemon.append(pokemon_4)
  trainer_two_pokemon.append(pokemon_3)
else:
  trainer_one_pokemon.append(pokemon_3)
  trainer_two_pokemon.append(pokemon_4)
choice = input("And for your last Pokemon.\n" + trainer_one_name +", would you like a level {level_5} {name_5} or a level {level_6} {name_6}?\n".format(level_5 = pokemon_5.level, name_5 = pokemon_5.name, level_6 = pokemon_6.level, name_6 = pokemon_6.name) + trainer_two_name + " will get the other.\n")
while choice != pokemon_5.name and choice != pokemon_6.name:
  choice = input("Whoops! It looks like you didn't choose {name_5} or {name_6}!\nTry selecting one again.\n".format(name_5 = pokemon_5.name, name_6 = pokemon_6.name))
if choice == pokemon_6.name:
  trainer_one_pokemon.append(pokemon_5)
  trainer_two_pokemon.append(pokemon_6)
else:
  trainer_one_pokemon.append(pokemon_6)
  trainer_two_pokemon.append(pokemon_5)

trainer_one = Trainer(trainer_one_pokemon, 5, 2, trainer_one_name)
trainer_two = Trainer(trainer_two_pokemon, 5, 2, trainer_two_name)

print("Trainer battle!\nPokemon Trainer {name_1} vs Pokemon Trainer {name_2}!".format(name_1 = trainer_one.name, name_2 = trainer_two.name))
print(trainer_one.current_pokemon)
print(trainer_two.current_pokemon)

#Testing attacking, giving potions, and switching pokemon
for i in (1, 20):
  if i % 2 != 0 and i > 20:
    trainer_one_battle_choice = input("""
    {trainer_one_name}, would you like to:
    Attack      Use Potion
    Use Revive  Switch Pokemon
    """.format(trainer_one_name = trainer_one.name))
    if trainer_one_battle_choice == "Attack":
      trainer_one.attack_other_trainer(trainer_two)
    elif trainer_one_battle_choice == "Use Potion":
      trainer_one.use_potion()
    elif trainer_one_battle_choice == "Use Revive":
      trainer_one.use_revive()
    elif trainer_one_battle_choice == "Switch Pokemon":
      lineup = input("""
      To which Pokemon?
      {pokemon_1_name}
      {pokemon_2_name}
      {pokemon_3_name}
      """.format(pokemon_1_name = trainer_one_pokemon[0].name, pokemon_2_name = trainer_one_pokemon[1].name, pokemon_3_name = trainer_one_pokemon[2].name))
      if lineup == trainer_one_pokemon[0].name:
        trainer_one.switch_active_pokemon(0)
      elif lineup == trainer_one_pokemon[1].name:
        trainer_one.switch_active_pokemon(1)
      elif lineup == trainer_one_pokemon[2].name:
        trainer_one.switch_active_pokemon(2)
      else:
        lineup = input("""
        Please select one of the following Pokemon?
        {pokemon_1_name}
        {pokemon_2_name}
        {pokemon_3_name}
        """.format(pokemon_1_name = trainer_one_pokemon[0].name, pokemon_2_name = trainer_one_pokemon[1].name, pokemon_3_name = trainer_one_pokemon[2].name))
    else:
      trainer_one_battle_choice = input("""
      Please choose from one of the following:
      Attack      Use Potion
      Use Revive  Switch Pokemon
      """)
  elif i % 2 == 0 or i == 20:
    trainer_two_battle_choice = input("""
      {trainer_two_name}, would you like to:
      Attack      Use Potion
      Use Revive  Switch Pokemon
      """.format(trainer_two_name = trainer_two.name))
    if trainer_two_battle_choice == "Attack":
      trainer_two.attack_other_trainer(trainer_one)
    elif trainer_two_battle_choice == "Use Potion":
      trainer_two.use_potion()
    elif trainer_two_battle_choice == "Use Revive":
      trainer_two.use_revive()
    elif trainer_two_battle_choice == "Switch Pokemon":
      lineup = input("""
      To which Pokemon?
      {pokemon_1_name}
      {pokemon_2_name}
      {pokemon_3_name}
      """.format(pokemon_1_name = trainer_two_pokemon[0].name, pokemon_2_name = trainer_two_pokemon[1].name, pokemon_3_name = trainer_two_pokemon[2].name))
    if lineup == trainer_two_pokemon[0].name:
      trainer_two.switch_active_pokemon(0)
    elif lineup == trainer_two_pokemon[1].name:
      trainer_two.switch_active_pokemon(1)
    elif lineup == trainer_two_pokemon[2].name:
      trainer_two.switch_active_pokemon(2)
    else:
      lineup = input("""
      Please select one of the following Pokemon?
      {pokemon_1_name}
      {pokemon_2_name}
      {pokemon_3_name}
      """.format(pokemon_1_name = trainer_two_pokemon[0].name, pokemon_2_name = trainer_two_pokemon[1].name, pokemon_3_name = trainer_two_pokemon[2].name))
print("Battle over!")