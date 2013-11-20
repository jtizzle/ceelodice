#!/usr/bin/env python3

import random, time
class Ceelo:
	def diceroll(self):
		self.ceelo1 = random.randint(1,6)
		self.ceelo2 = random.randint(1,6)
		self.ceelo3 = random.randint(1,6)
		self.ce = [self.ceelo1,self.ceelo2,self.ceelo3]
		self.index = 0
		while self.index < len(self.ce):
			self.ce[self.index] = int(self.ce[self.index])
			self.index += 1
		self.ce.sort()
		print('rolled', (self.ce))
		self.calcWinner() 
		self.autowin = [4,5,6]
		self.autolose = [1,2,3]
		self.checkAutoWinLose()
		self.reroll()
		
	def calcWinner(self):
		if self.ce[0] == self.ce[1] and self.ce[0] != self.ce[2]:
			print('user 1 rolled', self.ce[2])
		elif self.ce[0] == self.ce[1] and self.ce[0] == self.ce[2]:
			print('user 1 rolled trip', self.ce[2], 's')
		elif self.ce[1] == self.ce[2] and self.ce[0] != self.ce[2]:
			print('user 1 rolled', self.ce[0])
		
	def checkAutoWinLose(self):
		if self.ce == self.autowin:
			print('user 1 autowins')
		elif self.ce == self.autolose:
			print('user 1 autoloses')
		return self.ce
		
	def reroll(self):
		while self.ce[0] != self.ce[1] and self.ce[1] != self.ce[2] and self.ce != self.autowin and self.ce != self.autolose:
			print('re-rolling')
			#time.sleep(2)
			self.ceelo1 = random.randint(1,6)
			self.ceelo2 = random.randint(1,6)
			self.ceelo3 = random.randint(1,6)
			self.ce = [self.ceelo1,self.ceelo2,self.ceelo3]
			self.index = 0
			while self.index < len(self.ce):       #converts each element into integer.
				self.ce[self.index] = int(self.ce[self.index])
				self.index += 1 
			self.ce.sort()
			print('the 1st user rolled', (self.ce))
			if self.ce == self.autowin:
				print('user 1 autowins')
			elif self.ce == self.autolose:
				print('user 1 autoloses')         
			self.calcWinner()
		
		
		
me = Ceelo()  
me.diceroll()  
		
