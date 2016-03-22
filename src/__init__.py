
if __name__ == '__main__':
	import os, pygame, sys, game, player
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	screen = pygame.display.set_mode((game.SCREEN_WIDTH, game.SCREEN_HEIGHT))
	black = 0, 0, 0
	game.init()
	
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit
			elif event.type == pygame.KEYDOWN:
				if game.MESSAGES:
					game.MESSAGES.pop()
				if event.key == pygame.K_w:
					player.POS_Y -= 1
					if player.POS_Y < 0:
						player.POS_Y = game.ROOM_HEIGHT - 1
				elif event.key == pygame.K_a:
					player.POS_X -= 1
					if player.POS_X < 0:
						player.POS_X = game.ROOM_WIDTH - 1
				elif event.key == pygame.K_s:
					player.POS_Y += 1
					if player.POS_Y >= game.ROOM_HEIGHT:
						player.POS_Y = 0
				elif event.key == pygame.K_d:
					player.POS_X += 1
					if player.POS_X >= game.ROOM_WIDTH:
						player.POS_X = 0
				
		game.update()
		screen.fill(black)
		
		game.render(screen)
		pygame.display.update()