import random

import pygame
from pygame.math import Vector2

import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

def run():
    core.cleanScreen()


core.main(setup, run)