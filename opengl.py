import pygame
from pygame.locals import *

import shaders
from gl import Renderer

# intervalo de tiempo
deltaTime = 0.0

# inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)
r.createObjects()

cam_x = 0
cam_z = 3
rotate_x = 0
rotate_y = 0

is_playing = True
while is_playing:

    # revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        cam_x -= 2 * deltaTime
    if keys[pygame.K_d]:
        cam_x += 2 * deltaTime
    if keys[pygame.K_w]:
        cam_z -= 2 * deltaTime
    if keys[pygame.K_s]:
        cam_z += 2 * deltaTime
    if keys[pygame.K_RIGHT]:
        rotate_x -= 60 * deltaTime
    if keys[pygame.K_LEFT]:
        rotate_x += 60 * deltaTime
    if keys[pygame.K_UP]:
        rotate_y += 60 * deltaTime
    if keys[pygame.K_DOWN]:
        rotate_y -= 60 * deltaTime

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            is_playing = False
        elif ev.type == pygame.KEYDOWN:
            # revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode
            elif ev.key == pygame.K_ESCAPE:
                is_playing = False

    # traslación de cámara en el eje x
    r.translate_cam(cam_x, 0, cam_z)

    # rotación de la cámara
    r.rotate_cam(rotate_x, rotate_y, 0)

    # renderer loop
    r.render()

    # fps
    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
