def dragTop(verticalVelocity, dragTop):
    if(verticalVelocity > 0):
        return dragTop.abs()
    else:
        return dragTop.abs()*-1
        