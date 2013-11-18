#!/usr/bin/env python3
import random, time
def ceelofunc1():	
	ceelo1 = random.randint(1,6)
	ceelo2 = random.randint(1,6)
	ceelo3 = random.randint(1,6)
	ce = [ceelo1,ceelo2,ceelo3]
	index = 0
	while index < len(ce):       #converts each element into integer.
		ce[index] = int(ce[index])
		index += 1 
	ce.sort()            
	print('the 1st user rolled', (ce))
	calcWinner(ce)
	autowin = [4,5,6]
	checkAutowin1(autowin,ce)
	reroll1(autowin,ce)
	if ce != autowin:	
		ceelofunc2(ce)
		
		
##still need to add something about [1,2,3] being auto-lose	
	
	
	
def checkAutowin1(autowin,ce):
	if ce == autowin:
		print('user 1 autowins')
	return ce
	
def reroll1(autowin,ce):
	while ce[0] != ce[1] and ce[1] != ce[2] and ce != autowin:
		print('re-rolling')
		#time.sleep(2)
		ceelo1 = random.randint(1,6)
		ceelo2 = random.randint(1,6)
		ceelo3 = random.randint(1,6)
		ce = [ceelo1,ceelo2,ceelo3]
		index = 0
		while index < len(ce):       #converts each element into integer.
			ce[index] = int(ce[index])
			index += 1 
		ce.sort()
		print('the 1st user rolled', (ce))
		if ce == autowin:
			print('user 1 autowins')         
		calcWinner(ce)
			


def ceelofunc2(ce):
	ceelo4 = random.randint(1,6)
	ceelo5 = random.randint(1,6)
	ceelo6 = random.randint(1,6)
	ce2 = [ceelo4,ceelo5,ceelo6]
	index = 0
	while index < len(ce2):
		ce2[index] = int(ce2[index])
		index += 1
	ce2.sort()
	print('the 2nd user rolled', (ce2))
	autowin2 = [4,5,6]
	checkAutowin2(autowin2,ce2)
	reroll2(autowin2,ce2,ce)
	calcWinner2(ce2,ce)

	
	
	
	
def checkAutowin2(autowin2,ce2):
	if ce2 == autowin2:
		print('user 2 autowins!')
	return ce2
		
def reroll2(autowin2,ce2,ce):
	while ce2[0] != ce2[1] and ce2[1] != ce2[2] and ce2 != autowin2:
		print('re-rolling')
		#time.sleep(2)
		ceelo4 = random.randint(1,6)
		ceelo5 = random.randint(1,6)
		ceelo6 = random.randint(1,6)
		ce2 = [ceelo4,ceelo5,ceelo6]
		index = 0
		while index < len(ce2):
			ce2[index] = int(ce2[index])
			index += 1
		ce2.sort()
		print('the 2nd user rolled', (ce2))
		if ce2 == autowin2:
			print('user 2 autowins!')
		calcWinner2(ce2,ce)
	#return ce2			

		
		
	



def calcWinner(ce):
	if ce[0] == ce[1] and ce[0] != ce[2]:
		print('user 1 rolled', ce[2])
	elif ce[0] == ce[1] and ce[0] == ce[2]:
		print('user 1 rolled trip', ce[2], 's')
	elif ce[1] == ce[2] and ce[0] != ce[2]:
		print('user 1 rolled', ce[0])

		
def calcWinner2(ce2,ce):
	if ce2[0] == ce2[1] and ce2[0] != ce2[2]:
		print('user 2 rolled', ce2[2])
	elif ce2[0] == ce2[1] and ce2[0] == ce2[2]:
		print('user 2 rolled trip', ce2[2], 's')
	elif ce2[1] == ce2[2] and ce2[0] != ce2[2]:
		print('user 2 rolled', ce2[0])



ceelofunc1()
