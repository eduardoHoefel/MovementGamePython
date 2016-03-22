'''
Created on Mar 22, 2016

@author: eduardo
'''

import game
import character
from character import Character

def generateRoom(roomID):
	room = None
	if roomID == 0:
		room = Room(CLEAN_WHITE)
		room.openDoors(0, 2)
	return room

class Room():
	
	chars = []
	
	def __init__(self, style):
		self.style = style
		self.doors = [False, False, False, False]
		for i in xrange(game.ROOM_HEIGHT):
			self.chars.append([])
			for j in xrange(game.ROOM_WIDTH):
				#print [i, j]
				self.chars[i].append(Character(style.template.chars[i][j], style.fgColor, style.bgColor))
			
				
	def openDoors(self, *doors):
		for door in doors:
			self.doors[door] = True
			

class RoomStyle():
		
	id = 0
		
	def __init__(self, bgColor=character.BLACK, fgColor=character.WHITE):
		import template
		from template import Template

		self.bgColor = bgColor
		self.fgColor = fgColor
		self.template = Template(template.MAP_FOLDER, RoomStyle.id)
		RoomStyle.id += 1
		
		
CLEAN_WHITE = RoomStyle(bgColor=character.WHITE, fgColor=character.BLACK)
	