import random
import numpy as np
from textwrap import dedent
import math
from fractions import Fraction
from columnar import columnar
from dice_rolling import *
from weapons import *
from items import *
from armor import *

class Monster:
    # To create a monster it will need a name and some stats
    def __init__(self, name, monster_type, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_die, weight_class="", has_shield=False, speed=30, challenge = Fraction(1), level = 1):
        self.name = name
        self.monster_type = monster_type
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
        self.weight_class = weight_class
        self.armor_bonus = 0
        if self.weight_class.lower() == "light":
            self.armor_bonus = 1
        elif self.weight_class.lower() == "medium":
            self.armor_bonus = 2
        elif self.weight_class.lower() == "heavy":
            self.armor_Bonus = 4
        self.has_shield = has_shield
        self.shield = 0 
        if has_shield == True:
            self.shield = 2
        self.dexterity_mod_for_ac = self.dexterity_mod
        if self.weight_class.lower() == "light":
            self.dexterity_mod_for_ac = self.dexterity_mod
        if self.weight_class.lower() == "medium":
            self.dexterity_mod_for_ac = min(2, self.dexterity_mod)
        if self.weight_class.lower() == "heavy":
            self.dexterity_mod_for_ac = 0
        self.armor_class = 10 + self.dexterity_mod_for_ac + self.armor_bonus + self.shield
        self.speed = speed
        self.hit_die = hit_die
        self.challenge = challenge
        self.level = level
        self.health = level * ((hit_die / 2) + 0.5 + self.constitution_mod)
        self.max_health = level * ((hit_die / 2) + 0.5 + self.constitution_mod)
    
    def __repr__(self):
    # Prints a short overview of the player character
        monster_info = [
            ["\033[1mNAME:\033[0m ", self.name, "\033[1mTYPE:\033[0m ", self.monster_type],
            ["\033[1mCHALLENGE RATING:\033[0m ", self.challenge, "", ""],
            ["\033[1mAC:\033[0m ", self.armor_class, "\033[1mSPEED:\033[0m ", self.speed],
            ["\033[1mCURRENT HP:\033[0m ", self.health, "\033[1mMAX HP:\033[0m ", self.max_health],
            ["\033[1mABILITY SCORES:\033[0m", "", "\033[1mABILITY MODIFIERS:\033[0m", ""],
            ["STR:", self.strength, "Modifier:", f"{self.strength_mod}"],
            ["DEX:", self.dexterity, "Modifier:", f"{self.dexterity_mod}"],
            ["CON:", self.constitution, "Modifier:", f"{self.constitution_mod}"],
            ["INT:", self.intelligence, "Modifier:", f"{self.intelligence_mod}"],
            ["WIS:", self.wisdom, "Modifier:", f"{self.wisdom_mod}"],
            ["CHA:", self.charisma, "Modifier:", f"{self.charisma_mod}"]
        ]
        stat_block = columnar(monster_info)
        return stat_block
    
    def equip_armor(self, armor_name):
        self.armor_name = armor_name
        self.weight_class = ""
    
goblin = Monster("Goblin", "Humanoid", 8, 14, 10, 10, 8, 8, 6, "Light", True, 30, Fraction(1/4), 2)
#goblin.equip_armor("Leather Armor")
print(goblin)