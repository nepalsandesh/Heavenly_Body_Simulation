import pygame
import numpy as np
from parameters import (
    bodies
)


class Window:
    """Window rendering class"""
    def __init__(self):
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.RUNNING = True
        
    def handle_events(self):
        """function for handling input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.RUNNING = False
                    
    def run(self):
        """Main-loop function"""
        while self.RUNNING:
            self.clock.tick(self.FPS)
            self.screen.fill((0, 0, 0))
            
            for body in bodies:
                body.draw(self.screen)
            
            self.handle_events()
            pygame.display.flip()
            
            
            
if __name__ == "__main__":
    app = Window()
    app.run()
