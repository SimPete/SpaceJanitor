""" Rules
Brasse 5 dés.
    1: moppe 
    2: caca
    3: 1 point
    4: 2 points
    5: multiplicateur
    6: 2^n

Check des cacas et Calcul preliminaire des points
Check:
    1. Si trop de caca:
        1. rerouler 1 dé pour 2$. 
        Sinon, on perd son tour. 
    2. Si assez de moppe, on peut:
        1: rerouler tous les dés+1. 
        2. rerouler un seul dé pour 2$.
        2: prendre le pointage et finir son tour.
"""

## Imports
import numpy as np
import matplotlib.pyplot as plt
import random
from histogram import histogram
from print import print_dice_results

## Initialize
nb_dice = 5
dice_results=[]

dice_dictionary= {}
dice_dictionary['1'] = ['moppe', 'moppes']
dice_dictionary['2'] = ['crotte', 'crottes']

dice_dictionary['1'][1]

# histogram(50000) #For verification of dice rolls

## roll dice
for x in range(nb_dice):
    dice= random.randint(1,6)
    dice_results.append(dice)
print(dice_results)
#print_dice_results(dice_results, 1, dice_dictionary)
#print_dice_results(dice_results, 2, dice_dictionary)

## check option

## 