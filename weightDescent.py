def weightDescent(vertDisplacement, massWithoutMotors, massPayload, parachuteDeploymentAltitude):
    if vertDisplacement > parachuteDeploymentAltitude:
        return massWithoutMotors *9.8
    else:
        return((massWithoutMotors-massPayload)* 9.8)