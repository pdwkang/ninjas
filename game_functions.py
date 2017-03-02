import pygame;
import sys;
from bullet import Bullet;

# class utility_functions(object):
# 	@staticmethod
# 	def check_events():
# 		print "Static test";

def check_events(screen, hero, game_settings, bullets, bullet_level, enemies):
	# pygame automatically creates an event queue (like JS)
	# we want to patch into certain events 
	# like... click, keypress, quit
	for event in pygame.event.get():
		# quit
		if event.type == pygame.QUIT:
			sys.exit();
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if bullet_level == 1:
					bullets.add(Bullet(screen, hero, game_settings, 1))
				elif bullet_level == 2:
					bullets.add(Bullet(screen, hero, game_settings, 1))
					bullets.add(Bullet(screen, hero, game_settings, 2))
					bullets.add(Bullet(screen, hero, game_settings, 3))
				elif bullet_level == 3:
					bullets.add(Bullet(screen, hero, game_settings, 4))
				# print bullets
			# elif event.key == pygame.K_a:
			# 	new_bullet = Bullet(screen, hero, game_settings, 'left', 'horizontal');
			# 	bullets.add(new_bullet);
		if hero.rect.x <= 0: hero.rect.x = 10
		if hero.rect.x >= 400: hero.rect.x = 390;			
		if hero.rect.y >= 660: hero.rect.y = 650;			
		if event.type == pygame.KEYDOWN and hero.rect.x >= 0 and hero.rect.x <= 400:
			if event.key == pygame.K_RIGHT: hero.moving_right	= True;
			elif event.key == pygame.K_LEFT: hero.moving_left	= True;
			elif event.key == pygame.K_UP	:    hero.moving_up	= True;
			elif event.key == pygame.K_DOWN	:  hero.moving_down	= True;							
		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT: hero.moving_right = False;
			elif event.key == pygame.K_LEFT	: hero.moving_left	= False;
			elif event.key == pygame.K_UP	: hero.moving_up	= False;
			elif event.key == pygame.K_DOWN	: hero.moving_down	= False;
			# while event.key == pygame.K_SPACE:
			# 	new_bullet = Bullet(screen, hero, game_settings, 'up');
			# 	bullets.add(new_bullet)				
		# elif event.type == pygame.K_a:	
		# elif event.type == pygame.KEYUP:
		# 	if event.key == pygame.K_SPACE:



def update_screen(screen, hero_group, game_settings, bullets, enemies, background, powers, powers2, the_hero):
	background.update_me();
	background.draw_me();
	# the_hero.update_me(game_settings);
	# the_hero.draw_me();
	# power.follow_hero(the_hero);
	# power.draw_me();	
	for power in powers.sprites():
		power.follow_hero(the_hero);
		power.draw_me();	
	for power2 in powers2.sprites():
		power2.follow_hero(the_hero);
		power2.draw_me();			

	for hero in hero_group.sprites():
		hero.update_me(game_settings);
		hero.draw_me();
	# Loop through bullets
	for bullet in bullets.sprites():
		bullet.update_bullet();
		bullet.draw_bullet();
	# enemy draw
	for enemy in enemies:
		# enemy.update_me(the_hero);
		enemy.go_straight_down();
		enemy.draw_me();
	score_font = pygame.font.SysFont("monospace",36);
	# render a font takes 3 params:
	# 1. What text.
	# 2. I cant remember
	# 3. Color
	score_render = score_font.render("Score: "+str(game_settings.ninjas_killed),1,(255,255,255));		
	screen.blit(score_render,(20,20));	




	# Flip/wipe out screen
	pygame.display.flip();	
			