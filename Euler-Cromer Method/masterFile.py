#Make it all into imperial
#Add so everything can be inputs
from thrustProfile import thrustProfile
import numpy as np
import matplotlib.pyplot as plt
import math
G = 6.674e-11 #Nm^2/kg^2
M_earth = 5.972e24 #kg
airDensity = 1.293 #kg/m^3
dt = 0.1 #Seconds
z0 = 0
v0 = 0
v = v0
z = z0
V = v
Z = z
x = 0 #lateral position, m
vx = 0 #lateral velocity, m/s
windspeed = 4.47 #m/s
m = 17.423 #initial mass in kgs 
M = m
theta = (7.5) * math.pi / 180 #initial launch angle || degs -> rads
main_deploy_alt = 213.36 #initial main parachute deployment altitude (m)
main_full_alt = main_deploy_alt - (100/3.281) #main parachute final deployment altitude (m)
main_full_area_top = (3.048/2) ** 2 * math.pi #Final area of main parachute top (m^2)
main_deploy_area_top = (0.131318/2) ** 2 * math.pi #Initital area of main parachute top (m^2), potentially change variable name
main_full_area_side = main_full_area_top / 2
main_deploy_side  = 1 #initial length of parachute
tmax = 100 #Seconds
Cd = 0.3
Cd_side = 0.75
g=9.81 #m/(s*s)
altitude = [0]
velocity = [0]
lat_vel = [0]
lat_pos = [0]

#Calculates side drag based on various drag coefficients
def side_drag(par_area, rocket_area, par_cd, rocket_cd, speed, time, theta):
    dir_rocket_area = math.sin(theta) * rocket_area
    rocket_drag = dir_rocket_area * speed ** 2 * rocket_cd
    par_drag = par_area * par_cd * speed ** 2
    total_drag = par_drag + rocket_drag
    return(total_drag)

#Calculates change in mass
def dm (time, z):
    if time<2.6:
        return (3.54369/2.6)
    elif time>50 and z == 500:
        return 3.40194
    else:
        return 0
#Take a look at open rocket
def Cd(time, z):
    if time> 10 and z <= 213.36:
        return 1.2#1.2
    else:
        return 0.5#0.453

def Cd_side(time, z):
    if time > 101 and z <= 213.36:
        return 0
    else: 
        return 0
t = np.linspace(0,tmax,1001)


def side_area(z, v, main_deploy_alt, main_full_alt):
    #k is a logarthmic curve
    k = (1 / (main_full_alt - main_deploy_alt)) * math.log(main_full_area_side, main_deploy_side)
    
    C = main_deploy_side * -k ** main_deploy_alt
    
    #Occurs if between full altitude and deploy altitude
    if z <= main_deploy_alt and z >= main_full_alt and v < 0:
        #Makes logarthmic curve
        AMS = C * k ** z
        
    #Below main full alt and if the rocket is going down
    elif z < main_full_alt and v < 0:
        AMS = main_full_area_side
    else:
    #Just drag from the rocket
        AMS = main_deploy_side
    return AMS

#Look at this for time
def area(time, z):
    k = (1 / (main_full_alt - main_deploy_alt)) * math.log(main_full_area_top, main_deploy_area_top)
    C = main_deploy_area_top * -k ** main_deploy_alt
    if z <= main_deploy_alt and z >= main_full_alt and v < 0:
        AMT = C * k ** z
    elif z < main_full_alt and v < 0:
        AMT = main_full_area_top
    else:
        AMT = main_deploy_area_top
    return AMT

parachuteDeploymentCounter = 0
for time in range(1,999):
    #Mass based on loss propellant and then eventually the lost payload
    m = m - (dm(t[time], z)*dt)
    
    if z<=213.36  and time>200 and parachuteDeploymentCounter == 0:
        v = -3
        parachuteDeploymentCounter = parachuteDeploymentCounter +1
    #Add side drag from side are
    drag = 0.5 *airDensity * v * v *Cd(t[time], z)*area(t[time], z) / m 
    if v < 0:
        drag = drag*-1
    v = v + ((thrustProfile(t[time])/m ) * math.cos(theta) - drag - g)  * dt
    vx = vx + (thrustProfile(t[time])/m * math.sin(theta)) * dt
    if(z*3.281> 5000):
        vx=0
    z = z + v * dt
    x = x + (vx - windspeed) * dt
    print("velocityx")
    print(vx)
    """
    print("area")
    print(area(t[time], z))
    print("velocity")
    print(v)
    print("thrust")
    print(thrustProfile(t[time]))

    print("time")
    print(t[time])
    print("height")
    print(z)"""
    
    altitude.append(z*3.281)
    velocity.append(v*3.281)
    lat_vel.append(vx * 3.281)
    lat_pos.append(x * 3.281)
    if z <0:
        break
altitude.append(1)

#plt.plot(range(len(altitude)),altitude)
print(lat_pos)
plt.plot(np.arange(0, len(altitude)/10, 0.1), altitude)
plt.show()

plt.plot((np.arange(0, len(lat_pos)))/10, lat_pos)
plt.title
plt.show()