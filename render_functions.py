import pygame.draw
import util

from values import map_colours
def do_background(screen, world, world_x, world_y, camera_x, camera_y, camera_w, camera_h):

    for x1 in range(0, camera_w):
        for y1 in range(0, camera_h):
            # blit background
            pygame.draw.rect(screen, map_colours[world[world_x + x1, world_y + y1]], pygame.Rect(util.to_pixel(camera_x + x1) , util.to_pixel(camera_y + y1), 15, 15))
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(util.to_pixel(camera_x + int(camera_w/2)), util.to_pixel(camera_y + int(camera_h/2)), 15, 15))
            #print("X1: ",x1, " Y1: ", y1, " COLOUR: ", world[x1, y1])
    return