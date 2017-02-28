import pygame;
from pygame.sprite import Sprite;

class Background(Sprite):
	def __init__(self, image, screen):
		super(Background, self).__init__();
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (470,1500));
		self.rect = self.image.get_rect()
		self.screen = screen;

		self.screen_rect = self.screen.get_rect();

		# self.rect.bottom = self.screen_rect.bottom
		# set the left side to match the left side of screen
		self.rect.right = self.screen_rect.right;
	def update_me(self):
		if self.rect.y > 0:
			self.rect.y = -698;
		self.rect.y += 4
	def draw_me(self):
		self.screen.blit(self.image, self.rect);
