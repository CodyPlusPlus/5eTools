# __main__.py
# Author: Cody Stuck
# test driver for damageranges.py and upscalespell.py

import spellmath.damageranges as dr
import spellmath.upscalespell as us

"""fireballStats = (dr.minDamage(3, 3, 8, 0), dr.averageDamage(3, 3, 8, 6, 0), dr.maxDamage(3, 3, 8, 6, 0))
fireballString = "Fireball has a min damage of %d (should be 8), an avg damage of %d (should be 28), and a max damage of %d (should be 48)"

print(fireballString % fireballStats)

fireballMins = us.findMins(3, 9, 8, 0, 1, 0)

print("Fireball's minimum damage numbers are %s" % fireballMins)

fireballMaxes = us.findMaxes(3, 9, 8, 6, 0, 1, 6, 0)

print("Fireball's maximum damage numbers are %s" % fireballMaxes)"""
fireballAllStats = us.findAll(3, 9, 8, 6, 0, 1, 6, 0)

print("Fireball's damage numbers are %s" % fireballAllStats)