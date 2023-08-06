import pygame
import numpy as np
from physics_engine import PhysicsEngine
from parameters import (
    bodies
)

from physics_engine_cython import compute_force_vectors_cython  # Import the Cython version



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
            
            net_force = engine.compute_force_vectors()
            # net_force = compute_force_vectors_cython(bodies)
            for i, body in enumerate(bodies):
                body.force = net_force[i]
            
            for body in bodies:
                body.draw(self.screen)
                
                if (body.position[0] >= 0 and body.position[0] <= 1920) and (body.position[1] >= 0 and body.position[1] <= 1080):
                    body.draw_lines(self.screen, body.color)
                
            for body in bodies:
                body.move()
                
            # keep heaviest body stable
            bodies[-1].velocity = [0,0,0]
            
            self.handle_events()
            pygame.display.flip()
            
            
            
if __name__ == "__main__":
    app = Window()
    engine = PhysicsEngine(bodies)
    app.run()
