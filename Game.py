from Player import Player
from AI import AI
from Score import Score

class Game:
	def __init__(self):
		self.player1 = None 				#set player1 and player2 slot up
		self.player2 = None
		self.ai = AI()
		self.score = Score(self.player1, self.player2, self.ai)
		self.win = 0
		self.loss = 0
		self.tie = 0
		
	def start(self):
		print ("Welcome to RPSLS, Lets Begin!")
		print ("Choose to face AI or Human")
		choice = input("1 for AI, 2 for Human: ")
		if choice == '1':
			self.player1 = self.getPlayer() #jump to getplayer function
			self.player1.getGuess()			#jump to get user pick function
			self.comp = self.getAI()		#jumps to getAI function
			self.player1.name
			self.end = self.score.results(self.player1.usernum, self.compnum, self.player1.name,self.win, self.loss, self.tie)
			self.score.win
			self.score.loss
			self.score.tie
			self.rest = self.restart(self.score.win, self.score.loss, self.score.tie)
			
		elif choice == '2':
			self.player1 = self.getPlayer() #jump to getplayer function
			self.player2 = self.getPlayer()
			print(self.player1.name , "'s turn")
			self.player1.getGuess()			#jump to get user pick function
			print(self.player2.name , "'s turn")
			self.player2.getGuess()	
			
			self.end = self.score.results2(self.player1.usernum, self.player2.usernum, self.player1.name, self.player2.name, self.win, self.loss, self.tie)
			self.score.win
			self.score.loss
			self.score.tie
			self.rest = self.restart(self.score.win, self.score.loss, self.score.tie)
		else:
			print("Invalid choice")
			return Game.start(self)			#returns to beginning of question
		
	def getPlayer(self):
		name = input("Enter a name: ")  	#ask for user input for name
		player = Player(name)				#jump to Player class and use name from previous line
		return player						#return player name into register 0
		
	def getAI(self):
		com = AI.AIgen(self)				#jumps to AI class and specifically AI gen function
		self.ai.compnum
	
	def restart(self, win, tie, loss):
		answer = input("would you like to play again? Y/N: ")
		print (answer)
		if answer.lower() == "y":
			Game.start(self)
		elif answer.lower() == "n":
			print("Goodbye.")
			print("Total Wins = ", win)
			print("Total Losses = ", loss)
			print("Total Ties = ", tie)
		else:
			print("Invalid, type Y or N")
			Game.restart()
	