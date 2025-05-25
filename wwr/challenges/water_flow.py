


def water_column_height(tower_height, tank_height):
    h = tower_height + ((tank_height*3)/4)
    return h
def pressure_gain_from_water_height(height):
    P = (998.2*9.80665*height)/1000
    return P
def pressure_loss_from_piper(pipe_diameter,pipe_length,friction_factor,fluid_velocity):
    P = (-1*friction_factor*pipe_length*998.2*fluid_velocity**2)/(2000*pipe_diameter)
    return P

