import random
class AI:
	def __init__(self):
		self.compnum = 0
	def AIgen(self):
		compnum = random.randrange(1,6)
		if compnum == 1:
			print ("computer chooses Rock")
		elif compnum == 2:
			print ("computer chooses Paper")
		elif compnum == 3:
			print ("computer chooses Scissors")
		elif compnum == 4:
			print("computer chooses Lizard")
		elif compnum == 5:
			print("computer chooses Spock")
		self.compnum = compnum