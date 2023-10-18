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
m = 18.7674
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
        return 0.3
t = np.linspace(0,tmax,1001)
def area(time, z):
    if time> 10 and z <= 213.36:
        return (3.048/2)*(3.048/2)*math.pi
    else:
        return (0.131318/2)*(0.131318/2)*math.pi
for time in range(0,999):
    m = m - (dm(t[time], z)*dt)
    drag = 0.5 *airDensity * v * v *Cd(t[time], z)*area(t[time], z) / m
    if v < 0:
        drag = drag*-1
    v = v + (thrustProfile(t[time])/m - drag - g)*dt
    z = z + v*dt
    print("drag")
    print(drag)
    print("velocity")
    print(v)
    print("time")
    print(t[time])
    print("height")
    print(z)
    altitude.append(z)
    velocity.append(v)
    if z <0:
        break

plt.plot(t,altitude)




