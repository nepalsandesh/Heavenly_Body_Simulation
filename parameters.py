from body import Body


# bodies list
body1 = Body(position=(500, 300, 0), mass=6e15,
             color=(255, 255, 255),
             radius=20)

body2 = Body(position=(600, 200, 0), mass=6e15,
             color=(255, 100, 100),
             radius=20)

body3 = Body(position=(300, 500, 0), mass=6e15,
             color=(100, 255, 100),
             radius=20)

body4 = Body(position=(1920//3, 1080//3, 0), mass=6e15,
             color=(100, 100, 255),
             radius=20)


bodies = [body1, body2, body3, body4]