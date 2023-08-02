from body import Body
import numpy as np


# bodies list
body1 = Body(position=(500, 300, 0), mass=6e15,
             color=(255, 255, 255),
             radius=20)
body1.add_velocity(np.array([40, 0, 0]))

body2 = Body(position=(600, 200, 0), mass=6e15,
             color=(255, 100, 100),
             radius=20)
body2.add_velocity(np.array([-40, 0, 0]))

body3 = Body(position=(300, 500, 0), mass=10 *6e15,
             color=(100, 255, 100),
             radius=50)

body4 = Body(position=(1920//3, 1080//3, 0), mass=6e15,
             color=(100, 100, 255),
             radius=20)
body3.add_velocity(np.array([50, 0, 0]))



bodies = [body1, body2, body3, body4]