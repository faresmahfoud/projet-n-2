import pickle
from random import randrange

def core():
	# load les anciens score si disponible
	try :
		f = open('score', 'rb')
		score = pickle.load(f)
		f.close()
	except :
		f = open('score', 'wb')
		f.close()
		score = {}

	# initialise les joueurs
	j = []
	j.append( input('Nom du joueur 1 :') )
	j.append( input('Nom du joueur 2 :') )

	# choisi un joueur au hasard pr commencer la partie
	tour = randrange(0,2)
	count = 0

	# initialise la planche de jeu
	tableau = [ [] for _ in range(randrange(3, 8)) ]
	for n, _ in enumerate(tableau) :
		tableau[n] = randrange(5, 24)
	affiche(tableau)

	# la partie en elle meme
	while sum(tableau) > 0 :
		A = input(j[tour]+' veuillez entrer votre coups :').split('-')
		ligne   = eval( A[0] )
		retirer = eval( A[1] )

		tableau[ ligne-1 ] -= retirer
		affiche(tableau)

		tour  = (tour + 1) % 2
		count += 1

	# calcule des point gagner
	point = 0
	for i in range(1, count+1) :
		point += i*10**i 
	
	# lise a jour des score
	maj_imprime(j[tour] , j[ (tour + 1) % 2 ] , point, score)

	# rejouer
	if input("Pour rejouez, entrer 'oui' :") == "oui" :
		core()

def maj_imprime(g, p, point, score):
	# met a jour les score et les enregistre dans le fichier score

	if g in score :
		score[g] = [ min(point, score[g][0] ), point ]
	else :
		score[g] = [ point, point ]

	if p in score :
		score[p][1] = float('inf')
	else :
		score[p] = [ float('inf'), float('inf') ]

	# print les 10 meilleurs score en ordre croissant (le plus petit est le meilleur)

	L = sorted( score.items(), key = lambda x: x[1][0] )
	for j in range( min(len(L), 10) ) :
		print( L[j][0], ':', L[j][1][0] )

	f = open('score', 'wb')
	pickle.dump(score, f)
	f.close()

def affiche(tableau):
	# print les tas a chaque tour du jeu
	L, c = max(tableau), 1

	for t in tableau :
		print( c, '|', '*'*t, ' '*(L-t), '|', t )
		c += 1
core()
