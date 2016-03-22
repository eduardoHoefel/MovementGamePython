'''
Created on Mar 22, 2016

@author: eduardo
'''

from character import Character, BLUE, WHITE, BLACK

POS_X = 19
POS_Y = 8

SYMBOLS = {}
SYMBOLS[WHITE] = Character('@', fgColor=BLUE, bgColor=WHITE, bold=True)
SYMBOLS[BLACK] = Character('@', fgColor=BLUE, bgColor=BLACK, bold=True)

def getSymbolWithBackground(color):
	return SYMBOLS[color]
