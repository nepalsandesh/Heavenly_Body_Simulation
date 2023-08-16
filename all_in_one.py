import numpy as np
import pygame
pygame.init()
from physics_engine import PhysicsEngine
from rotation_3d import get_projected_points
from ui_components import *

def rotate_y(theta):
    return np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [np.sin(theta), 0, np.cos(theta)]
    ])
    

def get_window_coordinates(point_array):
    """point array : [x, y, z]
        Returns [x+1920//2, y+1080//2, z]
    """
    if point_array.ndim == 1:
        point_array = [point_array[0] + 1920//2, point_array[1] + 1080//2, point_array[2]]
        return np.array(point_array)
    
    elif point_array.ndim == 2:
        x = point_array[:, 0] + 1920//2
        y = point_array[:, 1] + 1080//2
        z = point_array[:, 2]
        return np.array([x,y,z]).T


class Body:
    """Body Class"""
    def __init__(self, position, mass, color=np.random.randint(0, 255, 3), radius=10, TIME_DELAY=0.009):
        self.position = position
        self.mass = mass
        self.color = color
        self.radius = radius
        self.TIME_DELAY = TIME_DELAY
        self.velocity = np.zeros(3)
        self.force = np.zeros(3)
        self.position_history = np.array([self.position])
    
    def add_velocity(self, velocity_array):
        self.velocity += velocity_array
        
    def add_force(self, force_array):
        self.force += force_array
        
    def move(self):
        self.velocity = self.velocity + (self.force / self.mass) * self.TIME_DELAY
        self.position = self.position + self.velocity * self.TIME_DELAY
    
    def append_position(self, position):
        self.position_history = np.append(self.position_history, np.array([position]), axis=0)
        


class RenderEngine:
    """Engine Renderer Class
    """
    def __init__(self, bodies, save_image=False, display_logo=False):
        pygame.init()
        self.width, self.height = 1920, 1080
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.angle = 0.01 
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        
        self.distance = 4400
        self.scale = 2200
        
        self.rotate_x = False
        self.rotate_y = False
        self.rotate_z = False
        
        self.render_orbit = False       
        
        self.save_image = save_image
        self.frame_count = 0
        
        self.display_logo = display_logo
        self.logo = pygame.image.load("VORTEX_LAB_logo.png")
        self.logo = pygame.transform.rotozoom(self.logo, 0, 0.35)
        
        self.rotation_speed = 0.000
        self.bodies = bodies
        
    def check_events(self):
        """Input Events Handling Function"""
        [exit() for event in pygame.event.get() if event.type==pygame.QUIT]
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
            
        if keys[pygame.K_d]:
            self.distance += 22
        if keys[pygame.K_c]:
            self.distance -= 22
        if keys[pygame.K_s]:
            self.scale += 10
        if keys[pygame.K_x]:
            self.scale -= 10
        if keys[pygame.K_UP]:
            self.rotation_speed += 0.005
        if keys[pygame.K_DOWN]:
            self.rotation_speed -= 0.005
        
    # def rotate(self, angle):
    #     bodies_position = np.array([body.position for body in bodies])
    #     rotated_points = np.dot(rotate_y(angle), bodies_position.T)
    #     rotated_points = rotated_points.T
        
    #     for i, body in enumerate(bodies):
    #         window_coordinate = get_window_coordinates(rotated_points[i])
    #         if (window_coordinate[0] >= 0 and window_coordinate[0] <= 1920) and (window_coordinate[1] >= 0 and window_coordinate[1] <= 1080):
    #             pygame.draw.circle(self.screen, body.color, window_coordinate[:2], body.radius)
            
    #         orbit_points = body.position_history
    #         rotated_orbit_points = np.dot(rotate_y(angle), orbit_points.T)
    #         rotated_orbit_points = rotated_orbit_points.T
    #         rotated_orbit_points = get_window_coordinates(rotated_orbit_points)[:, :2]
            
    #         pygame.draw.lines(self.screen, body.color, False, rotated_orbit_points, 1)
    
    
    def rotate(self, angle):
        """Rotation Function"""
        bodies_position = np.array([body.position for body in self.bodies])
        # projected_points = get_projected_points(bodies_position, self.angle, self.distance, self.scale, rotate_y=True)
        projected_points = get_projected_points(
            points_3d=bodies_position,
            phi=angle,
            rotate_x=self.rotate_x,
            rotate_y=self.rotate_y,
            rotate_z=self.rotate_z,
            distance=self.distance,
            scale=self.scale            
        )
        
        
        for i, body in enumerate(self.bodies):
            point = projected_points[i]
            if (point[0] >= 0 and point[0] <= 1920) and (point[1] >= 0 and point[1] <= 1080):
                pygame.draw.circle(self.screen, body.color, point, body.radius)

                if self.render_orbit:
                    orbit_points = body.position_history
                    projected_orbit_points = get_projected_points(orbit_points, self.angle, self.distance,  self.scale,
                                                                  self.rotate_x, self.rotate_y,  self.rotate_z)
                    pygame.draw.lines(self.screen, body.color, False, projected_orbit_points, 1)

            
        self.angle += self.rotation_speed
        if angle >= 2* np.pi:
            angle = 0
    
    def update(self):
        net_force = engine.compute_force_vectors(bodies=self.bodies)
        for i, body in enumerate(self.bodies):
            body.force = net_force[i]
            body.move()
            body.append_position(body.position)
            

    def draw(self):
        # if not self.rotate_y:
        #     for i, body in enumerate(self.bodies):
        #         window_coordinate = get_window_coordinates(body.position)
                
        #         pygame.draw.circle(
        #             self.screen,
        #             body.color,
        #             window_coordinate[:2],
        #             body.radius
        #         )
        
        
        self.rotate(self.angle)
            
            
    def render_ui(self):
        panel.render(self.screen)
        distance_text_UI.render(self.screen, f"{self.distance}")
        scale_text_UI.render(self.screen, f"{self.scale}")
        rotate_text_UI.render(self.screen)
        
        if rotate_x_radiobutton.render(self.screen):
            self.rotate_x = True
        else:
            self.rotate_x = False

        if rotate_y_radiobutton.render(self.screen):
            self.rotate_y = True
        else:
            self.rotate_y = False
            
        if rotate_z_radiobutton.render(self.screen):
            self.rotate_z = True
        else:
            self.rotate_z = False
            
        if display_orbit_radiobutton.render(self.screen):
            self.render_orbit = True
        else:
            self.render_orbit = False
        
        if add_body_button.Draw(self.screen):
            mass = np.random.randint(5, 20) * 6e15
            self.bodies = np.append(self.bodies, 
                      Body(
                          position=np.random.randint(-500, 500, 3),
                          mass=mass,
                          color= np.random.randint(0, 256, 3),
                          radius= mass / 6e15
                      ))
            idx = self.bodies.size - 1
            self.bodies[idx].add_velocity(np.random.randint(-500, 500, 3))
            self.bodies = self.bodies[::-1]

        if distance_plus_button.is_double_clicked(self.screen):
            self.distance += 22
        if distance_minus_button.is_double_clicked(self.screen):
            self.distance -= 22

        if scale_plus_button.is_double_clicked(self.screen):
            self.scale += 22
        if scale_minus_button.is_double_clicked(self.screen):
            self.scale -= 22
            
    
    def run(self):
        while True:
            self.screen.fill((0,0,0))
            self.clock.tick(self.FPS)
            self.check_events()        
            self.update()
            self.draw()
            self.render_ui()
            bodies[-1].position = np.zeros(3)
            text = self.font.render("FPS: %f"%(self.clock.get_fps()), True, (255, 255, 255))
            # self.screen.blit(text, (1920//2, 20))
            
            if self.display_logo:
                self.screen.blit(self.logo, (1740, 1000))
            
            # image save
            if self.save_image:
                filename = "captures/observe/%08d.png" % (self.frame_count)
                pygame.image.save(self.screen, filename)
                self.frame_count += 1  
                
            # print("Distance: %g, Scale: %g, FPS: %g, Rotation_speed: %g"%(self.distance, self.scale, self.clock.get_fps(), self.rotation_speed))
        
            
            pygame.display.flip()
    



# ------------------------- Parameters ----------------------------
bodies = [Body(
    position=np.random.randint(-500, 500, 3),
    mass=np.random.randint(5, 20) * 6e15,
    color=np.random.randint(0, 256, 3)
) for i in range(1)]

bodies.append(Body(
    position=np.zeros(3),
    mass= 6e15 * 1000,
    radius=40,
    color=np.array([255, 255, 255])
))

for body in bodies:
    body.add_velocity(np.random.randint(-500, 500, 3))




# -------------------------- Run --------------------------------

if __name__ == "__main__":
    bodies = np.array(bodies, dtype=object)
    engine = PhysicsEngine()
    app = RenderEngine(bodies=bodies, save_image=False, display_logo=True)
    app.run()