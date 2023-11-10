def play():
	pass

def playWithIA():
	pass

def main():
	print("1 : Générer une grille et jouer")
	print("2 : Générer une grille et voir sa correction")
	choice = int(input("Entrer votre choix"))
	if choice == 1 :
		play()
	else : 
		playWithIA()

if __name__ == '__main__':
	main()