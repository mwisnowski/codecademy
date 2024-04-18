import random
import numpy as np
from textwrap import dedent
import math
from columnar import columnar
from dice_rolling import *
from items import *
from weapons import *

class Weapons:
    # To create a weapon, it should have a name, a weapon shape, a damage die, and a range it can interact with. By default it will not be equipped in either hand
    def __init__(self, name, damage_die, damage_type, range, right_hand_equip, left_hand_equip, two_handed):
        self.name = name
        self.damage_die = damage_die
        self.damage_type = damage_type
        self.range = range
        self.right_hand_equip = right_hand_equip
        self.left_hand_equip = left_hand_equip
        self.two_handed = two_handed
        self.is_equipped_right_hand = False
        self.is_equipped_left_hand = False
        self.is_equipped_two_hand = False

    def __repr__(self):
        # Printing a weapon will tell you it's name, weapon shape, damage die, and range
        if self.right_hand_equip == True and self.left_hand_equip == False:
            return "A {name}.\nWill deal {damage_die} {damage_type}, with an effective range of {range} units.\nCan only be equipped in the main hand.".format(name = self.name, damage_die = self.damage_die, damage_type = self.damage_type, range = self.range)
        if self.right_hand_equip == True and self.left_hand_equip == True:
            return "A {name}.\nWill deal {damage_die} {damage_type}, with an effective range of {range} units.\nCan be equipped in either hand.".format(name = self.name, damage_die = self.damage_die, damage_type = self.damage_type, range = self.range)
        if self.right_hand_equip == False and self.left_hand_equip == True:
            return "A {name}.\nWill deal {damage_die} {damage_type}, with an effective range of {range} units.\nCan only be equipped in the off hand.".format(name = self.name, damage_die = self.damage_die, damage_type = self.damage_type, range = self.range)
        if self.two_handed == True:
            return "A {name}.\nWill deal {damage_die} {damage_type}, with an effective range of {range} units.\nCan only be equipped with both hands.".format(name = self.name, damage_die = self.damage_die, damage_type = self.damage_type, range = self.range)