import panda
plot = panda.BambooPlot(
    'Oversupply',
    [10, 10, 5]
)

# Don't change anything above this line
# ===================================

# generate your solution as a list of indices
queue = [2, 0, 1, 0]

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
