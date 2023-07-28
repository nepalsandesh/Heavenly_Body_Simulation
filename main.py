import pygame
import numpy as np


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.RUNNING = False
                    
    def render(self):
        pass
        
    def run(self):
        while self.RUNNING:
            self.clock.tick(self.FPS)
            self.screen.fill((55, 55, 200))
            
            self.render()
            
            self.handle_events()
            pygame.display.flip()
            
            
            
if __name__ == "__main__":
    app = Window()
    app.run()
