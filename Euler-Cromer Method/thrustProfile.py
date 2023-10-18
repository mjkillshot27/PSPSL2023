def thrustProfile(time):
    if time < 0.0465839:
        return -2664.869*time + 1365.520
    elif time < .48913:
        return 701.260*time + 1208.713
    elif time< 1.01708:
        return 32.674*time + 1535.738
    elif time< 1.99534:
        return 35.246*time + 1533.123
    elif time< 2.3913:
        return -43.540*time + 1690.327
    elif time <2.48447:
        return 1850.488*time - 2838.863
    elif time <2.50776:
        return -71067.926*time + 178324.750
    elif time <2.6:
        return -1121.509*time + 2915.924
    else:
        return 0