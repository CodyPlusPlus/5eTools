import matplotlib.pyplot as plt
import numpy as np
import spellmath.upscalespell as us

def plotSpells(spellA, spellB):
    maxDamage = max((max(map(max, spellA))),(max(map(max, spellB))))

    spellAX, spellBX = [i for i in range((10 - len(spellA[0])), 10)], [i for i in range((10 - len(spellB[0])), 10)]

    for i in range(3):
        plt.plot(spellAX, spellA[i], 'o-r')
        plt.plot(spellBX, spellB[i], 'o-b')

    plt.axes([0,9,0,maxDamage])

    plt.show()

    return(plt)