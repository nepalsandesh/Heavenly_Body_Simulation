from body import Body
import numpy as np


# bodies list
body1 = Body(position=(960-400, 540-400, 0), mass=6e15,
             color=(255, 255, 255),
             radius=20)
body1.add_velocity(np.array([80, 0, 0]))

body2 = Body(position=(960+400, 540+400, 0), mass=6e15,
             color=(255, 100, 100),
             radius=20)
body2.add_velocity(np.array([-80, 0, 0]))

body3 = Body(position=(0, 0, 0), mass= 80 * 6e15,
             color=(52, 210, 235),
             radius=40)
body3.add_velocity(np.array([0, 0, 0]))

body4 = Body(position=(960-400, 540+400, 0), mass=6e15,
             color=(100, 100, 255),
             radius=20)
body4.add_velocity(np.array([0, -80, 0]))

body5 = Body(position=(960+400, 540-400, 0), mass=6e15,
             color=(100, 100, 255),
             radius=20)
body5.add_velocity(np.array([0, 80, 0]))


# body6 = Body(position=np.random.randint(0,1500, 3), mass=6e15,
#              color=(255, 255, 255),
#              radius=20)
# body6.add_velocity(np.array([0, 40, 0]))

# body7 = Body(position=np.random.randint(0,1500, 3), mass=6e15,
#              color=(255, 100, 100),
#              radius=20)
# body7.add_velocity(np.array([40, 40, 0]))

# body8 = Body(position=np.random.randint(0,1500, 3), mass=6e15,
#              color=(255, 100, 100),
#              radius=20)
# body8.add_velocity(np.array([40, 0, 0]))


bodies = [body1, body2, body3, body4, body5]
# bodies = [body1, body2, body3, body4, body5, body6, body7, body8]




# ------------ Generation of multiple bodies ---------------
bodies = [
    Body(
        position=[np.random.randint(-500, 500), np.random.randint(-500, 500), np.random.randint(-500, 500)],
        mass=  np.random.randint(5, 30) * 6e15,
        # mass=  5 * 6e15,
        color=np.random.randint(0,255,3),
        radius = 20
    ) for i in range(8)
]
bodies.append(body3)




for i in bodies:
    i.add_velocity([np.random.randint(-5000, 5000), np.random.randint(-5000, 5000), 0])
    i.save_positions = True
    i.radius = (i.mass / 6e15) * (1/2)
    

    
bodies[-1].radius = 40
bodies[-1].mass = 6e15 * 100000
# bodies = np.array(bodies, dtype=object)