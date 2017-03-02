import pygame;
# we are going to make the hero a sprite, sprites are special objects
# in pygame that come with cool features. so we need to include the class
from pygame.sprite import Sprite;

# create a class called hero, make it a sublcass of sprite (imported above)
class Hero(Sprite):
	# classes have two parts:
	# 1. properties/data
	# 2. methods
	# Initialize the calss properties with __init__ (start with just self)
	def __init__(self, image, screen):
		# because this is a subclass, we need to call super so that the parent class gets the data
		super(Hero, self).__init__();
		# give our hero an image property!
		self.image = pygame.image.load(image)

		self.image = pygame.transform.scale(self.image, (80, 80));
		# ..rect stuff
		# rect is available on all pygame entities. Its like x and y in canvas
		self.rect = self.image.get_rect()

		# add the screen to the object so we can use and reuse it as needed
		self.screen = screen;
		# find out the location and size of our screen (with get_rect())
		self.screen_rect = self.screen.get_rect();
		# print self.screen_rect
		# so, to put our hero on the left side, middle, set the self.rect 
		# properties to match those of the screen accordingly
		self.rect.bottom = self.screen_rect.bottom
		# set the left side to match the left side of screen
		self.rect.right = self.screen_rect.right;
		self.moving_right 	= False;
		self.moving_left 	= False;
		self.moving_up 		= False;
		self.moving_down 	= False;

		

	def update_me(self, settings):
		# if user is pushing left, move my self.rect left
		if 	 self.moving_right: self.rect.centerx += 1 * settings.hero_speed;
		elif self.moving_left: 	self.rect.centerx -= 1 * settings.hero_speed;
		elif self.moving_up: 	self.rect.centery -= 1 * settings.hero_speed;
		elif self.moving_down: 	self.rect.centery += 1 * settings.hero_speed;

	def draw_me(self):
		# first arg is "what" second is 'where' (exactly like ReactDOM)
		self.screen.blit(self.image, self.rect);
