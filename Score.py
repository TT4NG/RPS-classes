
class Score:
	def __init__(self, player1, player2, ai):
		self.player1 = player1
		self.player2 = player2
		self.ai = ai
		self.win = 0
		self.tie = 0
		self.loss = 0

	def results(self, compnum, player1, name, win, loss, tie):
		difference = compnum - player1
		if difference == 0:
			print ("Tie")
			self.tie += 1
		elif difference % 5 == 2 or difference % 5 == 4:
			print ("Sorry ", name, " you lose.")
			self.loss += 1
		elif difference % 5 == 3 or difference % 5 == 1:
			print ("Congratulation", name, " you win!")
			self.win += 1
		
	def results2(self, player2, player1, name1, name2, win, loss, tie):
		difference = player2 - player1
		if difference == 0:
			print ("Tie")
			self.tie += 1
		elif difference % 5 == 2 or difference % 5 == 4:
			print ("Congratulations", name2, " you win!")
			self.loss += 1
		elif difference % 5 == 3 or difference % 5 == 1:
			print ("Congratulations", name1," you win!")
			self.win += 1
