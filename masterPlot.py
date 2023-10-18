import matplotlib.pyplot as plt
from horizontalDisplacement import horizontalDisplacement
from verticalDisplacement import verticalDisplacement
import numpy as np
windSpeed = [0,5,10,15,20]
apogee = [5013, 5007, 4943, 4863, 4865]
time = np.linspace(0,100,500)
horizontalDriftDistance = [[],[],[],[],[]]
verticalDistance= [[],[],[],[],[]]
for i in range(0,5):
    verticalDistance[i].append(apogee[i])
for i in range(0,5):        
    for j in range(0,500):
        horizontalDriftDistance[i].append(horizontalDisplacement(windSpeed[i], time[j]))
for i in range(0,5):
    for j in range(1,500):
        verticalDistance[i].append(verticalDisplacement)
fig, axs = plt.subplots(2,3)
axs[0,0].plot(time,horizontalDriftDistance[0])
axs[0,1].plot(time,horizontalDriftDistance[1])
axs[0,2].plot(time,horizontalDriftDistance[2])
axs[1,0].plot(time,horizontalDriftDistance[3])
axs[1,1].plot(time,horizontalDriftDistance[4])
plt.show()
