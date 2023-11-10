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
			# en checkant possible ligne et colonne
			val = random.randint(0, 9)
			while  not self.checkChiffrePossible(val, col, lg):
				val = random.randint(0, 9)
			self.grille[lg][col] = val

	def checkChiffrePossible(self, val, col, lg):
		# ligne
		for i in self.grille[lg]:
			if i != col and self.grille[lg][i] == val:
				return False
		# colonne
		for i in self.grille:
			if i != lg and i[col] == val:
				return False
		# carré
		if lg < 3:
			if col < 3:
				return self.checkSquare(0,0,val,lg,col)
			elif col < 6:
				return self.checkSquare(0,3,val,lg,col)
			else:
				return self.checkSquare(0,6,val,lg,col)
		elif lg < 6:
			if col < 3:
				return self.checkSquare(3,0,val,lg,col)
			elif col < 6:
				return self.checkSquare(3,0,val,lg,col)
			else:
				return self.checkSquare(3,0,val,lg,col)
		else:
			if col < 3:
				return self.checkSquare(6,0,val,lg,col)
			elif col < 6:
				return self.checkSquare(6,0,val,lg,col)
			else:
				return self.checkSquare(6,0,val,lg,col)
		return True

	def checkSquare(self,lg,col, val, valLg, valCol):
		for i in range(3):
			for j in range(3):
				if self.grille[lg+i][col+i] == val and lg+i != valLg and col+1 != valCol:
					return False
		return True


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