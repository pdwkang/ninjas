import pygame;
from pygame.sprite import Sprite;
import math
class Power(Sprite):
	def __init__(self, image, screen):
		super(Power, self).__init__();
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (60,60));
		self.rect = self.image.get_rect()
		self.screen = screen;

		self.screen_rect = self.screen.get_rect();

		# self.rect.bottom = self.screen_rect.bottom
		# set the left side to match the left side of screen
		self.rect.right = self.screen_rect.right;
		self.speed = 4
	def follow_hero(self, hero):
		dx = self.rect.x - hero.rect.x;
		dy = self.rect.y - hero.rect.y;
		dist = math.hypot(dx, dy)
		if dist == 0: dist = 1
		dx = dx / dist;
		dy = dy / dist;
		self.rect.x -= dx * self.speed;
		self.rect.y -= dy * self.speed;
		self.x = self.rect.x;
		self.y = self.rect.y;				
	# def update_me(self):
	# 	if self.rect.y > 0:
	# 		self.rect.y = -698;
	# 	self.rect.y += 4
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
