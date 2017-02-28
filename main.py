import pygame
import sys;
import time;
from hero import Hero;
from settings import Settings;
from pygame.sprite import Group, groupcollide
from game_functions import check_events, update_screen;
from enemy import Enemy;
from background import Background;



def run_game():
	print 'game ran'
	pygame.init();
	game_settings = Settings();
	game_start_time = time.time();
	real_game_start_time = time.time();
	# create a tuple for the screen size
	screen 		= pygame.display.set_mode(game_settings.screen_size);
	pygame.display.set_caption('a heroic pygame shooter')
	the_hero	= Hero('images/Hero.png', screen);
	bullets 	= Group();
	enemies 	= Group();
	background = Background('images/background.png', screen)
	def add_enemy():
		enemies.add(Enemy(screen, game_settings, 1, 'front'));
		enemies.add(Enemy(screen, game_settings, 2, 'front'));
		enemies.add(Enemy(screen, game_settings, 3, 'front'));
		enemies.add(Enemy(screen, game_settings, 4, 'front'));
		enemies.add(Enemy(screen, game_settings, 5, 'front'));
		enemies.add(Enemy(screen, game_settings, 1, 'front1'));
		enemies.add(Enemy(screen, game_settings, 2, 'front1'));
		enemies.add(Enemy(screen, game_settings, 3, 'front1'));
		enemies.add(Enemy(screen, game_settings, 4, 'front1'));
		enemies.add(Enemy(screen, game_settings, 5, 'front1'));
		enemies.add(Enemy(screen, game_settings, 1, 'mid'));
		enemies.add(Enemy(screen, game_settings, 2, 'mid'));
		enemies.add(Enemy(screen, game_settings, 3, 'mid'));
		enemies.add(Enemy(screen, game_settings, 4, 'mid'));
		enemies.add(Enemy(screen, game_settings, 5, 'mid'));

	def add_enemy2():
		enemies.add(Enemy(screen, game_settings, 1, 'mid1'));
		enemies.add(Enemy(screen, game_settings, 2, 'mid1'));
		enemies.add(Enemy(screen, game_settings, 3, 'mid1'));
		enemies.add(Enemy(screen, game_settings, 4, 'mid1'));
		enemies.add(Enemy(screen, game_settings, 5, 'mid1'));
	def add_enemy3():	
		enemies.add(Enemy(screen, game_settings, 1, 'back'));
		enemies.add(Enemy(screen, game_settings, 2, 'back'));
		enemies.add(Enemy(screen, game_settings, 3, 'back'));
		enemies.add(Enemy(screen, game_settings, 4, 'back'));
		enemies.add(Enemy(screen, game_settings, 5, 'back'));
	def add_enemy4():	
		enemies.add(Enemy(screen, game_settings, 1, 'back1'));
		enemies.add(Enemy(screen, game_settings, 2, 'back1'));
		enemies.add(Enemy(screen, game_settings, 3, 'back1'));
		enemies.add(Enemy(screen, game_settings, 4, 'back1'));
		enemies.add(Enemy(screen, game_settings, 5, 'back1'));		
	while 1:
		game_settings.real_timer = int(time.time() - real_game_start_time)
		reset_time = 0
		if game_settings.real_timer > 120:
			reset_time = 2.5
		elif game_settings.real_timer > 100:
			reset_time = 3
		elif game_settings.real_timer > 80:
			reset_time = 3.5
		elif game_settings.real_timer > 60:
			reset_time = 4
		elif game_settings.real_timer > 40:
			reset_time = 4.5
		elif game_settings.real_timer > 20:
			reset_time = 5
		else: reset_time = 6			

		game_settings.timer = int(time.time() - game_start_time)
		if (game_settings.timer) > reset_time:
			enemies = Group();
			add_enemy();
			if game_settings.real_timer > 29:
				add_enemy2();
				if game_settings.real_timer > 41:
					add_enemy3();
					if game_settings.real_timer > 51:
						add_enemy4();								

			game_start_time = time.time() 
			# bullets = Group();
		kill_enemy = groupcollide(bullets, enemies, True, True);
		# if kill_enemy:
			# kill_enemy2 = groupcollide(bullets, enemies, True, True);
		check_events(screen, the_hero, game_settings, bullets, enemies);
		update_screen(screen, the_hero, game_settings, bullets, enemies, background)

run_game();

		
