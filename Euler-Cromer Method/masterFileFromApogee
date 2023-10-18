from thrustProfile import thrustProfile
import numpy as np
import matplotlib.pyplot as plt
import math
G = 6.674e-11
M_earth = 5.972e24
airDensity = 1.293 #kg/m^3
dt = 0.1
z0 = 1475.537
v0 = 0
v = v0
z = z0
V = v
Z = z
m = 15.2237
M = m
tmax = 100
Cd = 0.3
g=9.8
windSpeed = 5 * 0.447 #mph to meters/second
altitude = [1475.537]
velocity = [0]
def dm (time, z):
    counter = 0
    if z <= 152.4 and counter==0:
        counter= counter +1
        return 3.40194
    else:
        return 0
    
def Cd(time, z):
    if z <= 213.36:
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
    #m = m - (dm(t[time], z)*dt)
    parachuteDeploymentCounter = 0
    if z<=213.36 and parachuteDeploymentCounter == 0:
        v = -2.52628
        parachuteDeploymentCounter = parachuteDeploymentCounter +1

    drag = 0.5 *airDensity * v * v *Cd(t[time], z)*area(t[time], z) / m
    
    if v < 0:
        drag = drag*-1
    v = v + (- drag - g)*dt
    z = z + v*dt
    print("height")
    print(z)
    print("drag")
    print(drag)
    print("height")
    print(z)
    print("velocity")
    print(v)
    altitude.append(z)
    velocity.append(v)
    if z <0:
        break
#plt.plot(t[0:(len(altitude)-1-1000)],altitude) diagnostics for plot with altitude and time
#plt.show()
x=[0]
for time in range(0,len(altitude)-1):
    x.append(windSpeed*t[time])
print(len(altitude))
plt.plot(x, altitude)
plt.show()
