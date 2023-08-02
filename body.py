import numpy as np
import pygame

TIME_DELAY = 0.0005

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
    
    def add_velocity(self, velocity_array):
        self.velocity = self.velocity + velocity_array
    
    def add_force(self, force_array):
        self.force = self.force + force_array
    
    def move(self):
        self.velocity = self.velocity + (self.force / self.mass) * TIME_DELAY
        self.position = self.position + self.velocity * TIME_DELAY