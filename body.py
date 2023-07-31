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
        
        self.velocity = np.array([0, 0, 0])
        self.force = np.array([0, 0, 0])
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position[0], self.position[1]), self.radius)
    
    def add_velocity(self):
        pass
    
    def add_force(self):
        pass
    
    def move(self):
        pass