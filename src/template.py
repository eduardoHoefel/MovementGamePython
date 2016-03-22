'''
Created on Mar 22, 2016

@author: eduardo
'''

class Template():
	
	chars = []
	
	def __init__(self, folder, name):
		import os
		with open(os.path.dirname(os.getcwd()) + '/res/' + folder + '/' + str(name), 'r') as f:
			self.chars = [[char for char in line.decode('utf-8')] for line in f]
			#---------------------------------------------------- for line in f:
				#----------------------------------- line = line.decode('utf-8')
				#--------------------------- charsLine = [char for char in line]
				#---------------------------------- self.chars.append(charsLine)
		print len(self.chars)
		print len(self.chars[0])


MAP_FOLDER = 'Maps'
MESSAGE_FOLDER = 'Messages'