'''
Created on Mar 22, 2016

@author: eduardo
'''

import game

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

class Character():


	def __init__(self, char, fgColor=WHITE, bgColor=BLACK, bold=False):
		font = game.FONT
		self.bgColor = bgColor
		font.set_bold(bold)
		self.label = font.render(char, 1, fgColor, bgColor)
	
	
	
	def render(self, screen, y, x):	
		screen.blit(self.label, (x * game.FONT_WIDTH, y * game.FONT_SIZE))