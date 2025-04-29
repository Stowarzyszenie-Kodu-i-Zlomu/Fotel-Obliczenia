import pygame as pg
import sys
import time as t

# Config
axis_metric = 30
dead_zone = 0.1 * axis_metric
acceleration = 3
max_distance = axis_metric

# Initalize Pygame
pg.init()
pg.joystick.init()

if pg.joystick.get_count() == 0:
    print("No Joystick found")
    sys.exit()

joystick = pg.joystick.Joystick(0)
joystick.init()

# Dictionary to store value of start of the movement for each axis
start_time = {
    'leftX': None,
    'leftY': None,
    'rightX': None,
    'rightY': None
}


def calculate_axis_pos(axis_value, axis_name):
    """A function that calculates current position of an axis with acceleration"""
    global start_time

    # If in dead zone, reset time
    if abs(axis_value) < dead_zone / axis_metric:
        start_time[axis_name] = None
        return 0

    # If is outside dead zone, assign current time to axis
    if start_time[axis_name] is None:
        start_time[axis_name] = t.time()

    time_passed = t.time() - start_time[axis_name]
    distance = 0.5 * acceleration * (time_passed ** 2)  # Wzór na ruch jednostajnie przyspieszony

    # Make sure that distance is not higher than max distance
    distance = min(distance, max_distance)

    return axis_value * distance


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

    # Get joystick axis
    leftX = calculate_axis_pos(joystick.get_axis(0), 'leftX')
    leftY = calculate_axis_pos(-joystick.get_axis(1), 'leftY')  # Invert Y

    rightX = calculate_axis_pos(joystick.get_axis(3), 'rightX')
    rightY = calculate_axis_pos(-joystick.get_axis(4), 'rightY')  # Invert Y

    if abs(leftX) > dead_zone or abs(leftY) > dead_zone:
        print(f"Lewa gałka: X: {round(leftX, 2)} Y: {round(leftY, 2)}")

    if abs(rightX) > dead_zone or abs(rightY) > dead_zone:
        print(f"Prawa gałka: X: {round(rightX, 2)} Y: {round(rightY, 2)}")