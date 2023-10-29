import matplotlib.pyplot as plt

#Plots vertical position, vertical velocity, and vertical acceleration
def trajectory_plots(time, vert_pos, vert_veloc, vert_acc):
    
    #Plotting vertical trajectory and format
    plt.plot(time, vert_pos)
    plt.title("Vertical Trajectory vs. Time")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Vertical Position (Feet)")
    plt.grid()
    plt.show()
    
    #Plotting vertical velocity and format
    plt.plot(time, vert_veloc)
    plt.title("Vertical Velocity vs. Time")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Vertical Velocity (Feet/Seconds)")
    plt.grid()
    plt.show()
    
    #Plotting the vertical acceleration and format
    plt.plot(time, vert_acc)
    plt.title("Vertical Acceleration vs. Time")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Vertical Acceleration (Feet/Seconds$^2$)")
    plt.grid()
    plt.show()
    
    
def horizontal_plots(time, horiz_pos, horiz_vel, vert_pos):
    
    #Plotting horizaontal trajectory vs time
    plt.plot(time, horiz_pos)
    plt.title("Horizontal Position vs. Time")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Horizontal Position (Feet)")
    plt.grid()
    plt.show()
    
    #Plotting horizontal velocity vs time
    plt.plot(time, horiz_vel)
    plt.title("Horizontal Velocity vs. Time")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Horizontal Velocity (Feet/Seconds)")
    plt.grid()
    plt.show()
    
    #Plotting trajecgory
    plt.plot(horiz_pos, vert_pos)
    plt.title("Trajectory of Launch Vehicle")
    plt.xlabel("Horizontal Posiition (Feet)")
    plt.ylabel("Vertical Position (Feet)")
    plt.grid()
    plt.show()
