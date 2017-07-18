class HangmanGame():

	def __init__(self, word, nlives):
		self.word = list(word)
		self.decoded_word = list('*'*len(word))
		self.nlives = nlives

	
	def start(self):
		# global decoded_word

		while self.decoded_word != self.word and self.nlives:
			guess = input('type a letter\n')

			self.decoded_word = [new if new == guess else old for (new,old) in zip(self.word, self.decoded_word)]

			print(self.decoded_word)

			#Decrement live counter
			if(guess not in self.word):
				self.nlives -= 1
				print("You have " + str(nlives) + " lives left")
				
			
		if(self.nlives):
			print("you won!")
		else:
			print("you lost!")

if __name__ == '__main__':
	HangmanGame("jornada", 5).start()