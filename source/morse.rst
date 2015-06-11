# Morse Exercice

En cas d'urgence et de panique liée à cet ordinateur, vous pouvez avoir besoin d'envoyer un signal de détresse.
Le signal de détresse, SOS (Save Our Soul) est en effet le signal le plus connu pour communiquer sa position critique par la lumière ou par le son.
Elle est utilisé par les bateaux et par les naufragés elle passe par la lumière ou le son, elle permet aussi d'identifier les phares des cotes.
Nous nous allons pour notre part commencer à afficher des signaux morse depuis le terminal. En commencant par notre fameux signal de détresse SOS.

Pour écrire un SOS en morse:
S.O.S va se traduire en morse par (... --- ...) soit 3 signaux courts 3 signaux longs
Le S est donc égal à "..." et le O à "---"
 
Vous connaissez déjà la fonction print().
Nous allons donc créer un '''programme''' qui stocke les deux lettres et leur equivalent en morse dans des '''variables'''.

##Variables
Tout d'abord ouvrons un nouveau fichier et enregistrons-le  sous le nom morse.py
'''
s = "..."
o = "---"
print(s+o+s)
'''		

#Function
Si on veut la réutiliser et éviter de taper à chaque fois les mêmes instructions,il vaut mieux les enregistrer dans une fonction
Une fonction c'est un mini moteur, une instruction simple qui prend une donnée en entrée execute l'instruction (calcule) et renvoie la réponse.
En python on l'écrit def ma_fonction() on met les instructions à la luigne et on la ferme en lui  disant ce qu'elle retourne
Notre première fonction va se contenter d'imprimer notre signal de détresse. On crée donc la fonction et on l'appelle à la fin du fichier.

'''
	def print_sos():
		s = "..."
		o = "---"
		print s+o+s
		return
	print_sos()
'''

J'ai maintenant une fonction toute simple que je peux appeler à plusieurs reprises
Maintenant si on est malin on peut encore simplifier le code et réduire le signal au mininum. On peut aussi vouloir découper le signal et signifier que notre mot est terminé
On va donc ajouter une nouvelle variable "stop" pour découper le mot et ainsi savoir quand le mot est terminé.
'''
	def print_sos():
		s = "..."
		o = "---"
		stop = "|"
		print (s+o+s+stop)
		return
	print_sos()
'''


Mais on peut être encore plus malin
si on considère que s est égal à trois points et o égal à trois tirets. On peut parfaitement optimiser notre print_sos
	'''
	def print_sos(nb):
		s = "." * 3
		o = "-" * 3
		stop = "|"
		print (s+o+s+stop) * nb
	'''	
	

Si on voulait l'executer plusieurs fois, on peut imprimer autant de fois print_sos à la fin du fichier. Mais les informaticiens sont flemmards et la machine est là 
pour nous éviter de refaire la même chose et faire notre travail répétitif et ennuyeux.
On a besoin de dire à la machine combien de fois on veut imprimer notre SOS.
On va donc étendre la fonction et lui donner le nb de fois ou on veut imprimer le signal.

Pour qu'on puisse mieux lire les différents SOS et visualiser la fin de la phrase on va lui ajouter une nouvelle ligne. Et souvenez vous python est une super calculatrice capable de
multiplier du texte 

'''
	def print_sos(nb):
		s = "..."
		o = "---"
		print (s+o+s+"\n") * nb
		return
		
	print_sos(26)
'''

#Define a fonction and return
On a donc une fonction qui prend en entrée le nombre de fois où l'on veut emettre le signal SOS, pour l'instant elle ne se contente que d'afficher.
Si on veut rendre ce programme encore plus facile à utiliser, imaginons par exemple que nous avons un robot qui transforme le . et le - en sons différents, 
ou une machine qui allume et éteigne une lampe plus ou moins longtemps.
On peut vouloir juste que cette fonction emette le signal SOS sans l'imprimer dans le terminal. 
On va donc demander à la fonction de la retourner et donc on va changer le nom de la fonction de print à emit.

'''
	def emit_sos(nb):
		s = "..."
		o = "---"
		stop = "|"
		return (s+o+s+stop) * nb
		
	emit_sos(26)
'''

#Embedding functions 
Rassurez vous on peut toujours le demander de l'imprimer dans le terminal pour vérifier que cela marche
'''
	def emit_sos(nb):
		s = "..."
		o = "---"
		return (s+o+s+"\n") * nb
		
	print(emit_sos(26))
'''

On a donc une fonction utilisable ici on lui a greffé la fonction print à l'exterieur pour la visualiser dans le terminal.
mais on pourrait faire autre chose par exemple la jouer en son et créer une fonction play au lieu de print.
'''
	play(emit_sos(26))
'''
## Installation pour activer le son
##Sur windows
Pour Windows on va utiliser une mini librarie qui permet de faire du son sur l'ordinateur on l'appelle windsound 
et on la met dans notre programme en l'important avec l'instruction import:
'''
	
	import winsound
	
	bip_long = winsound.Beep(100,2000)
'''
## Sur MacOS X

## Sur Linux (Debian)
Pour Linux, s'assurer que le son des alertes est activé. Pour cela dans le terminal
taper echo -e '\a'
si rien ne se passe




télécharger ici hhtp://django-carrots-french.readthedocs.org/fr/latest/linux-windsound un petit utilitaire que nous allons enregistré dans notre repertoire de travail avec le nom windsound



#Conditions
Si on a le temps on peut créer une nouvelle fonction qui plutot que d'imprimer des points et des traits 
emette un son sourt pour le "." et un son long pour "-" et un temps de silence pour découper les mots. 
## Installation pour activer le son
##Sur windows
Pour Windows on va utiliser une mini librarie qui permet de faire du son sur l'ordinateur on l'appelle windsound 
et on la met dans notre programme en l'important avec l'instruction import:
'''
	
	import winsound
	
	bip_long = winsound.Beep(100,2000)
	bip_court = winsound.Beep(100,200)
	
	def convert_signal(signal):
		if signal == ".":
			return bip_court
		else:
			return bip_long
	
	convert_signal(".")
	
'''		

On va donc d'abord créer une nouvelle fonction qui prend un signal en entrée : un point ou un tiret et renvoie un son.

Pour savoir si c'est un point ou un tiret on va utilise des conditions si(if) alors sinon (else). 
Quand on a plusieurs conditions on ajoute elif. Ici on a donc 2 conditions: (un . ou un -)


'''
	
	import winsound
	
	bip_long = winsound.Beep(100,2000)
	bip_court = winsound.Beep(100,200)
	
	def convert_signal(signal):
		if signal == ".":
			return bip_court
		else:
			return bip_long
	
	convert_signal(".")
	
'''		
 On va d'abord tester que cela marche avec un seul signal et qu'il convertit bien le point en un bip court
 Evidemment si ca marche on pourrait encore se répeter et reproduire le SOS
en faisant
'''
	convert_signal(".")
	convert_signal(".")
	convert_signal(".")
	convert_signal("-")
	convert_signal("-")
	convert_signal("-")
	convert_signal(".")
	convert_signal(".")
	convert_signal(".")
	
	
'''
Mais ca m'ennuye rien que de l'écrire et on est bien plus malin que ça en fait. En plus on a déjà ecrit une fonction qui compose le sos
en lui donnant le nombre de fois ou emettre le signal. 

#String and lists
Ce signal est composé de caractères à la chaine "string", c'est à dire des caractères stockées les à la suite les uns des autres.
Il est stocké dans ce qu'on appelle une liste. Regardons attentivement on peut accéder à chacun des caractères par numéro:
sos = "...---..."
Je veux le 1er caractère du sos (Attention en informatique c'est comme pour les ascenseurs on commence par 0):
'''
	#Premiere caractère
	print sos[0]
	#
	print sos[1]
	#dernier caractere
	print sos[-1]
	#avant dernier caractere
	print sos[-2]
'''
En python on utilise les listes pour stocker des informations à la suite les unes des autres.
'''
	#liste des activités
	activites = ["lire", "ecrire", "compter", "rêver", "se promener", "rire", "chanter"]
	#On y accede de la même manière
	activites[0]
	activites[1]
	activites[-1]
	activites[0:2]
	...
'''
Toujours pour moins se fatiguer on peut appliquer une même instruction à cette liste en la déroulant on parle de boucle et elle s'écrit for en python:
Un exemple plus parlant: pour chaque activité de ma liste je vais ajouter "Je veux" et le nom de l'activité
	'''
		#liste des activités
		activites = ["lire", "ecrire", "compter", "rêver", "se promener", "rire", "chanter"]
		for a in activites:
			print ("Je veux "+ a)
	'''


On peut évidemment apppliquer d'autres instructions plus compliquées et des conditions aussi variées qu'inutiles ici. 
	'''
		#liste des activités
		activites = ["lire", "ecrire", "compter", "rêver", "se promener", "rire", "chanter"]
		for a in activites:
			
			if a == "rire":
				print ("Je veux VRAIMENT "+ a)
			elif a in ["lire", "ecrire", "compter"]:
				print ("Je ne veux pas" + a)
			elif a[0:1] == "se":
				a[0:1] = "me"
				
			else:
				print ("J'aime" + a)
	'''

#Back to SOS playsound function
Mais revenons plutôt à notre SOS.
On a d'un coté une fonction qui écrit le SOS en morse et de l'autre une fonction qui prend un element de la chaine de caractère et transforme le caractère en signal sonore.

C'est parti on va donc écrire notre fonction play : pour chaque élément de ma chaine de caractère la machine va emettre un son.
	'''
		Souvenez vous de comment on a construit le SOS c'est une suite de caractères
		sos = emit_sos(1)
		for signal in sos:
			convert_signal(signal)
	# A nous:
		def play(msg):
			for signal in msg:
				convert_signal(signal)
			return 
	#On a bien notre fonction:
	sos =  emit_sos(1)
	play(sos)			
	'''
Ahaha mais on a un petit problème! Notre signal stop s'affiche mais on ne peux pas distinguer si on est au premier ou au deuxième SOS.
Si je demande d'emettre 3 fois le SOS, c'est de la bouillie que je vais entendre
	'''
	for signal in emit_sos(3):
		convert_signal(signal)
	'''
Il faut donc qu'on reprenne notre petit programme convert_signal pour lui ajouter une condition quand il stoppe. Ici on va le faire attendre en silence pendant 1 minute.
On va donc importer le module time. Pour le faire attendre on lui dit sleep()

	'''
	import winsound
	import time
	
	bip_long = winsound.Beep(100,6000)
	bip_court = winsound.Beep(100,600)
	stop = time.sleep(60)
	def convert_signal(signal):
		if signal == ".":
			return bip_court
		elif signal == "-":
			big_long
		else:
			return stop
	'''

Voila nous avons donc un programme complet pour appeler à l'aide depuis notre ordinateur:

	'''
	
	
	def emit_sos(nb):
		s = "."*3
		o = "-"*3
		stop = "|"
		return (s+o+s+stop) * nb
	import winsound
	import time

	bip_long = winsound.Beep(100,2000)
	bip_court = winsound.Beep(100,200)
	stop = time.sleep(2000)
	
	
	def convert_signal(signal):
		if signal == ".":
			return bip_court
		elif signal == "-":
			big_long
		else:
			return stop
	
	'''	
#STRING TO SOUND MORSE Functions
Maintenant à vous de jouer nous allons créer un programme qui convertit tous  les nombres et toutes les lettres de l'alphabet en morse
et ensuite nous les feront jouer par l'ordinateur. Pour stocker ces informations on va utiliser un autre systeme de stockage (un type particulier)
qu'on appelle le dictionnaire. Ca tombe bien c'est dictionnaire morse/français que nous allons créer.
Un dictionnaire prend la forme {clé: valeur}. A la différence de la liste ou de la chaine de caractère, chaque clé est unique.
Pour ne pas vous barber vous aller copier/coller le 2 dictionnaire alphabet_m dans un nouveau fichier  play_morse.py
'''	
alphabet_m ={"a" : ".-",
			"b" : "-...",
			"c" : "-.-.",
			"d" : "-..",
			"e" : ".",
			"f" : "..-.",
			"g" : "--.",
			"h" : "....",
			"i" : "..",
			"j" : ".---",
			"k" : "-.-",
			"l" : ".-..",
			"m" : "--",
			"n" : "-.",
			"o" : "---",
			"p" : ".--.",
			"q" : "--.-",
			"r" : ".-.",
			"s" : "...",
			"t" : "-",
			"u" : "..-",
			"v" : "...-",
			"w" : ".--",
			"x" : "-..-",
			"y" : "-.--",
			"z" : "--..",
			"1":".----", 
			"2":"..---", 
			"3":"...--", 
			"4":"....-", 
			"5":".....",
            "6":"-....", 
            "7":"--...", 
            "8":"---..", 
            "9":"----.", 
            "0":"-----", 
            " ": "|" }

'''






