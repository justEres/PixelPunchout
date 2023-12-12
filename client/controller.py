import pygame
import pygame.joystick as joy

ps4keys = {
    "x": 0,
    "circle": 1,
    "square": 2,
    "triangle": 3,
    "share": 4,
    "PS": 5,
    "options": 6,
    "left_stick_click": 7,
    "right_stick_click": 8,
    "L1": 9,
    "R1": 10,
    "up_arrow": 11,
    "down_arrow": 12,
    "left_arrow": 13,
    "right_arrow": 14,
    "touchpad": 15
}
LEFT, RIGHT, UP, DOWN = False, False, False, False

joy.init()
analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}
joysticks = []
jcount = joy.get_count()
print("joystick count = " + str(joy.get_count()))
for i in range(joy.get_count()):
    joysticks.append(joy.Joystick(i))

for j in joysticks:
    j.init()

def getVec(event):
    if event.type == pygame.JOYAXISMOTION:
        analog_keys[event.axis] = event.value
        return pygame.Vector2(analog_keys[0], analog_keys[1])
    else:
        return pygame.Vector2(0,0)
