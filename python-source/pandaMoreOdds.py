import panda
plot = panda.BambooPlot(
    'MoreOdds',
    [9, 7, 7, 5, 5, 3, 3, 3]
)

# Don't change anything above this line
# ===================================

# generate your solution as a list of indices
queue = [0, 4, 2, 5, 1, 0, 6, 2, 4, 1, 0, 3, 2, 7, 1]

#(0, 1, 2, 3, 0, 4, 1, 2, 0, 3, 5, 6) -> 30

#(0, 4, 2, 5, 1, 0, 6, 2, 4, 1, 0, 3, 2, 7, 1) -> 35

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
