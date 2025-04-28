import pygame as pg
import sys
from pygame import joystick

pg.init()
pg.joystick.init()
joysticks = joystick.Joystick(0)
DEAD_ZONE = 0.1

while True:
    for event in pg.event.get():

        leftX = joysticks.get_axis(0)
        leftY = joysticks.get_axis(1)

        rightX = joysticks.get_axis(3)
        rightY = joysticks.get_axis(4)

        if abs(leftY) > DEAD_ZONE or abs(leftX) > DEAD_ZONE:
            print("Lewa gałka: ", "X: ", leftX, "Y: ", leftY * -1)

        if abs(rightX) > DEAD_ZONE or abs(rightY) > DEAD_ZONE:
            print("Prawa gałka: ", "X: ", rightX, "Y: ", rightY * -1)
