import pygame;
from pygame.sprite import Sprite;

class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings, bullet_level):
		super(Bullet,self).__init__();
		# Get the screen so the object can use it whenever needed
		self.screen = screen;
		self.image = pygame.image.load('images/shuriken4.png');
		self.image = pygame.transform.scale(self.image, (50, 100));
		# create a bullet from scratch
		# if bullet_type == 'vertical':
			# self.rect = pygame.Rect(0,0, game_settings.bullet_width, game_settings.bullet_height);
		# elif bullet_type == 'horizontal':
			# self.rect = pygame.Rect(0,0, game_settings.bullet_height, game_settings.bullet_width);
		# set the centerx of the bullet we just created to the centerx of the hero
		self.rect = self.image.get_rect();
		self.screen_rect = screen.get_rect();
		self.screen = screen;
		self.rect.x = self.screen_rect.x
		self.rect.y = self.screen_rect.y
		self.rect.centerx = hero.rect.centerx;
		# set the top to the hero top
		self.rect.centery = hero.rect.centery;
		# self.color = game_settings.bullet_color;
		self.speed = game_settings.bullet_speed;
		self.x = self.rect.x;
		self.y = self.rect.y;
		# self.direction = direction

	def update_bullet(self):
		# change the x and y accordingly based on self.speed
		# if self.direction == 'up':
		
		# elif self.direction == 'down':
			# self.y += self.speed;
		# elif self.direction == 'left':
			# self.x -= self.speed;
		# elif self.direction == 'right':
			# self.x += self.speed;									
			# actually change the y coord of this bullet
		# if self.y < -20:
		# 	self.x = 700
		# else:
		self.y -= self.speed;
		self.rect.y = self.y;
		self.rect.x = self.x;
	def draw_bullet(self):
		# draw rect takes 3 arg, what entity, what color, and where
		# pygame.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.image, self.rect)
		# draw.rect because its actually drawing the thing, not blit(images)
