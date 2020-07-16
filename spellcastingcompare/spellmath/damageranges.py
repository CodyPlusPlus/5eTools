# damageranges.py
# Author: Cody Stuck
# The purpose of this file is to determine the minimum, maximum and average roll value of a spell with specified scaling

def minDamage(baseLevel, castLevel, baseNumDice, baseBonus, upcastNumDice=0, upcastBonus=0):
    if castLevel == baseLevel: # first, figure out of this is an upcast spell...
        return(baseNumDice + baseBonus)
    else: # ... or not.
        return(baseNumDice + baseBonus + ((castLevel - baseLevel) * upcastNumDice) + ((castLevel - baseLevel) * upcastBonus))

def maxDamage(baseLevel, castLevel, baseNumDice, baseDiceSize, baseBonus, upcastNumDice=0, upcastDiceSize=0, upcastBonus=0):
    if castLevel == baseLevel: # first, figure out of this is an upcast spell...
        return((baseNumDice * baseDiceSize) + baseBonus)
    else: # ... or not.
        return((baseNumDice * baseDiceSize) + baseBonus + ((castLevel - baseLevel) * (upcastNumDice * upcastDiceSize)) + ((castLevel - baseLevel) * upcastBonus))

def averageDamage(baseLevel, castLevel, baseNumDice, baseDiceSize, baseBonus, upcastNumDice=0, upcastDiceSize=0, upcastBonus=0):
    if castLevel == baseLevel: # first, figure out of this is an upcast spell...
        return(baseNumDice * ((baseDiceSize / 2) + 0.5) + baseBonus)
    else: # ... or not.
        return((baseNumDice * ((baseDiceSize / 2) + 0.5)) + baseBonus + ((castLevel - baseLevel) * (upcastNumDice * ((upcastDiceSize / 2) + 0.5))) + ((castLevel - baseLevel) * upcastBonus))