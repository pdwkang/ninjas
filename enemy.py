import pygame;
import math;
from random import randint
from pygame.sprite import Sprite

enemy_images = ('images/monster1.png', 'images/monster2.png', 'images/monster3.png','images/monster4.png', 'images/monster5.png', 'images/monster6.png', 'images/reaper.png')
class Enemy(Sprite):
	def __init__(self, screen, game_settings, monster_count, position, health):
		super(Enemy, self).__init__();
		# random_index 		= randint(0,5);
		self.enemy_counter 	= monster_count
		self.position 		= position
		self.image 			= pygame.image.load(enemy_images[0]);
		# if   self.enemy_counter == 1: self.image = pygame.image.load(enemy_images[0]);
		# elif self.enemy_counter == 2: self.image = pygame.image.load(enemy_images[1]);
		# elif self.enemy_counter == 3: self.image = pygame.image.load(enemy_images[2]);
		# elif self.enemy_counter == 4: self.image = pygame.image.load(enemy_images[3]);
		# elif self.enemy_counter == 5: self.image = pygame.image.load(enemy_images[4]);	
		# if   self.position == 'front' : self.image = pygame.image.load(enemy_images[0]);
		# elif self.position == 'front1': self.image = pygame.image.load(enemy_images[2]);
		# elif self.position == 'mid'   : self.image = pygame.image.load(enemy_images[3]);
		# elif self.position == 'mid1'  : self.image = pygame.image.load(enemy_images[4]);	
		# elif self.position == 'back'  : self.image = pygame.image.load(enemy_images[1]);
		# elif self.position == 'back1' : self.image = pygame.image.load(enemy_images[5]);
		self.image 			= pygame.transform.scale(self.image, (80, 80));
		self.health 		= health
		self.rect 			= self.image.get_rect();
		self.screen_rect	= screen.get_rect();
		self.screen 		= screen;
		self.rect.y 		= self.screen_rect.y
		self.current_time 	= game_settings.real_timer
		self.speed 			= 1     # enemey speed increase by timer
		if   self.current_time > 120: self.speed = self.current_time/100 + 6
		elif self.current_time > 100: self.speed = 7 
		elif self.current_time > 80 : self.speed = 6 
		elif self.current_time > 60 : self.speed = 5 
		elif self.current_time > 40 : self.speed = 4 
		elif self.current_time > 20 : self.speed = 3
		else						: self.speed = 2

		if   self.position == 'front' : self.rect.y = self.screen_rect.y 
		elif self.position == 'front1': self.rect.y = self.screen_rect.y - 90
		elif self.position == 'mid'   : self.rect.y = self.screen_rect.y - 180
		elif self.position == 'mid1'  : self.rect.y = self.screen_rect.y - 270
		elif self.position == 'back'  : self.rect.y = self.screen_rect.y - 360						
		elif self.position == 'back1' : self.rect.y = self.screen_rect.y - 450

		self.direction = 1
		# print self.direction
		if   self.enemy_counter == 1: self.rect.x = 150
		elif self.enemy_counter == 2: self.rect.x = 175
		elif self.enemy_counter == 3: self.rect.x = 200
		elif self.enemy_counter == 4: self.rect.x = 225
		elif self.enemy_counter == 5: self.rect.x = 250
	def go_straight_down(self):
		if self.health > 1.5: 
			self.rect.y += 1.0 * self.speed;	
			if   self.enemy_counter == 1: self.rect.x += 1 * self.direction;			
			elif self.enemy_counter == 2: self.rect.x += 2 * self.direction
			elif self.enemy_counter == 3: self.rect.x += 3 * self.direction
			elif self.enemy_counter == 4: self.rect.x += 4 * self.direction
			elif self.enemy_counter == 5: self.rect.x += 5 * self.direction
		if self.rect.x in range(0,50): self.direction = 1.2
		if self.rect.x in range(350, 400): self.direction = -1.2
		
	def draw_me(self):
		self.screen.blit(self.image, self.rect);

	def hit(self, damage):
		if self.current_time > 45:
			self.health -= damage * 1;
		else:
			self.health -= damage * 1.5;
		if self.health <= 1.5: 
			self.image = pygame.image.load(enemy_images[6]);
			self.image = pygame.transform.scale(self.image, (80, 80));
	# follow hero
		# def follow_hero(self, hero):
		# dx = self.rect.x - hero.rect.x;
		# dy = self.rect.y - hero.rect.y;
		# dist = math.hypot(dx, dy)
		# if dist == 0: dist = 1
		# dx = dx / dist;
		# dy = dy / dist;
		# self.rect.x -= dx * self.speed;
		# self.rect.y -= dy * self.speed;
		# self.x = self.rect.x;
		# self.y = self.rect.y;				
