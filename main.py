import pygame
import numpy as np
from physics_engine import PhysicsEngine
from parameters import (
    bodies
)
from rotation import rotate_x, rotate_y, rotate_z

from physics_engine_cython import compute_force_vectors_cython  # Import the Cython version




class Window:
    """Window rendering class"""
    def __init__(self, save_image=False):
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.RUNNING = True
        
        self.rotate_x = False
        self.rotate_y = False
        self.rotate_z = False
        
        self.frame_count = 0
        self.save_image = save_image
        
        self.show_axis = True
        
        self.logo = pygame.image.load("VORTEX_LAB_logo.png")
        self.logo = pygame.transform.rotozoom(self.logo, 0, 0.53)
        
    def handle_events(self):
        """function for handling input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.RUNNING = False
                    
                if event.key == pygame.K_SPACE:
                    self.show_axis = not self.show_axis
                    
            
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_x]:
            for body in bodies:
                body.position = rotate_x(body.position, 0.02)
        if keys[pygame.K_y]:
            for body in bodies:
                body.position = rotate_y(body.position, 0.02)
        if keys[pygame.K_z]:
            for body in bodies:
                body.position = rotate_z(body.position, 0.02)

                
                    
    def run(self):
        """Main-loop function"""
        while self.RUNNING:
            self.clock.tick(self.FPS)
            self.screen.fill((0, 0, 0))
            
            net_force = engine.compute_force_vectors(bodies=bodies)
            # print("Net Force :\n", net_force)
            # net_force = compute_force_vectors_cython(bodies)
            for i, body in enumerate(bodies):
                body.force = net_force[i]
            
            if self.show_axis:
                for body in bodies:               
                    if (body.position[0] >= -500 and body.position[0] <= 1920+500) and (body.position[1] >= -500 and body.position[1] <= 1080+500):
                        body.draw_lines(self.screen, (body.color[0]/1.6, body.color[1]/1.6, body.color[2]/1.6))
                        pass
                
            for body in bodies:
                body.draw(self.screen)  
                body.move()
                
            # keep heaviest body stable
            bodies[-1].velocity = [0,0,0] 
            # print("Position history of a first body : \n", bodies[i].position_history)
            
            # render logo
            self.screen.blit(self.logo, (1680, 980))
            
            
            # image save
            if self.save_image:
                filename = "captures/observe/%08d.png" % (self.frame_count)
                pygame.image.save(self.screen, filename)
                self.frame_count += 1
            
            
            self.handle_events()
            pygame.display.flip()
            
            
            
if __name__ == "__main__":
    app = Window(save_image=True)
    engine = PhysicsEngine()
    app.run()
