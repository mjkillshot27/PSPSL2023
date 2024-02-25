def thrustProfile(time):
    #Gotten from thrust curve
    thrust = 0
    thrustTimes = [0, 0.00776398, 0.0465839, 0.48913, 1.01708, 1.99534, 2.3913, 2.48447, 2.50776, 2.6]
    thrustValues = [0, 1344.83, 1241.38, 1551.72, 1568.97, 1603.45, 1586.21, 1758.62, 103.448, 0]
    
    #Gets the last thrust time
    if time <= thrustTimes[len(thrustTimes) - 1]:
        for i in range(len(thrustTimes)-1):
            if (time > thrustTimes[i] and time < thrustTimes[i+1]):
                #Takes current time and subtracts if by thrust time
                fromPoint = time - thrustTimes[i]
                
                #Gap between the two thrust times and actual thrust values
                perFromPoint = thrustTimes[i+1] - thrustTimes[i]
                diffThrust = thrustValues[i+1] - thrustValues[i]
                
                #Linearizes it
                thrust = thrustValues[i] + fromPoint * diffThrust / perFromPoint
                break
    else:
        thrust = 0
    return thrust
#print(thrustProfile(3))