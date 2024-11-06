import pygame
# upgrade system help you find the path of image
import os
pygame.font.init()


WIDTH, HEIGHT = 900, 500 # CONTANT
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # create frame with WIDTH and HEIGHT
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
# 9. draw the border
BODER = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)
#12 health font
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
# 3 .fps
FPS = 30
VEL = 3
#10.2 define speed for bullet
BULLET_VEL = 7
#10.5
MAX_BULLET = 3
#10.7 create event add score
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
#11 create health
red_health = 10
yellow_health = 10
# 5 sacle up
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
# 4. create character
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
#11 . background img
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(WIDTH,HEIGHT))
#scale for character red
# 6 rotate
RED_SPACESHIP =pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90) 

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
#scale for character yellow
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
# 1.change caption 
pygame.display.set_caption("first game !")

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BLACK, BODER)

    #12 create health 
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    # draw inside window
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10 ))
    WIN.blit(yellow_health_text, ( 10, 10 ))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update() 

def draw_winner(winner_text) :
    draw_text = WINNER_FONT.render(winner_text, 1, WHITE)
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2, HEIGHT /2 - draw_text.get_height()/2))
    # update
    pygame.display.update()
    # delay 
    pygame.time.delay(5000)
    
def red_handle_movement(key_press,red):
    # 10 check if spaceship go off the screen or go cross the border
    if(key_press[pygame.K_a]) and red.x - VEL > 0 : # LEFT 
        red.x -= VEL
    if(key_press[pygame.K_d]) and red.x + VEL + SPACESHIP_WIDTH < BODER.x: # RIGHT
        red.x += VEL
    if(key_press[pygame.K_w]) and red.y - VEL > 0: # U
        red.y -= VEL
    if(key_press[pygame.K_s]) and red.y + VEL+ SPACESHIP_HEIGHT < HEIGHT : # DOWN
        red.y += VEL

def yellow_handle_movement(key_press,yellow):
    if(key_press[pygame.K_j]) and yellow.x - VEL >WIDTH /2 + 5 : # LEFT 
        yellow.x -= VEL
    if(key_press[pygame.K_l]) and yellow.x + VEL + SPACESHIP_WIDTH < WIDTH : # RIGHT
        yellow.x += VEL
    if(key_press[pygame.K_i]) and yellow.y - VEL > 0 : # UP
        yellow.y -= VEL
    if(key_press[pygame.K_k]) and yellow.y + VEL + SPACESHIP_HEIGHT < HEIGHT: # DOWN
        yellow.y += VEL

def handle_bullets(yellow_bullets, red_bullets, red, yellow) :
    # check if bullet collided with orther or go off screen
    for bullet in yellow_bullets :
        # move bullet
        bullet.x -= BULLET_VEL
        #check
        if(red.colliderect(bullet)):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets :
        # move bullet
        bullet.x += BULLET_VEL
        #check
        if(yellow.colliderect(bullet)):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH :
            red_bullets.remove(bullet)

def main():
    #7 upgrade the draw_window function
    red = pygame.Rect(300,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    # 10.1 bullet
    red_bullet = []
    yellow_bullet = []
    #12.1 create headth
    red_health = 10
    yellow_health = 10
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # 10.3 handle bullet when user press
            if event.type == pygame.KEYDOWN:
                # check if key is ctrl left or ctrl right
                if event.key == pygame.K_LCTRL and len(red_bullet) < MAX_BULLET:
                    # create bullet ( from body of red_spaceship)
                    bullet = pygame.Rect(red.x + red.width,red.y + red.height//2 -2,10, 5)
                    # append to red_bullet array
                    red_bullet.append(bullet)
                if event.key == pygame.K_RCTRL and len(yellow_bullet) < MAX_BULLET :
                    # create bullet
                    bullet = pygame.Rect(yellow.x,yellow.y +yellow.width//2 -2,10,5)
                    # append to red_bullet array
                    yellow_bullet.append(bullet)
            if event.type == RED_HIT :
                red_health -= 1
            if event.type == YELLOW_HIT:
                yellow_health -= 1

            winner_text = ""
            if red_health <= 0 :
                winner_text ="yellow winnwer !"

            if yellow_health <=0 :
                winner_text ="red winner !"
            
            if winner_text != "" :
                draw_winner(winner_text)
                break
            # 8. move spaceship
            # every loop pygame will ask you if have any key is press
            key_press = pygame.key.get_pressed()
            red_handle_movement(key_press, red)
            yellow_handle_movement(key_press, yellow)

            #10.6 handle bullet (firing)
            handle_bullets(yellow_bullet, red_bullet, red, yellow)
        # 1. change color bg
            draw_window(red, yellow, red_bullet, yellow_bullet, red_health, yellow_health)
    main()

if __name__ == "__main__":
    main()
