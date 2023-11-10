import random
class Sudoku:

	# nb est le nombre de chiffres donnés au départ
	def __init__(self, nb):
		self.nb = nb
		# -1 veut dire que le coup n'est pas joué
		self.grille = [[-1 for i in range(10)] for j in range(10)]
		self.placeChiffre()

	def placeChiffre(self):
		for i in range(self.nb):
			# on cherche une case vide
			case = False
			while not case:
				col = random.randint(0, 9)
				lg = random.randint(0, 9)
				print(col,lg)
				if self.grille[lg][col] == -1:
					case = True
			# on place un chiffre au pif dans cette case
			c = random.randint(0, 9)
			self.grille[lg][col] = c


	def __str__(self):
		s = '--' * 20
		s += '\n'
		for i in self.grille:
			for j in i:
				s += "|   "if j == -1 else "| "+str(j)+" "
			s+="|\n"
			s += '--' * 20
			s += '\n'
		return s