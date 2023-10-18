import matplotlib.pyplot as plt
from horizontalDisplacement import horizontalDisplacement
from verticalDisplacement import verticalDisplacement
from terminalDescentVelocity import terminalDescentVelocity
from weightDescent import weightDescent
import numpy as np
import math
windSpeed = [0,5,10,15,20] #m/s
apogee = [5013, 5007, 4943, 4863, 4865] #mph
time = np.linspace(0,100,500)
massWithoutMotor = 15.2237 #kg
massPayload = 3.40194 #kg
horizontalDriftDistance = [[],[],[],[],[]]
verticalDistance= [[],[],[],[],[]]
heightParachuteDeployment = 213.16 #m
heightPayloadDeployment = 152.4 #m
airDensity = 1.293 #kg/m^3
cDrag = 1.6
parachuteArea = (3.048/2)*(3.048/2) *math.pi
for i in range(0,5):
    verticalDistance[i].append(apogee[i])
for i in range(0,5):        
    for j in range(0,500):
        horizontalDriftDistance[i].append(horizontalDisplacement(windSpeed[i], time[j]))
for i in range(0,5):
    for j in range(1,500):
        if(verticalDistance[i],[j] > heightParachuteDeploy):
            verticalDistance[i][j].append(verticalDisplacement(verticalDistance[i][j-1]), 0.2, terminalDescentVelocity(verticalDistance[i][j-1], massWithoutMotor, 0.3082, airDensity, (0.131318/2)(0.131318/2)*math.pi))
        else:
            verticalDistance[i][j].append(verticalDisplacement(verticalDistance[i][j-1]), 0.2, terminalDescentVelocity(verticalDistance[i][j-1], weightDescent(verticalDistance[i][j-1],massWithoutMotor, massPayload, heightPayloadDeployment), cDrag, airDensity, parachuteArea))
fig, axs = plt.subplots(2,3)
#horizontal displacement graphs
axs[0,0].plot(time,horizontalDriftDistance[0])
axs[0,1].plot(time,horizontalDriftDistance[1])
axs[0,2].plot(time,horizontalDriftDistance[2])
axs[1,0].plot(time,horizontalDriftDistance[3])
axs[1,1].plot(time,horizontalDriftDistance[4])
plt.show()
