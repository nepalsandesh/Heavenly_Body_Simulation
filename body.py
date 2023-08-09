import numpy as np
import pygame

TIME_DELAY=0.0006

class Body:
    """Heavenly body class.
    """
    def __init__(self,  position, mass, color, radius=17, save_positions=False):
        self.position = position
        self.mass = mass
        self.color = color
        self.radius = radius
        self.save_positions = save_positions
        
        self.velocity = np.array([0, 0, 0])
        self.force = np.array([0, 0, 0])
        self.position_history = []
        
        
    def draw(self, screen):
        if (self.position[0] >= 0 and self.position[0] <= 1920) and (self.position[1] >= 0 and self.position[1] <= 1080):
            pygame.draw.circle(screen, self.color, (self.position[0], self.position[1]), self.radius)
        
        if self.save_positions == True:
            self.position_history.append((self.position[0], self.position[1]))
            
    def draw_lines(self, screen, color):
        if len(self.position_history) >= 2:
            pygame.draw.lines(screen, color, False, self.position_history, 2)
    
    def add_velocity(self, velocity_array):
        self.velocity = self.velocity + velocity_array
    
    def add_force(self, force_array):
        self.force = self.force + force_array
    
    def move(self):
        self.velocity = self.velocity + (self.force / self.mass) * TIME_DELAY
        self.position = self.position + self.velocity * TIME_DELAY