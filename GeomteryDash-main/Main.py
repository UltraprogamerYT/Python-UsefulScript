import pygame
from random import randint

pygame.init()

window_width = 710
window_height = 400
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Geometry Dash My Version")

#Map and player movement
player_surface = pygame.image.load('images/player2.png').convert()
player_rect = player_surface.get_rect(center = (80, 330))
map_surface = pygame.image.load('images/map.png').convert()
map_x_pos = 0
incrementer = 1

#Spike movement
spike_surface = pygame.image.load('images/Spikes.png').convert()
spike_list =[]
SPAWNSPIKE = pygame.USEREVENT
pygame.time.set_timer(SPAWNSPIKE,1500)


#Jumping Variables
vel = 5
isJump = False
jumpCount = 10
run = True


def background_loop():
    window.blit(map_surface, (int(map_x_pos),0))
    window.blit(map_surface, (int(map_x_pos + 710),0))

#Main loop that runs during the game
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SPAWNSPIKE:
            print("Spike")
    keys = pygame.key.get_pressed() #Checks for keys being pressed
    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            negative = 1
            if jumpCount <0:
                negative = -1
            player_rect.centery -= int(jumpCount **2 *0.15 * negative)
            jumpCount -=1
        else:
            isJump = False
            player_rect.centery = 330
            jumpCount = 10
    map_x_pos -= incrementer
    background_loop()
    if map_x_pos <= -710: #Checks for map being scrolled off on the side
        map_x_pos = 0
        incrementer = incrementer * 1.2
    window.blit(player_surface, player_rect)
    #pygame.draw.rect(window, player, (character['x'], character['y'], character['width'], character['height']))
    pygame.display.update()
pygame.quit()