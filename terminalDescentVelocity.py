import math
def terminalDescentVelocity(weight, Cdrag, airDensity, parachuteArea):
    return(math.sqrt((2*weight)/(Cdrag*airDensity*parachuteArea)))