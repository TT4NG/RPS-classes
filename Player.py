from Choice import Choice

class Player:
	def __init__(self,name):
		self.name = name
		self.choice = Choice()
	def getGuess(self):
		Choice.guess(self)
		self.choice.usernum