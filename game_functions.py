import pygame;
import sys;
from bullet import Bullet;

# class utility_functions(object):
# 	@staticmethod
# 	def check_events():
# 		print "Static test";

def check_events(screen, hero, game_settings, bullets, enemies):
	# pygame automatically creates an event queue (like JS)
	# we want to patch into certain events 
	# like... click, keypress, quit
	for event in pygame.event.get():
		# quit
		if event.type == pygame.QUIT:
			sys.exit();
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bullets.add(Bullet(screen, hero, game_settings, 1))
				# print bullets
			# elif event.key == pygame.K_a:
			# 	new_bullet = Bullet(screen, hero, game_settings, 'left', 'horizontal');
			# 	bullets.add(new_bullet);
		if hero.rect.x <= 0:
			hero.rect.x = 10
		if hero.rect.x >= 400:
			hero.rect.x = 390;			
		if event.type == pygame.KEYDOWN and hero.rect.x >= 0 and hero.rect.x <= 400:
			if event.key == pygame.K_RIGHT: hero.moving_right	= True;
			elif event.key == pygame.K_LEFT: hero.moving_left	= True;
		

			# elif event.key == pygame.K_UP	:    hero.moving_up	= True;
			# elif event.key == pygame.K_DOWN	:  hero.moving_down	= True;							
		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT: hero.moving_right = False;
			elif event.key == pygame.K_LEFT	: hero.moving_left	= False;
			# elif event.key == pygame.K_UP	: hero.moving_up	= False;
			# elif event.key == pygame.K_DOWN	: hero.moving_down	= False;
			# while event.key == pygame.K_SPACE:
			# 	new_bullet = Bullet(screen, hero, game_settings, 'up');
			# 	bullets.add(new_bullet)				
		# elif event.type == pygame.K_a:	
		# elif event.type == pygame.KEYUP:
		# 	if event.key == pygame.K_SPACE:


def update_screen(screen, the_hero, game_settings, bullets, enemies, background):
	background.update_me();
	background.draw_me();
	the_hero.update_me(game_settings);
	the_hero.draw_me();
	# Loop through bullets
	for bullet in bullets.sprites():
		bullet.update_bullet();
		bullet.draw_bullet();
	# enemy draw
	for enemy in enemies:
		# enemy.update_me(the_hero);
		enemy.go_straight_down();
		enemy.draw_me();
	



	# Flip/wipe out screen
	pygame.display.flip();	
			