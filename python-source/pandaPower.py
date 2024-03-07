import panda
plot = panda.BambooPlot(
    'Power',
    [16, 8, 4, 2, 1, 1]
)

# Don't change anything above this line
# ===================================

# generate your solution as a list of indices
queue = [0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0, 4,
         0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0, 5]


# Applying constraints and iterating through remaining 
# rates to find out the best amongst others 


#(0,1,0,2,0,1,0,3,4,0,1,0,2,0,1,0,5) -> 17

#(0,1,0,2,0,3) -> 16

#(0,1,0,2,0,1,0,3,4,0,1,0,2,0,1,0,3,5) -> 18
#(0,1,0,2,0,1,0,3,0,4,0,1,0,2,0,1,0,3,0,5) -> 20
#(0,1,0,2,0,1,0,3,0,1,4,0,1,0,2,0,1,0,3,0,1,5) -> 22
#(0,1,0,2,0,1,0,3,0,1,0,4,0,1,0,2,0,1,0,3,0,1,0,5) -> 24

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
