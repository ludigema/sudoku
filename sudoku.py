class Sudoku:

	# nb est le nombre de chiffres donnés au départ
	def __init__(self, nb):
		self.nb = nb
		# -1 veut dire que le coup n'est pas joué
		self.grille = [[-1 for i in range(9)] for j in range(9)]

	def __str__(self):
		s = '';
		for i in self.grille:
			for j in i:
				s += "   "if j == -1 else " "+str(j)+" "
			s+="\n"
		return s