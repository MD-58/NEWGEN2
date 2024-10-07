import pygame
from world_generation import generate_world
import time
import util
from input_handlers import handle_keys
from render_functions import do_background

pygame.init()

BLACK = (0, 0, 0)

def main():
    screen_height = 80
    screen_width = 50
    camera_width = 80
    camera_height = 30
    is_fullscreen = False

    size = (util.to_pixel(screen_width), util.to_pixel(screen_width))
    window = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("New_World")
    camera_x = 0
    camera_y = 0
    world_x = 0
    world_y = 0

    print("here we go again")
    start = time.time()
    world = generate_world(128, 128, 16, 8, 0)
    end = time.time()
    print("BYTES: ", world.size * world.itemsize)
    print("TIME TAKEN: ", end - start)

    running = True
    while running:
        for event in pygame.event.get():
            action = handle_keys(event)
            if action.get("exit"):
                running = False
            elif action.get("fullscreen"):
                is_fullscreen = not is_fullscreen
                flags = pygame.FULLSCREEN if is_fullscreen else 0
                window = pygame.display.set_mode(size, flags)
            elif "move" in action:
                move_x, move_y = action["move"]
                #print(move_x)
                world_x = world_x + move_x
                world_y = world_y + move_y
        #print("X: ", camera_x, " Y: ", camera_y)
        window.fill(BLACK)
        do_background(window, world, world_x, world_y, camera_x, camera_y, camera_width, camera_height)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()