import random
import numpy as np
from textwrap import dedent
import math
from columnar import columnar
from dice_rolling import *
from weapons import *
from items import *

class Player:
    # To create a player, you'll need a name, then you'll roll for some stats. Your health will depend on your level, class, and your consitution
    def __init__(self, name, race, strength, dexterity, constitution, intelligence, wisdom, charisma, character_class, class_hit_die, level = 1):
        self.name = name
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.strength_mod = math.floor((strength - 10) / 2)
        self.dexterity_mod = math.floor((dexterity - 10) / 2)
        self.constitution_mod = math.floor((constitution - 10) / 2)
        self.intelligence_mod = math.floor((intelligence - 10) / 2)
        self.wisdom_mod = math.floor((wisdom - 10) / 2)
        self.charisma_mod = math.floor((charisma - 10) / 2)
        self.character_class = character_class
        self.class_hit_die = class_hit_die
        self.level = level
        self.health = level * (class_hit_die + self.constitution_mod)
        self.max_health = level * (class_hit_die + self.constitution_mod)
        self.is_bleeding_out = False
        # self.death_saves_left = 3
        self.death_saves_succeed = 0
        self.death_saves_failed = 0
        self.is_dead = False
    
    def __repr__(self):
        # Prints a short overview of the player character
        character_info = [
            ["\033[1mNAME:\033[0m ", self.name, "", ""],
            ["\033[1mLEVEL:\033[0m ", self.level, "\033[1mRACE:\033[0m ", self.race],
            [f"\033[1mClass\033[0m", self.character_class, "", ""],
            ["\033[1mCURRENT HP:\033[0m ", self.health, "\033[1mMAX HP:\033[0m ", self.max_health],
            ["\033[1mABILITY SCORES:\033[0m", "", "\033[1mABILITY MODIFIERS:\033[0m", ""],
            ["STR:", self.strength, "Modifier:", f"+{self.strength_mod}"],
            ["DEX:", self.dexterity, "Modifier:", f"+{self.dexterity_mod}"],
            ["CON:", self.constitution, "Modifier:", f"+{self.constitution_mod}"],
            ["INT:", self.intelligence, "Modifier:", f"+{self.intelligence_mod}"],
            ["WIS:", self.wisdom, "Modifier:", f"+{self.wisdom_mod}"],
            ["CHA:", self.charisma, "Modifier:", f"+{self.charisma_mod}"]
        ]
        character_sheet = columnar(character_info)
        return character_sheet
    
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.bleeding_out
        else:
            print(f"You took {amount} damage and now have {self.health} HP left")
    
    def attack(self):
        pass
    def heal(self):
        pass
    def escape(self):
        pass
    
    def bleeding_out(self):
        self.is_bleeding_out = True
        if self.health >= 1:
            print(f"You've stabilized with {self.health} HP now.")
            self.is_bleeding_out = False
            self.death_saves_failed = 0
            self.death_saves_succeed = 0
        else:
            pass
        if self.death_saves_failed < 3 and self.is_bleeding_out == True and self.death_saves_succeed < 3:
            # make a death save
            death_saving_throw = DiceSet()
            if death_saving_throw.roll_death_save(1, self.constitution_mod) >= 10:
                print("Successful death save, one step closer to stabilized.")
                self.death_saves_succeed += 1
            elif death_saving_throw.roll_death_save(1, self.constitution_mod) < 10:
                print("Successful death save, one step closer to stabilized.")
                self.death_saves_failed -= 1
        elif self.death_saves_failed < 3 and self.is_bleeding_out == True and self.death_saves_succeed == 3:
            self.health += 1
        elif self.death_saves_failed == 3 and self.is_bleeding_out == True and self.death_saves_succeed < 3:
            print("You bleed out and die, please play again.")
            self.is_dead = True
    
    def inventory(self):
        pass

p1_name = input("Hello!\nPlease enter your name:\n")
p1_race = input("What race is your character?\n")

#Let's get some class descriptions
class_descriptions = input("Before we choose our class, would you like to learn more about any of them?\n")
while(True):
    if class_descriptions.lower() == "yes":
        which_class = input(dedent("""
                        Which class would you like to learn more about?
                        Barbarian  Bard    Cleric
                        Druid      Fighter Monk
                        Paladin    Ranger  Rogue
                        Sorcerer   Warlock Wizard
                                   
                        Or say no/cancel/nevermind/leave if you are done.

                        """))
        if which_class.lower() == "barbarian":
            print("The Barbarian is a strong melee fighter with powerful rage abilities.\nHit Die: d12\nPrimary Ability: Strength\nSaving throws: Strength and Constitution\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "bard":
            print("The Bard uses their wit and cutting words to empower allies and weaken enemies.\nHit Die: d8\nPrimary Ability: Charisma\nSaving throws: Dexterity and Charisma\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "cleric":
            print("The Cleric wields divine magic from their gods to aid allies and defeat foes.\nHit Die: d8\nPrimary Ability: Wisdom\nSaving throws: Wisdom and Charisma\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "druid":
            print("The Druid is one with nature, using natural magics and taking animal shapes.\nHit Die: d8\nPrimary Ability: Charisma\nSaving throws: Dexterity Intelligence and Wisdom\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "fighter":
            print("The Fighter is a master of martial combat, skilled in many a weapon and armor.\nHit Die: d10\nPrimary Ability: Strength or Dexterity\nSaving throws: Strength and Constitution\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "monk":
            print("The Monk is a master of martial arts, using their body in pursuit of physical and spiritual perfection.\nHit Die: d8\nPrimary Abilities: Dexterity and Wisdom\nSaving throws: Strength and Wisdom\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "paladin":
            print("The Paladin is a holy warrior bound to and empowered by a sacred oath.\nHit Die: d10\nPrimary Abilities: Strength and Charisma\nSaving throws: Wisdom and Charisma\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "ranger":
            print("The Ranger is a warrior combatting threats in the edges of civilization.\nHit Die: d10\nPrimary Abilities: Dexterity and Wisdom\nSaving throws: Strength and Dexterity\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "rogue":
            print("The Rogue is a master of stealth that prefers to slip in and attack while undetected.\nHit Die: d8\nPrimary Ability: Dexterity\nSaving throws: Dexterity and Intelligence\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "sorcerer":
            print("The Sorcerer wields powerful magics granted to them by their bloodline.\nHit Die: d6\nPrimary Ability: Charisma\nSaving throws: Constitution and Charisma\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "warlock":
            print("The Warlock has been granted magic from an extraplanar being.\nHit Die: d8\nPrimary Ability: Charisma\nSaving throws: Wisdom and Charisma\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "wizard":
            print("The Wizard has spent years studying the arcane to cast powerful spells.\nHit Die: d6\nPrimary Ability: Intelligence\nSaving throws: Intelligence and Wisdom\n\nPress Enter to continue.")
            input()
            continue
        elif which_class.lower() == "no" or which_class.lower() == "cancel" or which_class.lower() == "nevermind" or which_class.lower() == "leave":
            print("Alright then, let's move on to choosing a class.")
            break
        else: 
            print("Please choose a class.")
            continue
    else:
        pass
    break

    
p1_class = input(dedent("""
                 What class would you like to play?
                 Barbarian  Bard    Cleric
                 Druid      Fighter Monk
                 Paladin    Ranger  Rogue
                 Sorcerer   Warlock Wizard
                """))
# assign default ability scores
p1_str = 10
p1_dex = 10
p1_con = 10
p1_int = 10
p1_wis = 10
p1_cha = 10
p1_hit_die = 10

# Assign hit die
if p1_class == "Barbarian":
    p1_hit_die = 12
elif p1_class == "Paladin" or p1_class == "Fighter" or p1_class == "Ranger":
    p1_hit_die = 10
elif p1_class == "Bard" or p1_class == "Druid" or p1_class == "Monk" or p1_class == "Rogue" or p1_class == "Warlock":
    p1_hit_die = 8
else:
    p1_hit_die = 6

roll_ability_scores = input("Let's roll for some ability scores!\nPress the Enter Key when you're ready.\n")
ability_roller = DiceSet()
#roll_1 = stat_roller.m4d6()
#roll_2 = stat_roller.m4d6()
#roll_3 = stat_roller.m4d6()
#roll_4 = stat_roller.m4d6()
#roll_5 = stat_roller.m4d6()
#roll_6 = stat_roller.m4d6()
ability_rolls = []
while len(ability_rolls) < 8:
    ability_rolls.append(ability_roller.m4d6())
    if len(ability_rolls) == 8:
        break
while len(ability_rolls) > 7:
    lowest = min(ability_rolls)
    ability_rolls.remove(lowest)

# print(ability_rolls)
# Roll for Strength, choosing from array.
roll_str = int(input(f"You rolled for your ability scores, which would you like to use for your STR score?\nPlease enter from the following:\n{ability_rolls}\n"))
p1_str = roll_str
ability_rolls.remove(roll_str)

# Roll for Dexterity, choosing from array.
roll_dex = int(input(f"Now, which would you like to use for your DEX score?\nPlease enter from the following:\n{ability_rolls}\n"))
p1_dex = roll_dex
ability_rolls.remove(roll_dex)

# Roll for Constitution, choosing from array.
roll_con = int(input(f"Now, which would you like to use for your CON score?\nPlease enter from the following:\n{ability_rolls}\n"))
p1_con = roll_con
ability_rolls.remove(roll_con)

# Roll for Intelligence, choosing from array.
roll_int = int(input(f"On to the mental stats, which would you like to use for your INT score?\nPlease enter from the following:\n{ability_rolls}\n"))
p1_int = roll_int
ability_rolls.remove(roll_int)

# Roll for Wisdom, choosing from array.
roll_wis = int(input(f"Almost there, which would you like to use for your WIS score?\nPlease enter from the following:\n{ability_rolls}\n"))
p1_wis = roll_wis
ability_rolls.remove(roll_wis)

# Roll for Charisma, choosing from array.
roll_cha = int(input(f"Now, which would you like to use for your CHA score?\nPlease enter from the following:\n{ability_rolls}\n"))
p1_cha = roll_cha
ability_rolls.remove(roll_cha)

# Add floating ability bonuses.
plus_two_bonus = input("Which ability score would you like put your plus two bonus into?\n")
while plus_two_bonus.lower() == "strength" or plus_two_bonus.lower() == "dexterity" or plus_two_bonus.lower() == "constitution" or plus_two_bonus.lower() == "intelligence" or plus_two_bonus.lower() == "wisdom" or plus_two_bonus.lower() == "charisma":
    if plus_two_bonus.lower() == "strength":
        p1_str += 2
    elif plus_two_bonus.lower() == "dexterity":
        p1_dex += 2
    elif plus_two_bonus.lower() == "constitution":
        p1_con += 2
    elif plus_two_bonus.lower() == "intelligence":
        p1_int += 2
    elif plus_two_bonus.lower() == "wisdom":
        p1_wis += 2
    elif plus_two_bonus.lower() == "charisma":
        p1_cha += 2
    break
else:
    plus_two_bonus = input("Make sure you enter a valid ability score name.\n")

# Add floating ability bonuses.
plus_one_bonus = input("Which ability score would you like put your plus one bonus into?\n")
while plus_one_bonus.lower() == "strength" or plus_two_bonus.lower() == "dexterity" or plus_two_bonus.lower() == "constitution" or plus_two_bonus.lower() == "intelligence" or plus_two_bonus.lower() == "wisdom" or plus_two_bonus.lower() == "charisma":
    if plus_one_bonus.lower() == "strength":
        p1_str += 1
    elif plus_one_bonus.lower() == "dexterity":
        p1_dex += 1
    elif plus_one_bonus.lower() == "Constitution":
        p1_con += 1
    elif plus_one_bonus.lower() == "intelligence":
        p1_int += 1
    elif plus_one_bonus.lower() == "wisdom":
        p1_wis += 1
    elif plus_one_bonus.lower() == "charisma":
        p1_cha += 1
    break
else:
    plus_one_bonus = input("Make sure you enter a valid ability score name.\n")