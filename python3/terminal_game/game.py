import random
import numpy as np
from textwrap import dedent
import math
from columnar import columnar
from character_creation import *
from dice_rolling import *
from weapons import *
from items import *
from monsters import *
player_one = Player(p1_name, p1_race, p1_str, p1_dex, p1_con, p1_int, p1_wis, p1_cha, p1_class, p1_hit_die, 1)
input(f"Here's your character, does that look right?\n{player_one}")

print("Oh no, you triggered a trap and take 12 damage!")
player_one.lose_health(12)
#input("You find a goblin, it's time to fight!\n")
#input(f"What would you like to do?\n>Attack\n>Heal\n>Escape\n")


#player_one = 
#    def toggle_equip(self):
        # Set item status and call it's equip/unequip functions
#        if self.two_handed == False:
#            hand = input("Which hand would you like to equip {name} to?\n")
#            if hand == "Right":
#                self.equipped_right_hand
        
#axes = ["Handaxe", "Throwing Axe", "Battleaxe", "Greataxe"]
#weapons = [swords, axes, "Dagger", "Spear", "Mace"]
#ranged_weapons = ["Shortbow", "Longbow", "Crossbow", "Hand Crossbow"]
#shield = "Shield"M