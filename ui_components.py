import pygame
from ui import RenderText, Button, Panel

panel = Panel((20, 20), 300, 400, (55, 55, 100), 80)

# button to append body in bodies 
add_body_button = Button(
    x=panel.position[0] + 20,
    y=panel.position[1] + 20,
    w=100, h=30, text="Add Body",
   
)
