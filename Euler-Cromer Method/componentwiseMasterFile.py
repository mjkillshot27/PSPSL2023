from thrustProfile import thrustProfile
import numpy as np
import matplotlib.pyplot as plt
import math
G = 6.674e-11
M_earth = 5.972e24
airDensity = 1.293 #kg/m^3
dt = 0.1
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
Cd = 0.3
g=9.8
altitude = [0]
velocity = [0]
def dm (time, z):
    if time<2.6:
        return (3.54369/2.6)
    elif time>50 and z == 500:
        return 3.40194
    else:
        return 0
    
def Cd(time, z):
    if time> 10 and z <= 213.36:
        return 1.6
    else:
        return 0.453
t = np.linspace(0,tmax,1001)
def area(time, z):
    if time> 10 and z <= 213.36:
        return (3.048/2)*(3.048/2)*math.pi
    else:
        return (0.131318/2)*(0.131318/2)*math.pi
for time in range(0,300):
    m = m - (dm(t[time], z)*dt)
    parachuteDeploymentCounter = 0
    if z<=213.36  and time>200 and parachuteDeploymentCounter == 0:
        v = -3
        parachuteDeploymentCounter = parachuteDeploymentCounter +1
    
    drag = 0.5 *airDensity * v * v *Cd(t[time], z)*area(t[time], z) / m
    print(drag)
    if v < 0:
        drag = drag*-1
    v = v + (thrustProfile(t[time])/m - drag - g)*dt
    vx = (v + (thrustProfile(t[time])/m - drag - g))*np.cos(angle * np.pi/180)*dt
    vy = (v + (thrustProfile(t[time])/m - drag - g))*np.sin(angle * np.pi/180)*dt
    if vx == 0:
        angle = 90
    else:
        angle = np.arctan(vy/vx)
    print("m",m)
    print("v",v)
    print("vx", vx)
    print("vy", vy)
    z = z + vy*dt
    print("drag")
    print(drag)
    print("velocity")
    print(v)
    print("time")
    print(t[time])
    print("height")
    print(z)
    altitude.append(z*3.281)
    velocity.append(vy*3.281)
    if z <0:
        break
altitude.append(1)
plt.plot(range(len(altitude)),altitude)
plt.show()