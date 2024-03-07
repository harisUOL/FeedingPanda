import panda
plot = panda.BambooPlot(
    'Odds',
    [9, 7, 7, 5, 5, 3, 3]
)

# Don't change anything above this line
# ===================================

# generate your solution as a list of indices
queue = [0, 4, 1, 2, 0, 3, 5, 4, 0, 1, 2, 3]

# Restricting first bamboo to occur every 4th day:

# (0, 4, 1, 2, 0, 3, 5, 4, 0, 1, 2, 3, 5) -> 18

# (0, 4, 1, 2, 0, 3, 4, 0, 1, 2, 3, 5) -> 25

# (0, 4, 1, 2, 0, 3, 5, 4, 0, 1, 2, 3) -> 30

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
