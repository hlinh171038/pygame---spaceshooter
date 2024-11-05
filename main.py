import pygame
# upgrade system help you find the path of image
import os

WIDTH, HEIGHT = 900, 500 # CONTANT
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # create frame with WIDTH and HEIGHT
WHITE = (255,255,255)
# 3 .fps
FPS = 60
VEL = 3
# 5 sacle up
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
# 4. create character
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

#scale for character red
# 6 rotate
RED_SPACESHIP =pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90) 

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
#scale for character yellow
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
# 1.change caption 
pygame.display.set_caption("first game !")

def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    pygame.display.update() 
    
def red_handle_movement(key_press,red):
    if(key_press[pygame.K_a]) : # LEFT 
        red.x -= VEL
    if(key_press[pygame.K_d]) : # RIGHT
        red.x += VEL
    if(key_press[pygame.K_w]) : # UP
        red.y -= VEL
    if(key_press[pygame.K_s]) : # DOWN
        red.y += VEL

def yellow_handle_movement(key_press,yellow):
    if(key_press[pygame.K_LEFT]) : # LEFT 
        yellow.x -= VEL
    if(key_press[pygame.K_RIGHT]) : # RIGHT
        yellow.x += VEL
    if(key_press[pygame.K_UP]) : # UP
        yellow.y -= VEL
    if(key_press[pygame.K_DOWN]) : # DOWN
        yellow.y += VEL

def main():

    #7 upgrade the draw_window function
    red = pygame.Rect(300,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # 8. move spaceship
            # every loop pygame will ask you if have any key is press
            key_press = pygame.key.get_pressed()
            red_handle_movement(key_press, red)
            yellow_handle_movement(key_press, yellow)
        # 1. change color bg
            draw_window(red, yellow)
    pygame.quit()

if __name__ == "__main__":
    main()
