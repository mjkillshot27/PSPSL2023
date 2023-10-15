def airDensity(altitude,initT,initP):
    '''this function is valid only for the troposphere (18-20km)
    Input(s): altitude in meters
            initT (reference temperature) in K
            initP (reference static pressure) in Pa
    Output(s): density in meters cubed per kilogram'''
    TLapseRate = 6.5/1000 #Degrees Kelvin per meter
    mm = 0.0289664 #kg/mol
    R = 8.3145 #J/(molK)
        
    g = 9.8 #m/s^2
    temperature = initT - TLapseRate*altitude
    pressure = initP*pow((1-(TLapseRate*altitude)/(initT)),((g*mm)/(R*TLapseRate)))
    density = (pressure*mm)/(R*temperature)
    print(temperature)
    return density