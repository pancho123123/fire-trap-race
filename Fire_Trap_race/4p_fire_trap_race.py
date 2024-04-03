import pygame, random
from random import randint

WIDTH = 1366
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)
#BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire Trap Race")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/sven.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.centery = 350
		self.speed_x = 0
		self.hp = 100

class Player1(Player):
	#def __init__(self):
		#super().__init__()
		
	def update(self):
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -3
		if keystate[pygame.K_d]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -3
		if keystate[pygame.K_s]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH + 50:
			self.rect.right = WIDTH + 50
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 170:
			self.rect.top = 170
		if self.rect.bottom > 460:
			self.rect.bottom = 460

class Player2(Player):
	def __init__(self):
		super().__init__()
				
	def update(self):
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -3
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -3
		if keystate[pygame.K_DOWN]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH + 50:
			self.rect.right = WIDTH + 50
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 170:
			self.rect.top = 170
		if self.rect.bottom > 460:
			self.rect.bottom = 460

class Player3(Player):
	def __init__(self):
		super().__init__()
				
	def update(self):
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			self.speed_x = -3
		if keystate[pygame.K_h]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_t]:
			self.speed_y = -3
		if keystate[pygame.K_g]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH + 50:
			self.rect.right = WIDTH + 50
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 170:
			self.rect.top = 170
		if self.rect.bottom > 460:
			self.rect.bottom = 460

class Player4(Player):
	def __init__(self):
		super().__init__()
				
	def update(self):
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_j]:
			self.speed_x = -3
		if keystate[pygame.K_l]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_i]:
			self.speed_y = -3
		if keystate[pygame.K_k]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH + 50:
			self.rect.right = WIDTH +50
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 170:
			self.rect.top = 170
		if self.rect.bottom > 460:
			self.rect.bottom = 460

class Fire_trap1a(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/1a.png").convert(),(100,100))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		
class Fire_trap1a1(Fire_trap1a):
	def __init__(self):
		super().__init__()
		self.rect.x = 385
		self.rect.y = 150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)

class Fire_trap1a2(Fire_trap1a):
	def __init__(self):
		super().__init__()
		self.rect.x = 600
		self.rect.y =  150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)

class Fire_trap1a3(Fire_trap1a):
	def __init__(self):
		super().__init__()
		self.rect.x = 710
		self.rect.y = 150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)

class Fire_trap1a4(Fire_trap1a):
	def __init__(self):
		super().__init__()
		self.rect.x = 1100
		self.rect.y =  150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)

class Fire_trap1a5(Fire_trap1a):
	def __init__(self):
		super().__init__()
		self.rect.x = 50
		self.rect.y =  150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)

class Fire_trap1a6(Fire_trap1a):
	def __init__(self):
		super().__init__()
		self.rect.x = 50
		self.rect.y =  150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)

class Fire_trap1b(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/1b.png").convert(),(100,100))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	
class Fire_trap1b1(Fire_trap1b):
	def __init__(self):
		super().__init__()
		self.rect.x = 390
		self.rect.y =  410

	def shoot(self):
		bullet2 = Bullet2(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet2)
		bullets.add(bullet2)

class Fire_trap1b2(Fire_trap1b):
	def __init__(self):
		super().__init__()
		self.rect.x = 670
		self.rect.y =  410

	def shoot(self):
		bullet2 = Bullet2(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet2)
		bullets.add(bullet2)

class Fire_trap1b3(Fire_trap1b):
	def __init__(self):
		super().__init__()
		self.rect.x = 1150
		self.rect.y =  410

	def shoot(self):
		bullet2 = Bullet2(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet2)
		bullets.add(bullet2)

class Fire_trap1b4(Fire_trap1b):
	def __init__(self):
		super().__init__()
		self.rect.x = 50
		self.rect.y =  366

	def shoot(self):
		bullet2 = Bullet2(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet2)
		bullets.add(bullet2)

class Fire_trap2a(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/2a.png").convert(),(100,100))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 20
		self.rect.y =  410

	def shoot(self):
		bullet2 = Bullet2(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet2)
		bullets.add(bullet2)

class Fire_trap2b(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/2b.png").convert(),(100,100))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 110
		self.rect.y =  410

	def shoot(self):
		bullet2 = Bullet2(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet2)
		bullets.add(bullet2)

class Fire_trap3a(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/3a.png").convert(),(65,100))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 850
		self.rect.y =  150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)

class Fire_trap3b(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/3b.png").convert(),(65,100))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 910
		self.rect.y =  150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)
		
class Fire_trap3c(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/3c.png").convert(),(60,90))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 975
		self.rect.y =  150

	def shoot(self):
		bullet1 = Bullet1(self.rect.centerx, self.rect.bottom)
		all_sprites.add(bullet1)
		bullets.add(bullet1)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x , y):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/bullet.png").convert(),(10,10))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centery = y
		self.rect.centerx = x

class Bullet1(Bullet):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.speedy = 10
	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > 520:
			self.kill()

class Bullet2(Bullet):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.speedy = -10
	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 150:
			self.kill()

def show_go_screen():
	
	screen.fill(BLACK)
	draw_text1(screen, "Fire Trap Race", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Make it to the end without being killed by the fire", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	
	
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False


def show_game_over_screenp1():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 1 Lose", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 2 Lose", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp3():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 3 Lose", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp4():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 4 Lose", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False


background = pygame.transform.scale(pygame.image.load("img/2.png").convert(), (1300,700))


game_over1 = False
game_over2 = False
game_over3 = False
game_over4 = False
running = True
start = True
counter = True
trap1_times = [
	2,3,4,7,8,9,10,13,14,15,16,19,20,21,22,25,26,27,28,31,32,33,34,37,38,39,40,43,44,45,46,49,50,
	51,52,55,56,57,58,61,62,63,64,67,68,69,70,73,74,75,76,79,80,81,82,85,86,87,88,91,92,93,94,97,
	98,99,100,103,104,105,106,109,110,111,112,115,116,117,118] #(2a)
trap2_times = [
	2,3,4,7,8,11,12,13,14,17,18,19,20,23,24,27,28,29,30,33,34,35,36,39,40,43,44,45,46,49,50,51,
	52,55,56,59,60,61,62,65,66,67,68,71,72,75,76,77,78,81,82,83,84,87,88,91,92,93,94,97,98,99,
	100,103,104,107,108,109,110,113,114,115,116,119] # (2b), (3a), (3c), (1a6)#1131311131113131113111313
trap3_times = [
	4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52,55,58,61,64,67,70,73,76,79,82,85,88,91,94,97,
	100,103,106,109,112,115,118] # (1a1), (3b), (1b2), (1a4), (1b3), (1a7)
trap4_times = [
	3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,
	69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99,101,103,105,107,109,111,113,115,117,119] # (1a2)
trap5_times = [
	2,3,6,7,8,11,12,13,16,17,18,21,22,23,26,27,28,31,32,33,36,37,38,41,42,43,45,46,47,50,51,52,55,56,
	57,60,61,62,64,65,66,69,70,71,74,75,76,79,80,81,84,85,86,89,90,91,94,95,96,99,100,101,104,105,106,
	109,110,111,114,115,116,119] # (1b1), (1b4) 113113113113
trap6_times = [
	2,3,4,7,8,11,12,13,14,17,
	]
trap1_idx = 0
trap2_idx = 0
trap3_idx = 0
trap4_idx = 0
trap5_idx = 0
while running:
	if game_over1:

		show_game_over_screenp1()
		screen.blit(background,(0,0))
		game_over1 = False		
		all_sprites = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		fire_trap1a1 = Fire_trap1a1()
		fire_trap1a2 = Fire_trap1a2()
		fire_trap1a3 = Fire_trap1a3()
		fire_trap1a4 = Fire_trap1a4()
		fire_trap2a = Fire_trap2a()
		fire_trap2b = Fire_trap2b()
		fire_trap1b1 = Fire_trap1b1()
		fire_trap1b2 = Fire_trap1b2()
		fire_trap1b3 = Fire_trap1b3()
		fire_trap3a = Fire_trap3a()
		fire_trap3b = Fire_trap3b()
		fire_trap3c = Fire_trap3c()
		all_sprites.add(fire_trap1a1, fire_trap1a2, fire_trap1a3, fire_trap1a4, fire_trap2a, 
		fire_trap2b, fire_trap1b1, fire_trap1b2, fire_trap1b3, fire_trap3a, fire_trap3b, fire_trap3c)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		trap1_idx = 0
		trap2_idx = 0
		trap3_idx = 0
		trap4_idx = 0
		trap5_idx = 0
		start_time = pygame.time.get_ticks()

	if game_over2:

		show_game_over_screenp2()
				
		screen.blit(background,(0,0))
		game_over2 = False
		all_sprites = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		fire_trap1a1 = Fire_trap1a1()
		fire_trap1a2 = Fire_trap1a2()
		fire_trap1a3 = Fire_trap1a3()
		fire_trap1a4 = Fire_trap1a4()
		fire_trap2a = Fire_trap2a()
		fire_trap2b = Fire_trap2b()
		fire_trap1b1 = Fire_trap1b1()
		fire_trap1b2 = Fire_trap1b2()
		fire_trap1b3 = Fire_trap1b3()
		fire_trap3a = Fire_trap3a()
		fire_trap3b = Fire_trap3b()
		fire_trap3c = Fire_trap3c()
		all_sprites.add(fire_trap1a1, fire_trap1a2, fire_trap1a3, fire_trap1a4, fire_trap2a, 
		fire_trap2b, fire_trap1b1, fire_trap1b2, fire_trap1b3, fire_trap3a, fire_trap3b, fire_trap3c)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		trap1_idx = 0
		trap2_idx = 0
		trap3_idx = 0
		trap4_idx = 0
		trap5_idx = 0
		start_time = pygame.time.get_ticks()

	if game_over3:

		show_game_over_screenp3()
		
		
		screen.blit(background,(0,0))
		game_over3 = False
		all_sprites = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		fire_trap1a1 = Fire_trap1a1()
		fire_trap1a2 = Fire_trap1a2()
		fire_trap1a3 = Fire_trap1a3()
		fire_trap1a4 = Fire_trap1a4()
		fire_trap2a = Fire_trap2a()
		fire_trap2b = Fire_trap2b()
		fire_trap1b1 = Fire_trap1b1()
		fire_trap1b2 = Fire_trap1b2()
		fire_trap1b3 = Fire_trap1b3()
		fire_trap3a = Fire_trap3a()
		fire_trap3b = Fire_trap3b()
		fire_trap3c = Fire_trap3c()
		all_sprites.add(fire_trap1a1, fire_trap1a2, fire_trap1a3, fire_trap1a4, fire_trap2a, 
		fire_trap2b,fire_trap1b1, fire_trap1b2, fire_trap1b3, fire_trap3a, fire_trap3b, fire_trap3c)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		trap1_idx = 0
		trap2_idx = 0
		trap3_idx = 0
		trap4_idx = 0
		trap5_idx = 0
		start_time = pygame.time.get_ticks()

	if game_over4:

		show_game_over_screenp4()
		
		screen.blit(background,(0,0))
		game_over4 = False
		all_sprites = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		fire_trap1a1 = Fire_trap1a1()
		fire_trap1a2 = Fire_trap1a2()
		fire_trap1a3 = Fire_trap1a3()
		fire_trap1a4 = Fire_trap1a4()
		fire_trap2a = Fire_trap2a()
		fire_trap2b = Fire_trap2b()
		fire_trap1b1 = Fire_trap1b1()
		fire_trap1b2 = Fire_trap1b2()
		fire_trap1b3 = Fire_trap1b3()
		fire_trap3a = Fire_trap3a()
		fire_trap3b = Fire_trap3b()
		fire_trap3c = Fire_trap3c()
		all_sprites.add(fire_trap1a1, fire_trap1a2, fire_trap1a3, fire_trap1a4, fire_trap2a, 
		fire_trap2b, fire_trap1b1, fire_trap1b2, fire_trap1b3, fire_trap3a, fire_trap3b, fire_trap3c)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		trap1_idx = 0
		trap2_idx = 0
		trap3_idx = 0
		trap4_idx = 0
		trap5_idx = 0
		start_time = pygame.time.get_ticks()

	if start:
		show_go_screen()
		
		start = False
		screen.blit(background,(0,0))
		all_sprites = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		fire_trap1a1 = Fire_trap1a1()
		fire_trap1a2 = Fire_trap1a2()
		fire_trap1a3 = Fire_trap1a3()
		fire_trap1a4 = Fire_trap1a4()
		fire_trap2a = Fire_trap2a()
		fire_trap2b = Fire_trap2b()
		fire_trap1b1 = Fire_trap1b1()
		fire_trap1b2 = Fire_trap1b2()
		fire_trap1b3 = Fire_trap1b3()
		fire_trap3a = Fire_trap3a()
		fire_trap3b = Fire_trap3b()
		fire_trap3c = Fire_trap3c()
		all_sprites.add(fire_trap1a1, fire_trap1a2, fire_trap1a3, fire_trap1a4, fire_trap2a, 
		fire_trap2b, fire_trap1b1, fire_trap1b2, fire_trap1b3, fire_trap3a, fire_trap3b, fire_trap3c)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		start_time = pygame.time.get_ticks()
		
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

	if player1.hp == 0:
		player1.hp = 100
		player1.rect.x = 0
		player1.rect.y = HEIGHT//2
		
	if player2.hp == 0:
		player2.hp = 100
		player2.rect.x = 0
		player2.rect.y = HEIGHT//2
		
	if player3.hp == 0:
		player3.hp = 100
		player3.rect.x = 0
		player3.rect.y = HEIGHT//2
		
	if player4.hp == 0:
		player4.hp = 100
		player4.rect.x = 0
		player4.rect.y = HEIGHT//2
		
	now = (pygame.time.get_ticks() - start_time)//1000
	
	if now % 121 in trap1_times[trap1_idx:]:
		fire_trap2a.shoot()
		trap1_idx += 1
		if trap1_idx == len(trap1_times):
			trap1_idx = 0

	if now % 121 in trap2_times[trap2_idx:]:
		fire_trap2b.shoot()
		fire_trap3a.shoot()
		fire_trap3c.shoot()
		fire_trap1a4.shoot()
		trap2_idx += 1
		if trap2_idx == len(trap2_times):
			trap2_idx = 0

	if now % 121 in trap3_times[trap3_idx:]:
		fire_trap3b.shoot()
		fire_trap1a2.shoot()
		fire_trap1a3.shoot()
		fire_trap1b2.shoot()
		fire_trap1b3.shoot()
		trap3_idx += 1
		if trap3_idx == len(trap3_times):
			trap3_idx = 0

	if now % 121 in trap4_times[trap4_idx:]:
		fire_trap1a1.shoot()
		trap4_idx += 1
		if trap4_idx == len(trap4_times):
			trap4_idx = 0

	if now % 121 in trap5_times[trap5_idx:]:
		fire_trap1b1.shoot()
		trap5_idx += 1
		if trap5_idx == len(trap5_times):
			trap5_idx = 0

	if counter:
			counter = False
			fire_trap1a1.shoot()
			fire_trap1a2.shoot()
			fire_trap1a3.shoot()
			fire_trap1a4.shoot()
			fire_trap1b1.shoot()
			fire_trap1b2.shoot()
			fire_trap1b3.shoot()
			fire_trap2a.shoot()
			fire_trap2b.shoot()
			fire_trap3a.shoot()
			fire_trap3b.shoot()
			fire_trap3c.shoot()
	
	all_sprites.update()
	
	
	
	# Checar colisiones - player1 - bullets
	hits = pygame.sprite.spritecollide(player1, bullets, True)
	for hit in hits:
		
		if player1.hp > 0:
			player1.hp -= 20
			
	# Checar colisiones - player2 - bullets
	hits = pygame.sprite.spritecollide(player2, bullets, True)
	for hit in hits:
		
		if player2.hp > 0:
			player2.hp -= 20
			
	# Checar colisiones - player3 - bullets
	hits = pygame.sprite.spritecollide(player3, bullets, True)
	for hit in hits:
		
		if player3.hp > 0:
			player3.hp -= 20

	# Checar colisiones - player4 - bullets
	hits = pygame.sprite.spritecollide(player4, bullets, True)
	for hit in hits:
		
		if player4.hp > 0:
			player4.hp -= 20

			
	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
	
	# Escudo.
	draw_text1(screen, "P1", 20, 110, 6)
	draw_text1(screen, "P2", 20, 400, 6)
	draw_text1(screen, "P3", 20, 700, 6)
	draw_text1(screen, "P4", 20, 1000, 6)

	draw_hp_bar(screen, 120, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 170, 6)
	if player1.hp > 0:
		draw_hp_bar(screen, player1.rect.x, player1.rect.y - 10, player1.hp)

	draw_hp_bar(screen, 415, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 470, 6)
	if player2.hp > 0:
		draw_hp_bar(screen, player2.rect.x, player2.rect.y - 10, player2.hp)

	draw_hp_bar(screen, 715, 5, player3.hp)
	draw_text2(screen, str(int(player3.hp))+ "/100", 10, 770, 6)
	if player3.hp > 0:
		draw_hp_bar(screen, player3.rect.x, player3.rect.y - 10, player3.hp)

	draw_hp_bar(screen, 1015, 5, player4.hp)
	draw_text2(screen, str(int(player4.hp))+ "/100", 10, 1070, 6)
	if player4.hp > 0:
		draw_hp_bar(screen, player4.rect.x, player4.rect.y - 10, player4.hp)
	
	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
		

	pygame.display.flip()
pygame.quit()