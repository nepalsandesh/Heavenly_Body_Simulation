from body import Body


# bodies list
body1 = Body(position=(1920//2, 1080//2, 0), mass=10,
             color=(255, 255, 255),
             radius=20)

body2 = Body(position=(1920//3, 1080//2, 0), mass=10,
             color=(255, 100, 100),
             radius=20)

body3 = Body(position=(1920//2, 1080//3, 0), mass=10,
             color=(100, 255, 100),
             radius=20)

body4 = Body(position=(1920//3, 1080//3, 0), mass=10,
             color=(100, 100, 255),
             radius=20)


bodies = [body1, body2, body3, body4]