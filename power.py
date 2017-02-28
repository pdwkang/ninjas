import pygame;
import math;
from pygame.sprite import Sprite

enemy_counter = 0;
class Bonus(Sprite):
	def __init__(self, screen, game_settings, monster_count, position):
		super(Enemy, self).__init__();
		self.image = pygame.image.load('images/monster1.png');
		self.image = pygame.transform.scale(self.image, (66, 66));
		
		self.rect = self.image.get_rect();
		self.screen_rect = screen.get_rect();
		self.screen = screen;
		self.rect.y = self.screen_rect.y
		self.enemy_counter = monster_count
		self.position = position
		self.current_time = game_settings.real_timer
		# enemry speed increase by timer
		self.speed = 4
		if self.current_time > 120:
			self.speed = self.current_time/80 + 12
		elif self.current_time > 100:
			self.speed = 12 
		elif self.current_time > 80:
			self.speed = 11 
		elif self.current_time > 60:
			self.speed = 10 
		elif self.current_time > 40:
			self.speed = 8 
		elif self.current_time > 20:
			self.speed = 6 
		else: self.speed = 4

		if self.position == 'front':
			self.rect.y = self.screen_rect.y 
		elif self.position == 'front1':
			self.rect.y = self.screen_rect.y - 40
		elif self.position == 'mid':
			self.rect.y = self.screen_rect.y - 80
		elif self.position == 'mid1':
			self.rect.y = self.screen_rect.y - 120
		elif self.position == 'back':
			self.rect.y = self.screen_rect.y - 160						
		elif self.position == 'back1':
			self.rect.y = self.screen_rect.y - 200


		if self.enemy_counter == 1:
			self.rect.x = 150
		elif self.enemy_counter == 2:
			self.rect.x = 175
		elif self.enemy_counter == 3:
			self.rect.x = 200
		elif self.enemy_counter == 4:
			self.rect.x = 225
		elif self.enemy_counter == 5:
			self.rect.x = 250
	def go_straight_down(self):
		if self.rect.y > 240:
			self.rect.y += 1 * self.speed;	
		elif self.rect.y > 170:
			self.rect.y += 0.9 * self.speed;		
		elif self.rect.y > 130:
			self.rect.y += 0.8 * self.speed;
		elif self.rect.y > 90:
			self.rect.y += 0.7 * self.speed;
		elif self.rect.y > 50:
			self.rect.y += 0.6 * self.speed;
		else:
			self.rect.y += 0.5 * self.speed;	

		if self.enemy_counter == 1:
			if self.rect.x > 0 :
				self.rect.x -= 1.4 * self.speed;	
		elif self.enemy_counter == 2:
			if self.rect.x > 100 :
				self.rect.x -= 1 * self.speed;	
		elif self.enemy_counter == 3:
			self.rect.x = 200
		elif self.enemy_counter == 4:
			if self.rect.x < 300 :
				self.rect.x += 1 * self.speed;	
		elif self.enemy_counter == 5:
			if self.rect.x < 400 :
				self.rect.x += 1.4 * self.speed;	

		
	def draw_me(self):
		self.screen.blit(self.image, self.rect);


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
