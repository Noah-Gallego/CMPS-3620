# Compass
from microbit import *

# Calibrate The Compass
compass.calibrate()

# Get Direction
def get_direction(deg):
    """
    Input:
        bearing (int) - a degree
    Output:
        direction (str) - N, E, S, W
    """

    dir = None
    
    if deg >= 315 or deg < 45:
        dir = 'N'
    elif deg >= 45 and deg < 135:
        dir = 'E'
    elif deg >= 135 and deg < 225:
        dir = 'S'
    elif deg >= 225 and deg < 315:
        dir = 'W'

    return dir

# Start on A press
while True:     
    if button_a.was_pressed():
        if compass.is_calibrated():
            # Send to microbit
            dir = get_direction(compass.heading())
            
            display.show(str(dir))
    

        