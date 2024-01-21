def thrustProfile(time):   
    thrustTimes = [0, 0.00776398, 0.0465839, 0.48913, 1.01708, 1.99534, 2.3913, 2.48447, 2.50776, 2.6]
    thrustValues = [0, 1344.83, 1241.38, 1551.72, 1568.97, 1603.45, 1586.21, 1758.62, 103.448, 0]
    if time <= time[len(time) - 1]:
        for i in range(len(thrustTimes)-1):
            if time > thrustTimes[i]:
                fromPoint = time - thrustTimes[i]
                perFromPoint = thrustTimes[i+1] - thrustTimes[i]
                diffThrust = thrustValues[i+1] - thrustValues[i]
                thrust = thrustValues[i] + fromPoint * diffThrust / perFromPoint
    else:
        thrust = 0
    return thrust
