import numpy as np

def galilean_transformation(s,v,t):
    moving_frame_position = v * t
    gamma = 1
    x = moving_frame_position[0]
    y = moving_frame_position[1]
    z = moving_frame_position[2]

    new_position = np.array([
        s[0] - x,
        s[1] - y,
        s[2] - z
    ])

    new_position_list = []
    for i in new_position:
        new_position_list.append(i)

    return new_position_list


def lorentz_transformation(s,v,t):
    moving_frame_position = v * t
    c = 3 * (10 ** 8)
    x = moving_frame_position[0]
    y = moving_frame_position[1]
    z = moving_frame_position[2]

    beta = v/c
    gamma = 1/np.sqrt(1 - (beta**2))

    new_position = np.array([
        gamma[0] * (s[0] - x),
        gamma[1] * (s[1] - y),
        gamma[2] * (s[2] - z)
    ])

    new_position_list = []
    for i in new_position:
        new_position_list.append(i)
    return new_position_list

def rotation_transformation(vector, angle, constant_axis):

    cosθ = np.cos(angle)
    sinθ = np.sin(angle)

    if constant_axis == "x":        #constant axis is the parameter which is the axis of rotation of the frame

        new_position = np.array([
            vector[0],
            (vector[1] * cosθ) - (vector[2] * sinθ),
            (vector[1] * sinθ) - (vector[2] * cosθ)
        ])

    elif constant_axis == "y":

        new_position = np.array([
            (vector[0] * cosθ) + (vector[2] * sinθ),
            vector[1],
            (vector[2] * cosθ) - (vector[0] * sinθ)
        ])

    elif constant_axis == "z":

        new_position = np.array([
            (vector[0] * cosθ) - (vector[1] * sinθ),
            (vector[0] * sinθ) + (vector[1] * cosθ),
            vector[2]
        ]) 

    new_position_list = []
    for i in new_position:
        new_position_list.append(i)

    return new_position_list

s = [2,3,4]
v = np.array([1,2,3])
t = 0.5

print(galilean_transformation(s,v,t))

s_lorentz = [2,3,4]
relativistic_velocity = np.array([10**5,10**4,10**7])
t_lorentz = 2

print(lorentz_transformation(s_lorentz,relativistic_velocity,t_lorentz))

vector = [2,3,4]
angle = 100
axis_of_rotation = "x"

print(rotation_transformation(vector,angle=100,constant_axis= axis_of_rotation))






