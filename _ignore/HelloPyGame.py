import pygame

# import time
# import asyncio

# start = time.time()
#
#
# def tic():
#     return 'at %1.1f seconds' % (time.time() - start)
#
#
# async def gr1():
#     # Busy waits for a second, but we don't want to stick around...
#     await asyncio.sleep(5)
#
#
# async def gr2():
#     # Busy waits for a second, but we don't want to stick around...
#     await asyncio.sleep(5)
#
#
# async def gr3():
#     await asyncio.sleep(5)
#     print("creating")
#     tasks.append(ioloop.create_task(gr4()))
#
#
# async def gr4():
#     await asyncio.sleep(2)
#     print("Now I am here!")
#
#
# ioloop = asyncio.get_event_loop()
# tasks = [
#     ioloop.create_task(gr1()),
#     ioloop.create_task(gr2()),
#     ioloop.create_task(gr3())
# ]
# # ioloop.run_in_executor()
# ioloop.run_until_complete(asyncio.wait(tasks))
# ioloop.close()

from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg):
        print ("running")
        sleep(1)


if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (10, ))
    thread.start()
    thread.join()
    print ("thread finished...exiting")

def delta_time():
    """Get the current time in seconds since last frame"""
    return (pygame.time.get_ticks() - getTicksLastFrame) / 1000.0

def get_fps():
    global t
    global fps_count
    global fps
    t += delta_time()
    fps_count += 1
    if(t > 1):
        fps = fps_count
        fps_count = 0.0
        t-=1
    return (fps)

white = (255, 255, 255) # defining colors as tuples:
black = (0, 0, 0)
red = (255, 0, 0)


"""Start"""
pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))  # that will return a surface
pygame.display.set_caption('Slither')
gameExit = False
velocity = 1000.0
transform_position_x = 300
transform_position_y = 300
gameDisplay.fill(black)  # change background color
getTicksLastFrame = pygame.time.get_ticks()
# gameDisplay.fill(red, [3, 4, 3, 3])

clock = pygame.time.Clock()

t = 0.0
fps = 0.0
fps_count = 0.0
"""-----"""

"""Update"""
while not gameExit:
    # for event in pygame.event.get():
    #     print(event)
    #     if(event.type == )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                transform_position_x -= velocity * delta_time() # must be a float
            if event.key == pygame.K_RIGHT:
                transform_position_x += velocity * delta_time()

    coordinates = [int(transform_position_x), int(transform_position_y), 100, 200]      # [x,y, width, height] top left conner
    pygame.draw.rect(gameDisplay, white, coordinates)                                   # the screen coordinates starts on the top left conne  # to apply the changes

    pygame.draw.circle(gameDisplay,white,[50, 50], 50)

    s = pygame.Surface((800, 600))
    s.set_alpha(250)
    s.fill((0, 0, 0))
    gameDisplay.blit(s, (0, 0))
    pygame.display.update()
    # print(delta_time())
    # print(get_fps())
    # print(get_fps())
    # clock.tick(200)
    getTicksLastFrame = pygame.time.get_ticks()
"""-----"""
# Two functions that do exactly the same thing
pygame.display.flip()    # act like a flip book -> this will update the entire surface
pygame.display.update()  # Will update the specific part that you tell it to update

pygame.quit()
quit()
