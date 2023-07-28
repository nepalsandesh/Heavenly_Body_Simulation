import numpy as np
import pygame


class Body:
    """Heavenly body class.
    """
    def __init__(self,  position, mass, color, radius=17):
        self.position = position
        self.mass = mass
        self.color = color
        self.radius = radius
        
    def draw(self):
        pass
    
    def add_velocity(self):
        pass
    
    def add_force(self):
        pass
    
    def move(self):
        pass