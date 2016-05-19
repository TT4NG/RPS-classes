
class Choice:
	def __init__(self):
		self.guess = None
		self.usernum = 0
	def guess(self):
		guess = input("Choose 'rock', 'paper', 'scissors', 'lizard', 'spock' by typing the word: ")
		if Choice.valid(self, guess):
			print(guess)
			if guess == 'rock':
				usernum = 1
			elif guess == 'paper':
				usernum = 2
			elif guess == 'scissors':
				usernum = 3
			elif guess == 'lizard':
				usernum = 4
			elif guess == 'spock':
				usernum = 5
			self.usernum = usernum
		else:
			print("Invalid choice")
			return Choice.guess(self)
			
	def valid(self, guess):
		if guess in ('rock', 'paper', 'scissors', 'lizard', 'spock'):
			status = True
		else:
			status = False
		return status