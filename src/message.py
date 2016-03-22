'''
Created on Mar 22, 2016

@author: eduardo
'''

class Message():

	WIDTH = 19
	HEIGHT = 6
	chars = []

	def __init__(self, template):
		from character import Character
		import game
		room = game.getAtualRoom()
		for line in template.chars:
			charLine = []
			for char in line:
				charLine.append(Character(char, room.style.fgColor, room.style.bgColor))
			self.chars.append(charLine)
	
	def writeTo(self, charMatrix):
		for i in xrange(Message.HEIGHT):
			for j in xrange(Message.WIDTH):
				charMatrix[i+3][j+9] = self.chars[i][j]
		return charMatrix
				
				
import template
from template import Template
	
START1 = Template(template.MESSAGE_FOLDER, 0)
FOUND = Template(template.MESSAGE_FOLDER, 1)
LAYOUT = Template(template.MESSAGE_FOLDER, 2)