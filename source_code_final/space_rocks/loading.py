import pygame
from pygame.locals import *

pygame.init()
background = pygame.image.load('bck.png')
graph = pygame.image.load("trend.png")
font = pygame.font.Font('freesansbold.ttf', 32)

window = pygame.display.set_mode((800, 600))

image_sprite = [pygame.image.load("1.png"),
				pygame.image.load("2.png"),pygame.image.load("3.png"),pygame.image.load("4.png")]

clock = pygame.time.Clock()

value = 0

run = True

while run:

	clock.tick(1)
	window.fill((202,73,73))
	window.blit(background, (0, 0))
	if value == len(image_sprite):
		text = font.render("Game Start",True,"aqua")
		textRect = text.get_rect()
		textRect.center = (400,300)
		window.blit(text,textRect)

	elif value > len(image_sprite):
		run = False
	else:
		text = font.render("Loading...",True,"aqua")
		textRect = text.get_rect()
		textRect.center = (80,50)
		window.blit(text,textRect)
		window.blit(graph,(165,33))
		image = image_sprite[value]
		x = 370

		if value == 0 or value == 1 or value == 2:
			y = 480
			window.blit(image, (x, y))
		else:
			while(y>0):
				y-=1
		window.blit(image, (x, y))
    #window.blit(image, (x, y))
	pygame.display.update()
	window.fill((202, 73, 73))
	value += 1
