# damageranges.py
# Author: Cody Stuck
# The purpose of this file is to determine the minimum, maximum and average roll value of a spell considering all levels of casting

import spellmath.damageranges as dr

def findMins(baseLevel, maxLevel, baseNumDice, baseBonus, upcastNumDice=0, upcastBonus=0):
    minimums = [dr.minDamage(baseLevel, l, baseNumDice, baseBonus, upcastNumDice, upcastBonus) for l in range(baseLevel, maxLevel + 1)]
    return minimums

def findMaxes(baseLevel, maxLevel, baseNumDice, baseDiceSize, baseBonus, upcastNumDice=0, upcastDiceSize=0, upcastBonus=0):
    maximums = [dr.maxDamage(baseLevel, l, baseNumDice, baseDiceSize, baseBonus, upcastNumDice, upcastDiceSize, upcastBonus) for l in range(baseLevel, maxLevel + 1)]
    return maximums

def findAvgs(baseLevel, maxLevel, baseNumDice, baseDiceSize, baseBonus, upcastNumDice=0, upcastDiceSize=0, upcastBonus=0):
    maximums = [dr.averageDamage(baseLevel, l, baseNumDice, baseDiceSize, baseBonus, upcastNumDice, upcastDiceSize, upcastBonus) for l in range(baseLevel, maxLevel + 1)]
    return maximums

def findAll(baseLevel, maxLevel, baseNumDice, baseDiceSize, baseBonus, upcastNumDice=0, upcastDiceSize=0, upcastBonus=0):
    allStats = [findMins(baseLevel, maxLevel, baseNumDice, baseBonus, upcastNumDice, upcastBonus),
                findAvgs(baseLevel, maxLevel, baseNumDice, baseDiceSize, baseBonus, upcastNumDice, upcastDiceSize, upcastBonus),
                findMaxes(baseLevel, maxLevel, baseNumDice, baseDiceSize, baseBonus, upcastNumDice, upcastDiceSize, upcastBonus)]
    return (allStats)