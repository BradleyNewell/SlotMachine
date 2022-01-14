import random 

class slot_Machine:


	def __init__(self):
		self.symbols = ['♦', '♠', '♣', '♥', '☻']

		self.row_1 = []
		self.row_2 = []
		self.row_3 = []
		self.row_4 = []
		self.row_5 = []

		self.outcome = [self.row_1, self.row_2, self.row_3, self.row_4, self.row_5]


	def spin_wheel(self):
		for i in range(5):
			for result in self.outcome:
				result.append(random.choice(self.symbols))


	def check_spin(self):
		winning_spin = all(element == self.row_3[0] for element in self.row_3)
		formatted_out = ""	
		if (winning_spin):
			print(f"\nYou win with {formatted_out.join(self.row_3)}")
		else:
			print("\nBetter luck next time")


	def show_spin(self):
		formatted_roll = ""
		for i in self.outcome:
			print(formatted_roll.join(i))



slots = slot_Machine()


slots.spin_wheel()
slots.show_spin()
slots.check_spin()
