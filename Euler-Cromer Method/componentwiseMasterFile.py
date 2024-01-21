from thrustProfile import thrustProfile
import numpy as np
import matplotlib.pyplot as plt
import math
G = 6.674e-11
M_earth = 5.972e24
airDensity = 1.293 #kg/m^3
z0 = 0
v0 = 0
v = v0
z = z0
V = v
Z = z
vx = 0
vy = 0
launchAngle = 90
angle = launchAngle
windSpeed = 0
m = 18.7674 #initial mass
M = m
tmax = 100
amountOfIterations = 1000
dt = tmax / amountOfIterations
Cd = 0.3
g=9.8
burnTime = 26 #tenths of seconds
engineMass = 3.54369
payloadDeploymentHeight = 152.4 #ft
payloadMass = 3.40194
altitude = [0]
velocity = [0]
def dm (time, z):
    count = 0
    if time<burnTime: 
        return (engineMass/burnTime)
    elif time>50 and z < payloadDeploymentHeight and count == 0:
        count+=1
        return payloadMass
    else:
        return 0
    
def Cd(time, z):
    if time > 100 and z <= 213.36:
        return 1.6
    else:
        return 0.453
t = np.linspace(0,tmax,amountOfIterations + 1)
def area(time, z):
    if time> 10 and z <= 213.36:
        return (3.048/2)*(3.048/2)*math.pi
    else:
        return (0.131318/2)*(0.131318/2)*math.pi
parachuteDeploymentCounter = 0
for time in range(0, amountOfIterations):
    m = m - (dm(t[time], z) * dt)

    if z <= 213.36 and time > 200 and parachuteDeploymentCounter == 0:
        v = -3
        parachuteDeploymentCounter = parachuteDeploymentCounter + 1

    drag = 0.5 * airDensity * v * v * Cd(t[time], z) * area(t[time], z) / m
    if v < 0:
        drag = drag * -1

    thrust = thrustProfile(t[time])

    vx = vx + (thrust / m - drag) * np.cos(angle) * dt -windSpeed * dt
    vy = vy + (thrust / m - drag) * np.sin(angle) * dt - g*dt

    v = np.sqrt(vx * vx + vy * vy)

    if np.abs(vx) < 0.0001:
        angle = 90
    else:
        angle = np.arctan2(vy, vx)

    z = z + vy * dt

    altitude.append(z * 3.281)
    velocity.append(v * 3.281)

    if z < 0:
        break
    print("vy", vy)
    print('time', t[time])
altitude.append(1)
plt.plot(range(len(altitude)),altitude)
plt.show()