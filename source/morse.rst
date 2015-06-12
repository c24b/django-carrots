Essayons maintenant de créer un programme simple qui affiche du Morse

# Exercice de Morse

En cas d'urgence et de panique liée à cet ordinateur, vous pouvez avoir besoin d'envoyer un signal de détresse.
Le signal de détresse, S.O.S. (Save Our Soul) est en effet le signal le plus connu pour communiquer sa position critique par la lumière ou par le son.

Elle est utilisé par les bateaux et par les naufragés elle passe par la lumière ou le son, elle permet aussi d'identifier les phares des cotes.

Nous nous allons pour notre part commencer à afficher des signaux morse depuis le terminal. En commencant par notre fameux signal de détresse SOS.

Pour écrire un SOS en morse:
S.O.S va se traduire en morse par :
	(... --- ...)
	soit 3 signaux courts 3 signaux longs

Le S est donc égal à "..." et le O à "---"

Vous connaissez déjà la fonction print().



Nous allons donc créer un *__programme__* 
qui stocke les deux lettres et leur equivalent en morse dans des *__variables__*.

Une *__variable__* est une boite dans laquelle on stocke une référence à une valeur (entier, chaine de caractère ou résultat d'un calcul).

Un programme est simplement une liste d'instruction écrites les unes à la suite des autres 
dans un autre logique et en suivant un langage particulier (ici Python3) 
qui suit une syntaxe, un vocabulaire et une grammaire.



###Variables

Tout d'abord ouvrons un nouveau fichier et enregistrons-le sous le nom morse.py.
Nous assignons deux *__variables__* 
ici: s et o

``` python
	s = "..."
	o = "---"
	print(s+o+s)
``` 
Les variables sont des boites dans lequel on stocke *la référence* à une valeur.

S renvoie à la référence "..." .

Assignons donc une variable signal composé de nos lettres de morse

``` python
	s = "..."
	o = "---"
	mot = s+o+s
	print mot
``` 

La variable signal est donc une composition de deux variables s et o. 
Mais attention Python stocke dans la variable une **référence** à une valeur(chaine de caractère, entier,etc...)
et non pas **la valeur** elle même. Ce qui peut poser parfois des problèmes.
Démonstration:

``` python
	s = "..."
	o = "---"
	mot = s+o+s
	# Je change la référence de la valeur
	s = "000"
	print (mot)
```
Ouuuups! Que s'est-it passé? 

Réessayons maitenant:

``` python
	s = "..."
	o = "---"
	mot = s+o+s
	#Je réassigne ma variable mot
	mot = s+o+s
	print (mot)
```
Conclusion il faut juste faire attention à ce détail 
quand on change ces variables.

Commentons ce code en utilisant # au début de la ligne
Cela permet de dire au programme "ne l'execute pas"

	
Reprenons donc notre première version du code.
Nous allons créer une nouvelle variable dans notre programme: 
la variable stop qui permet de découper les mots 
et qu'on va représenter par un caractère "|".

``` python
	s = "..."
	o = "---"
	stop = "|"
	mot = s+o+s
	
	print (mot)+(stop)
```
### Les types de variables	
Python comprend les différent **types** de valeurs qu'on lui donne, il sait reconnaitre un caractère d'un entier, il en existe pleins.
Mais les plus importants qu'on va manipuler dans ce tutoriel sont les suivants


|   					| 	 		| 	 	|
| :-------------------------| :-----------:	| :-----------	|
| un nombre entier 			| 	`int`  		| 	3			|
| une chaine de caractères	| `str`  		| "sos" 		|
| un nombre décimal			| `float` 		|1.63 			|
|							| 				|  				|
|un booléen 				|`bool` 		|True/False		|
| un liste |`list` |```["carottes", 1, "bananes", True, 3]``` |
| un dictionnaire |`dict`|```{"nom":"Morse", "prénom": "Marc", "age": 27, "taille": 1.63}```|



Rassurez vous pour l'instant nous manipulons des chaine de caractères pour former un signal. La chaine de caractère
est indiquée par " "

On peut vérifier à tout moment que la variable signal est bien une chaine de caractère avec la fonction
```type()```


``` python
	print(type(signal))
```
Python est sympa et vous permet aussi d'avoir une aide à tout moment avec la fonction

``` python
	help(print)
```
	


###Fonctions

Si on veut la réutiliser et éviter de taper à chaque fois les mêmes instructions, il vaut mieux les enregistrer dans une *__fonction__*.

Une fonction c'est un mini moteur, une instruction simple qui 
prend une donnée en entrée exécute l'instruction (calcule) 
et renvoie la réponse en sortie.
En python on définit une fonction ``` def ma_fonction()``` 

Notre première fonction va se contenter d'imprimer notre signal de détresse. On crée donc la fonction et on l'appelle à la fin du fichier.

``` python

	def print_sos():
		s = "..."
		o = "---"
		print s+o+s
		return
	print_sos()
```

Nous avons maintenant une fonction toute simple qu'on peux appeler à plusieurs reprises.

On va essayer maintenant modifier cette fonction.

Si on est malin on peut encore simplifier le code et réduire le signal au mininum. 
si on considère que la variable s est égale à trois points 
et la variable o égale à trois tirets.




```
	def print_sos(nb):
		s = "." * 3
		o = "-" * 3
		stop = "|"
		mot = s+o+s
		print (mot+stop) * nb
```	
	

Si on voulait l'exécuter plusieurs fois, on peut imprimer autant de fois print_sos à la fin du fichier. Mais les informaticiens sont flemmards et la machine est là 
pour nous éviter de refaire la même chose.

On a besoin de dire à la machine combien de fois on veut imprimer notre SOS.
On va donc étendre la fonction et lui donner le nombre de fois où l'on veut imprimer le signal.


```
	def print_sos(nb):
		s = "..."
		o = "---"
		stop = "|"
		mot = s+o+s
		print (mot+stop) * nb
		return
		
	print_sos(26)
```


On a donc une fonction qui prend en entrée le nombre de fois où l'on veut emettre le signal SOS, pour l'instant elle ne se contente que d'afficher.

Si on veut rendre ce programme encore plus facile à utiliser et pouvoir utiliser
imaginons par exemple que nous avons un robot qui transforme le . et le - en sons différents, 
ou une machine qui allume et éteigne une lampe plus ou moins longtemps.
On peut vouloir juste que cette fonction emette le signal SOS sans l'imprimer dans le terminal. 
On va donc demander à la fonction de la retourner et donc on va changer le nom de la fonction de print à emit.

```
	def emit_sos(nb):
		s = "..."
		o = "---"
		stop = "|"
		mot = s+o+s
		return (mot+stop) * nb
		
	emit_sos(26)
```


Rassurez vous on peut toujours le demander de l'imprimer dans le terminal pour vérifier que cela marche

```
	def emit_sos(nb):
		s = "..."
		o = "---"
		return (s+o+s+"\n") * nb
		
	print(emit_sos(26))
```

On a donc une fonction utilisable ici on lui a greffé la fonction print à l'exterieur pour la visualiser dans le terminal.
mais on pourrait faire autre chose par exemple la jouer en son et créer une fonction play au lieu de print.

```
	play(emit_sos(26))
```

<!---
Cet fonction n'existe pas encore dans Python, nous allons la créer mais avant cela nous avons besoin d'être sur que notre ordinateur peut faire du son avec Python

### Activer le son

## Sur Windows
Pour Windows on va utiliser une bibliothèque (library). Comprenez par là que quelqu'un à déjà fait le travail pour nous
et à fait un ensemble de programme disponible en l'important simplement.
Ici la bibliothèque pour faire du son s'appelle windsound 
On la met dans notre programme en l'important avec l'instruction import:
```
	
	import winsound
	
```
Normalement la fonction help(windsound) nous explique comment s'en servir.

## Sur MacOS X
## Sur Linux (Debian)

Téléchargez
Tout d'abord, il nous faut vérifier que les alertes sont bien activés.

Dans le terminal tapez:
``` bash
	$user@ordi:~ echo -e "\a"
```
Si vous n entendez rien, il nous faut l'activer:

* Mode graphique
 Paramêtres Systèmes >> Son >> Effets sonores >> Décochez "couper le son" et vérifiez le volume
* Mode commande
	``` bash
		$user@ordi:~ sudo modprobe pcspkr

	```
Si par malheur ca ne marchait toujours pas regardez donc par ici
	http://superuser.com/questions/22767/enable-system-beep-in-ubuntu
	
Nous allons ensuite installer un module simple
``` bash
	$user@ordi:~ sudo apt-get install beep
```
Pour Linux nous allons télécharger une bibliothèque (library) ici 
et l'enregistrer sous '''windsound''' dans notre dossier de travail.

```	
	import winsound
```



###Conditions
Ouf! Maintenant nous allons créer une nouvelle fonction qui plutot que d'imprimer des points et des traits 
emette un son sourt pour le "." et un son long pour "-" et un temps de silence pour découper les mots. 


On va donc d'abord créer une nouvelle fonction qui prend un signal en entrée : un point ou un tiret et renvoie un son.

Pour savoir si c'est un point ou un tiret on va utilise des conditions si ```if``` alors sinon ```else```. 
Quand on a plusieurs conditions on ajoute elif. Ici on a donc 2 conditions: (un . ou un -)



```
	
	import winsound
	
	bip_long = winsound.Beep(100,2000)
	bip_court = winsound.Beep(100,200)
	
	def convert_signal(signal):
		if signal == ".":
			return bip_court
		else:
			return bip_long
	
	convert_signal(".")
	
```		
 On va d'abord tester que cela marche avec un seul signal et qu'il convertit bien le point en un bip court
 Evidemment si ca marche on pourrait encore se répeter et reproduire le SOS
en faisant
```
	convert_signal(".")
	convert_signal(".")
	convert_signal(".")
	convert_signal("-")
	convert_signal("-")
	convert_signal("-")
	convert_signal(".")
	convert_signal(".")
	convert_signal(".")
	
	
```
-->
Mais ca m'ennuye rien que de l'écrire et on est bien plus malin que ça en fait. En plus on a déjà ecrit une fonction qui compose le sos
en lui donnant le nombre de fois ou emettre le signal. 

#String and lists
Ce signal est composé de caractères à la chaine "string", c'est à dire des caractères stockées les à la suite les uns des autres.
Il est stocké dans ce qu'on appelle une liste. Regardons attentivement on peut accéder à chacun des caractères par numéro:
sos = "...---..."
Je veux le 1er caractère du sos (Attention en informatique c'est comme pour les ascenseurs on commence par 0):
```
	#Premiere caractère
	print sos[0]
	#
	print sos[1]
	#dernier caractere
	print sos[-1]
	#avant dernier caractere
	print sos[-2]
```
En python on utilise les listes pour stocker des informations à la suite les unes des autres.
```
	#liste des activités
	activites = ["lire", "ecrire", "compter", "rêver", "se promener", "rire", "chanter"]
	#On y accede de la même manière
	activites[0]
	activites[1]
	activites[-1]
	activites[0:2]
	...
```
Toujours pour moins se fatiguer on peut appliquer une même instruction à cette liste en la déroulant on parle de boucle et elle s'écrit for en python:
Un exemple plus parlant: pour chaque activité de ma liste je vais ajouter "Je veux" et le nom de l'activité
	```
		#liste des activités
		activites = ["lire", "ecrire", "compter", "rêver", "se promener", "rire", "chanter"]
		for a in activites:
			print ("Je veux "+ a)
	```


On peut évidemment apppliquer d'autres instructions plus compliquées et des conditions aussi variées qu'inutiles ici. 
	```
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
	```

#Back to SOS playsound function
Mais revenons plutôt à notre SOS.
On a d'un coté une fonction qui écrit le SOS en morse et de l'autre une fonction qui prend un element de la chaine de caractère et transforme le caractère en signal sonore.

C'est parti on va donc écrire notre fonction play : pour chaque élément de ma chaine de caractère la machine va emettre un son.
	```
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
	```
Ahaha mais on a un petit problème! Notre signal stop s'affiche mais on ne peux pas distinguer si on est au premier ou au deuxième SOS.
Si je demande d'emettre 3 fois le SOS, c'est de la bouillie que je vais entendre
	```
	for signal in emit_sos(3):
		convert_signal(signal)
	```
Il faut donc qu'on reprenne notre petit programme convert_signal pour lui ajouter une condition quand il stoppe. Ici on va le faire attendre en silence pendant 1 minute.
On va donc importer le module time. Pour le faire attendre on lui dit sleep()

	```
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
	```

Voila nous avons donc un programme complet pour appeler à l'aide depuis notre ordinateur:

	```
	
	
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
	
	```	
#STRING TO SOUND MORSE Functions
Maintenant à vous de jouer nous allons créer un programme qui convertit tous  les nombres et toutes les lettres de l'alphabet en morse
et ensuite nous les feront jouer par l'ordinateur. Pour stocker ces informations on va utiliser un autre systeme de stockage (un type particulier)
qu'on appelle le dictionnaire. Ca tombe bien c'est dictionnaire morse/français que nous allons créer.
Un dictionnaire prend la forme {clé: valeur}. A la différence de la liste ou de la chaine de caractère, chaque clé est unique.
Pour ne pas vous barber vous aller copier/coller le 2 dictionnaire alphabet_m dans un nouveau fichier  play_morse.py

```	
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

```






