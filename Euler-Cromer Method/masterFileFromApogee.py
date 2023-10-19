from thrustProfile import thrustProfile
import numpy as np
import matplotlib.pyplot as plt
import math
G = 6.674e-11
M_earth = 5.972e24
airDensity = 1.293 #kg/m^3
dt = 0.1

v = 0
z = 1281.316672 #change altitude
m = 15.2237
tmax = 100
g=9.8
windSpeed = 20 * 0.447 #Change windspeed mph to meters/second
altitude = [1281.316672] #change altitude
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
    m = m - (dm(t[time], z))
    parachuteDeploymentCounter = 0
    if z<=213.36 and parachuteDeploymentCounter == 0:
        v = -2.45
        parachuteDeploymentCounter = parachuteDeploymentCounter +1

    drag = 0.5 *airDensity * v * v *Cd(t[time], z)*area(t[time], z) / m
    

    v = v + (-drag - g)*dt
    z = z + v*dt
    
    altitude.append(z)
    velocity.append(v)
    if z <0:
        break
fig, axs = plt.subplots(2)
fig.suptitle('20 mph, 10 degrees')
axs[0].plot(t[0:(len(altitude)-1-1000)],altitude) #diagnostics for plot with altitude and time
axs[0].set(xlabel = 'Time (Seconds)', ylabel = 'Altitude (Meters)')

x=[0]
for time in range(0,len(altitude)-1):
    x.append(windSpeed*t[time])
print(len(altitude)-1)
print(x[-1])
axs[1].plot(x, altitude)
axs[1].set(xlabel = 'Horizontal Drift (meters)', ylabel = 'Altitude (Meters)')
plt.show()
