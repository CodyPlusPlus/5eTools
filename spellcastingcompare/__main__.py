import spellmath.upscalespell as us
import visualization.graphcreation as gc

fireballAllStats = us.findAll(3, 9, 8, 6, 0, 1, 6, 0)
magicMissileStats = us.findAll(1, 9, 3, 4, 3, 1, 4, 1)

gc.plotSpells(fireballAllStats, magicMissileStats)