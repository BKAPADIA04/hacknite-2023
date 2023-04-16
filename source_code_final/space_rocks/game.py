import pygame
import random
from pygame import mixer
from pygame.math import Vector2
pygame.init()
from models import Asteroid, Spaceship, GameObject,Powerup
from utils import get_random_position, load_sprite, print_text
from load import *
#from menu import *

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
blue = (0, 0, 128)
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font('freesansbold.ttf', 32)
score = 0


class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        self._init_pygame()
        self.paused = False #
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        self.health = 200
        self.score = 0
        self.asteroids = []
        self.power = []
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)
        #self.power_up = GameObject((random.randint(0,800), random.randint(0,600)), load_sprite("planet-04"), (0, 1))

        for _ in range(10):
            while True:
                position = get_random_position(screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break

            self.asteroids.append(Asteroid(position, self.asteroids.append))

        # if(self.score%5==0):
        for _ in range(1):
            while True:
                position = get_random_position(screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break

            self.power.append(Powerup(position, self.power.append))
 


    def main_loop(self):
        mixer.music.load('background.wav')
        mixer.music.play(-1)
        while True:
            self._handle_input()
            if not self.paused:
                self._process_game_logic()
            self._draw()



    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            if (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.paused = not self.paused
        

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship and not self.paused:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()
            if is_key_pressed[pygame.K_DOWN]:
                self.spaceship.decelerate()

    def _process_game_logic(self):
        #self.power_up.move(screen)
        for game_object in self._get_game_objects():
            game_object.move(screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.health -= 1
                    mixer.music.load('hq-explosion-6288.wav')
                    mixer.music.play()
                    if(self.health<0):
                        self.spaceship = None
                        self.message = "You lost!"
                        break

        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.score += 1
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    mixer.music.load('explosion.wav')
                    mixer.music.play()
                    mixer.music.load('background.wav')
                    mixer.music.play(-1)
                    break
            for p in self.power[:]:
                if p.collides_with(bullet):
                    self.score += 10
                    self.power.remove(p)
                    self.bullets.remove(bullet)

        for bullet in self.bullets[:]:
            if not screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)
                
        if not self.asteroids and self.spaceship:
            self.message = "You won!"

    def _draw(self):
        screen.blit(self.background, (0, 0))
        text = font.render('score: ' + str(self.score), True, GREEN,blue)
        textRect = text.get_rect()
        textRect.center = (85,50)
        screen.blit(text, textRect)
        pygame.draw.rect(screen,RED,(10,10,200,10))
        pygame.draw.rect(screen,GREEN,(10,10,self.health,10))
        #self.power_up.draw(screen)

        if not self.paused:
            for game_object in self._get_game_objects():
                game_object.draw(screen)
            for g_o in self.power_objects():
                g_o.draw(screen)

            if self.message:
                print_text(screen, self.message, self.font)

        pygame.display.flip()
        self.clock.tick(60)

    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]
        if self.spaceship:
            game_objects.append(self.spaceship)
        return game_objects
    
    def power_objects(self):
        game_obj = [*self.power, *self.bullets]
        if self.spaceship:
            game_obj.append(self.spaceship)
        return game_obj
