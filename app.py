#MAKING a loop for the game
import pygame

from pygame import display, event, image
from animal import Animal

pygame.init()

display.set_caption("My Game") #to chng title of game window
screen=display.set_mode((812, 512))

matched= image.load('other_assets/matched.png') #match hoga to yeh print krega matched.
screen.blit(matched, (0,0)) #blit displays a surface on another surface
display.flip() #flit will update the screen, jab matched print hoga screen pr..tab..

running= True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

while running:
    current_events=event.get()
    for e in current_events:
        if e.type== pygame.QUIT:
            running=False
    
    screen.fill((255, 255, 255))

    for tile in tiles:
        screen.blit(title.image, (title.col * gc.IMAGE_SIZE, title.row * gc.IMAGE_SIZE))

    display.flip()
print("Goodbye!!") 
