'''
Created on Mar 22, 2016

@author: eduardo
'''
import message
from message import Message
import room
import pygame

class State():
	
	
	def __init__(self):
		self.ticks = 0
		self.limit = -1
		
	def update(self):
		self.ticks += 1


RUNNING = State()
SWITCHING_ROOM = State()

class Command():
	
	
	def __init__(self, value):
		self.value = value
		
	
	@classmethod
	def valueOf(commands):
		value = 4 * commands[0].value + commands[1].value
		return value
	
	@classmethod
	def add(commands, newCommand):
		commands[0] = commands[1]
		commands[1] = newCommand
		

DOWN = Command(0)
LEFT = Command(1)
UP = Command(2)
RIGHT = Command(3)

FONT_SIZE = 35
FONT_WIDTH = int(FONT_SIZE * 0.6)
ROOM_WIDTH = 38
ROOM_HEIGHT = 12
SCREEN_HEIGHT = FONT_SIZE * ROOM_HEIGHT
SCREEN_WIDTH = FONT_WIDTH * ROOM_WIDTH
pygame.font.init()
FONT = pygame.font.SysFont("Courier", FONT_SIZE)
STATE = RUNNING
MODIFIED = True	
GOT_BONUS = False
ROOMS = []
ROOMS_ENTERED = 1
ATUAL_ROOM_ID = 0
LAST_ROOM_ID = -1
COMMANDS = [DOWN, DOWN]
MESSAGES = []

import player

def init():
	ROOMS.append(room.generateRoom(0))
	MESSAGES.append(Message(message.START1))
		
def render(screen):
	charMatrix = [[char for char in line] for line in getAtualRoom().chars]
		
	playerPos = charMatrix[player.POS_Y][player.POS_X]
	charMatrix[player.POS_Y][player.POS_X] = player.getSymbolWithBackground(playerPos.bgColor)
		
	if MESSAGES:
		charMatrix = MESSAGES[0].writeTo(charMatrix)
		
	for i in xrange(len(charMatrix)):
		for j in xrange(len(charMatrix[i])):
			charMatrix[i][j].render(screen, i, j)

def update():
	pass
	

def getAtualRoom():
	return ROOMS[ATUAL_ROOM_ID]
	