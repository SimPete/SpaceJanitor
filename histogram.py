def histogram(nb_dice):

## Imports
    import numpy as np
    import matplotlib.pyplot as plt
    import random

## Initialize
    a = []
## roll dice
    for x in range(nb_dice):
        dice= random.randint(0,6)
        a.append(dice) 
        #print(a) 

    plt.hist(a) 
    plt.show()