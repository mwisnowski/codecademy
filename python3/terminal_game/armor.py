import random
import numpy as np
from textwrap import dedent
import math
from columnar import columnar
from dice_rolling import *
from items import *
from weapons import *

class Armor:
    # To create armor, it should have a name, a weight class, a material, and any enhancement bonuses
    def __init__(self, name, type_name, enhancement_bonus=0, other_info=""):
        self.name = name
        self.type_name = type_name
        self.weight_class = ""
        self.material = ""
        self.is_metal = False
        self.metallic = ""
        if self.is_metal == True:
            self.metallic = "Yes"
        else:
            self.metallic = "No"
        self.enhancement_bonus = enhancement_bonus
        self.stealth_disadvantage = "No"
        enhancement_bonus = 0
        weight_base_bonus = 0
        type_bonus = 0
        self.is_light = False
        if type_name.lower() == "leather":
            self.weight_class = "Light"
            self.is_light = True
            self.is_medium = False
            self.is_heavy = False
            self.is_metal = False
        elif type_name.lower() == "padded":
            self.weight_class = "Light"
            self.is_light = True
            self.is_metal = False
        elif type_name.lower() == "studded":
            self.weight_class = "Light"
            self.is_light = True
            self.is_metal = False
            type_bonus = 1
        self.is_medium = False
        if type_name.lower() == "hide":
            self.weight_class = "Medium"
            self.is_medium = True
            self.is_metal = False
        elif type_name.lower() == "chain":
            self.weight_class = "Medium"
            self.is_medium = True
            self.is_metal = True
            type_bonus = 1
        elif type_name.lower() == "scale":
            self.weight_class = "Medium"
            self.is_medium = True
            self.stealth_disadvantage = "Yes"
            self.is_metal = True
            type_bonus = 2
        elif type_name.lower() == "breastplate":
            self.weight_class = "Medium"
            self.is_medium = True
            self.stealth_disadvantage = "Yes"
            self.is_metal = True
            type_bonus = 2
        elif type_name.lower() == "halfplate":
            self.weight_class = "Medium"
            self.is_medium = True
            self.stealth_disadvantage = "Yes"
            self.is_metal = True
            type_bonus = 3
        self.is_heavy = False
        if self.is_light == True:
            weight_base_bonus = 1
            self.dex_cap = "None"
        else:
            pass
        if self.is_medium == True:
            weight_base_bonus = 2
            self.dex_cap = "+2"
        else:
            pass
        if self.is_heavy == True:
            weight_base_bonus = 4
            self.dex_cap = "0"
        else:
            pass
        self.base_ac = 10 + weight_base_bonus + type_bonus + enhancement_bonus
        self.other_info = other_info

    def __repr__(self):
        # Printing an armor will tell you it's name, material, damage die, and range
        armor_info = [
            ["\033[1mNAME:\033[0m ", self.name, "\033[1mTYPE:\033[0m ", self.type_name],
            ["\033[1mMETALLIC:\033[0m ", self.metallic, "\033[1mDEX CAP", self.dex_cap],
            ["\033[1mAC Bonus:\033[0m ", self.base_ac, "\033[1mSTEALTH PENALTY:\033[0m ", self.stealth_disadvantage],
        ]
        stat_block = columnar(armor_info)
        return f"{self.other_info}\n{stat_block}"
        
leather_armor = Armor("Leather Armor", "Leather", 0, "Basic leather armor, provides some protection.")
#print(leather_armor)