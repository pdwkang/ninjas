import pygame
import sys;
import time;
from hero import Hero;
from settings import Settings;
from pygame.sprite import Group, groupcollide
from game_functions import check_events, update_screen;
from enemy import Enemy;
from background import Background;
from power import Power;


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
	hero_group 	= Group();
	hero_group.add(the_hero)
	bullets 	= Group();
	enemies 	= Group();
	background  = Background('images/background.png', screen);
	power  = Power('images/react.png', screen)
	powers = Group();
	power2  = Power('images/redux.png', screen)
	powers2 = Group();	
	bullet_level = 1
	def add_enemy():
		enemies.add(Enemy(screen, game_settings, 1, 'front', 3));
		enemies.add(Enemy(screen, game_settings, 2, 'front', 3));
		enemies.add(Enemy(screen, game_settings, 3, 'front', 3));
		enemies.add(Enemy(screen, game_settings, 4, 'front', 3));
		enemies.add(Enemy(screen, game_settings, 5, 'front', 3));
		enemies.add(Enemy(screen, game_settings, 1, 'front1', 3));
		enemies.add(Enemy(screen, game_settings, 2, 'front1', 3));
		enemies.add(Enemy(screen, game_settings, 3, 'front1', 3));
		enemies.add(Enemy(screen, game_settings, 4, 'front1', 3));
		enemies.add(Enemy(screen, game_settings, 5, 'front1', 3));
	def add_enemy1():
		enemies.add(Enemy(screen, game_settings, 1, 'mid', 3));
		enemies.add(Enemy(screen, game_settings, 2, 'mid', 3));
		enemies.add(Enemy(screen, game_settings, 3, 'mid', 3));
		enemies.add(Enemy(screen, game_settings, 4, 'mid', 3));
		enemies.add(Enemy(screen, game_settings, 5, 'mid', 3));
	def add_enemy2():
		enemies.add(Enemy(screen, game_settings, 1, 'mid1', 3));
		enemies.add(Enemy(screen, game_settings, 2, 'mid1', 3));
		enemies.add(Enemy(screen, game_settings, 3, 'mid1', 3));
		enemies.add(Enemy(screen, game_settings, 4, 'mid1', 3));
		enemies.add(Enemy(screen, game_settings, 5, 'mid1', 3));
	def add_enemy3():	
		enemies.add(Enemy(screen, game_settings, 1, 'back', 3));
		enemies.add(Enemy(screen, game_settings, 2, 'back', 3));
		enemies.add(Enemy(screen, game_settings, 3, 'back', 3));
		enemies.add(Enemy(screen, game_settings, 4, 'back', 3));
		enemies.add(Enemy(screen, game_settings, 5, 'back', 3));
	def add_enemy4():	
		enemies.add(Enemy(screen, game_settings, 1, 'back1', 3));
		enemies.add(Enemy(screen, game_settings, 2, 'back1', 3));
		enemies.add(Enemy(screen, game_settings, 3, 'back1', 3));
		enemies.add(Enemy(screen, game_settings, 4, 'back1', 3));
		enemies.add(Enemy(screen, game_settings, 5, 'back1', 3));
	game_on = True
	add_enemy();
	while 1:

		if game_settings.game_active:
			game_settings.real_timer = int(time.time() - real_game_start_time)
			reset_time = 0
			if game_settings.real_timer > 120: reset_time = 4
			elif game_settings.real_timer > 100: reset_time = 5
			elif game_settings.real_timer > 80: reset_time = 6
			elif game_settings.real_timer > 60: reset_time = 7
			elif game_settings.real_timer > 40: reset_time = 8
			elif game_settings.real_timer > 20: reset_time = 9
			else: reset_time = 11			

			game_settings.timer = int(time.time() - game_start_time)
			if (game_settings.timer) > reset_time:
				enemies = Group();
				add_enemy();
				add_enemy1();

				if game_settings.real_timer in range(19, 26):
					powers.add(power);			
				if game_settings.real_timer > 29:
					add_enemy2();
					

					if game_settings.real_timer > 41:
						add_enemy3();						
						# if game_settings.real_timer in range(44, 50):
						powers2.add(power2);
						bullets = Group();														
						if game_settings.real_timer > 51:
							add_enemy4();
								

				game_start_time = time.time() 
			kill_enemy = False;
			if bullet_level == 3:
				kill_enemy = groupcollide(enemies, bullets, False, False);				
			else: 
				kill_enemy = groupcollide(enemies, bullets, False, True);
			for enemy in kill_enemy:
				enemy.hit(1);
				if enemy.health <= 0:
					enemies.remove(enemy);
					game_settings.ninjas_killed += 1;

			kill_hero = groupcollide(hero_group, enemies, True, True);
			if kill_hero:
				game_on = False;		
			power_up = groupcollide(hero_group, powers, False, True);	
			power_up2 = groupcollide(hero_group, powers2, False, True);	
			# print powers.len()
			if power_up2: bullet_level = 3
			elif power_up: bullet_level = 2
			# if kill_enemy:
				# kill_enemy2 = groupcollide(bullets, enemies, True, True);

			check_events(screen, the_hero, game_settings, bullets, bullet_level, enemies);
			update_screen(screen, hero_group, game_settings, bullets, enemies, background, powers, powers2, the_hero);
			# while not game_on:
				# time.sleep(1)
			print bullet_level

		
run_game();

		
