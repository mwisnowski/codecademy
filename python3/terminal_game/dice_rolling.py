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

d2 = [x + 1 for x in range(2)]
d4 = [x + 1 for x in range(4)]
d6 = [x + 1 for x in range(6)]
d8 = [x + 1 for x in range(8)]
d10 = [x + 1 for x in range(10)]
d12 = [x + 1 for x in range(12)]
d20 = [x + 1 for x in range(20)]

class DiceSet:
    # Define various values for the common dice
    def __init__(self, d2=d2, d4=d4, d6=d6, d8=d8, d10=d10, d12=d12, d20=d20):
        self.d2 = d2
        self.d4 = d4
        self.d6 = d6
        self.d8 = d8
        self.d10 = d10
        self.d12 = d12
        self.d20 = d20

    def m4d6(self, n_dice=4):
        results = [
            np.random.choice(d6)
            for n
            in range(n_dice)
            ]
        lowest = min(results)
        results.remove(lowest)
        return sum(results)
    
    def roll_death_save(self, n_dice=1, modifier=0):
        result = 0
        while num_rolls < n_dice:
            roll = np.random.choice(d20)
            if roll == 20:
                print("Nat 20!\nAuto success!")
                self.death_save_succed += 1
            if roll == 1:
                print("Nat 1!\n Auto failure!")
                self.death_save_fail -= 1
            death_save_roll = roll + modifier
            result += death_save_roll
            num_rolls += 1

    def ability_check(self, n_dice=1, modifier=0, advantage=False, disadvantage=False):
        total = 0
        totals = []
        num_rolls = 0
        while num_rolls < n_dice:
            roll = np.random.choice(d20)
            if roll == 20:
                print("Nat 20!\nAuto success!")
            if roll == 1:
                print("Nat 1!\n Auto failure!")
            ability = roll + modifier

            if (ability == 20) and (modifier != 0):
                print("Modified 20")
            total += ability
            totals.append(ability)
            num_rolls += 1
        
        if advantage == True:
            print(totals)
            return f"Rolled: {max(totals)}"
        elif disadvantage == True:
            print(totals)
            return f"Rolled: {min(totals)}"
        else:
            return f"Rolled: {total}"
