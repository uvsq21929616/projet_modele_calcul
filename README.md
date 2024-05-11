# Projet de Modèles de Calcul

## Projet - Métasimulation

### 1 - Simulation de l'exécution d'une machine RAM

Dans cette première partie, on a essayé de simuler l'exécution d'une machine RAM avec un programme Python. 

On a créé une classe RAM qui représente toutes les instructions d'une machine RAM vues dans le cours :
- ADD(i1, i2, i3) permet d'additionner le contenu de i1 et i2 et de stocker le résultat dans i3.
- SUB(i1, i2, i3) permet de soustraire le contenu de i1 et i2 et de stocker le résultat dans i3.
- MUL(i1, i2, i3) permet de multiplier le contenu de i1 et i2 et de stocker le résultat dans i3.
- DIV(i1, i2, i3) permet de diviser le contenu de i1 et i2 et de stocker le résultat dans i3.
- JE(i1, i2, z) permet de sauter z pas si la valeur de i1 est égale à la valeur de i2.
- JL(i1, i2, z) permet de sauter z pas si la valeur de i1 est plus grande que la valeur de i2.
- JUMP(z) permet de sauter z pas.
- terminé permet de terminer le programme de la machine RAM.

Le programme de la machine RAM est stocké dans un fichier .txt. Il est lu par la fonction read_programm(fichier, mot). Cette fonction ouvre le fichier et parcoure toutes ses lignes. Chaque ligne correspondant à une instruction, la fonction retire le symbole '\n' de la ligne et la stocke dans une liste appelée 'programme'. Cette fonctionprend également en argument un mot et initialise le registre de la machine ram sous forme d'un dictionnaire : la valeur de la clé 'i0' correspond à la position et la valeur de la clé 'i1' correspond au mot (s'il y a plusieurs mots, alors les valeurs des clés 'i1', 'i2', ... correspondent aux différents mots).

La machine ram est ensuite initialisée à partir de la classe RAM, qui prend en argument le programme et le registre de la machine et qui a pour attribut pos, qui correspond à la position dans la machine, registre, qui correspond au registre, et programme, qui correspond ç la liste des instructions.

Pour simuler l'avancée de la machine d'un seul pas, on utilise la fonction etape_suivante(ram, config) qui prend en argument une machine ram initialisée et une configuration [pos, registre]. La fonction remplace le registre de ram par le registre donné en argument et applique l'instruction à la position pos donnée en argument, puis renvoie le registre mis à jour de la machine ram.

Pour faire fonctionner une machine ram complète, on utlise la fonction marche_ram. Cette fonction prend en argument une machine ram ainsi que le mot stocké dans registre['i1']. Elle utilise une boucle infinie pour continuer à faire tourner toutes les instructions tant que l'instruction rencontrée n'est pas 'terminé', auquel cas la fonction s'arrête. 

### 2 - Machines RAM 

Nous avons trois exemples de machines RAM dans notre dossier.

La première est fichier.txt, qui est une machine RAM de test qui à chaque tour, ajoute 1 à i2 et divise i1 par 6. Cette machine se termine quand i2 est égal à 12.

La deuxième machine est machine_a_puissance_b.txt, qui prend en argument un nombre a et un nombre b, et calcule a puissance b.

La troisième machine est machine_tri_bulles.txt, qui prend en argument une liste de cinq chiffres et renvoie cette liste triée selon l'algorithme du tri à bulle. Nous avons choisi de programmer cette machine avec une liste de cinq chiffres, mais il est possible d'éteindre ou de restreindre la taille de la liste et de modifier la machine en conséquences.

### 3 - Comment faire rentrer la pile dans la RAM ?

Nous nous sommes ensuite penchés sur comment simuler un automate à pile avec une machine RAM.

Un automate à pile est représenté comme suit dans le registre : le nombre de ses transitions, puis pour chaque transition : l'état initial, la lettre lue, la lettre en haut de la pile, le symbole à rajouter sur la pile, l'état suivant.
Ici, nous avons choisi du à des problèmes d'implémentations de réduire nos automates à piles à des automates ne pouvant empiler ou dépiler qu'une seule lettre à chaque transition, mais il aurait fallu étendre notre implémentation à des automates ayant des transitions empilant ou dépilant plusieurs symboles à la fois.
Nos alphabets sont les suivants :
- L'alphabet de la pile est {0, 1, 2}.
  - 0 correspond au symbole de fond de la pile, ainsi qu'à ne rien empiler ou dépiler lors d'une transition.
  - 1 correspond à empiler un 1 sur la pile.
  - 2 correspond à dépiler un 1 sur la pile.
- Les états sont les suivants : (0, 1, 2, ...)
  - 0 est l'état initial.
  - 1 est l'état final.
  - 2, 3, ... sont les états intermédiaires.
- L'alphabet d'entrée est {0, 1}.

Nous avons créé une classe héritage RAM_AUTOMATE qui s'occupe d'un automate à pile simulé par une machine RAM.
Cette classe contient les fonctions suivantes : 
- FIND(i1, i2, i3) qui permet de trouver la transition de l'automate selon la valeur d'i1 (la première lettre du mot), i2 (la lettre de dessus de la pile) et i3 (l'état inital). 
- ADD(i2, i4, i4) qui récupère le symbole à empiler de i4 : s'il est égal à 1, la foncton ajouter 1 à la pile, s'il est égal à 2, elle dépile 1. Elle supprime aussi la première lettre de i1.
- JE(i1, i2, z) vérifie que i1 est i2 sont égaux et si c'est le cas, saute de z pas. sinon, elle avance de 1. La seule différence entre JE de RAM_AUTOMATE et JE de RAM est que la première compare des chaînes de caractères et la deuxième des entiers.
- nonreconnu renvoie que le mot n'est pas reconnu par l'automate.
- motreconnu renvoie que le mot est reconnu par l'automate.

Le programme et le registre sont initialisés par la fonction lire_automates(liste_transitions, mot, fichier). Cette fonction lit le fichier contenant le programme et le stocke dans une liste et initialise le registre avec 'i0' correspondant à la position et 'i1' correspondant au mot.
Elle ajoute ensuite la pile initialisée à 0 à 'i2', l'état actuel de l'automate initialisé à 0 à 'i3', le symbole à rajouter sur la pile initialisé à 0 à 'i4', l'état suivant initialisé à 0 à 'i5' et la taille de la liste des transitions à 'i6'.

On peut avancer la machine d'un pas de la même manière qu'on peut avancer d'un pas une machine RAM normale, avec la fonction etape_suivante.

On peut faire fonctionner l'automate à pile avec la fonction marche_automate(ram) qui prend en entrée la machine ram représentant l'automate initialisé.

### 4 - Reconnaitre 1^n0^n

On a pris l'automate à pile reconnaissant si un mot est égal à 1^n0^n. Cet automate contient cinq transitions:
- (0, 1, 0, 1, 0)
- (0, 1, 1, 1, 0)
- (0, 0, 1, 2, 2)
- (2, 0, 1, 2, 2)
- (2, 0, 0, 0, 1)


### 5 - Optimisation

On a ensuite voulu optimiser le code des machines ram en supprimant le code mort, ie le code qui n'est jamais accessible.

Pour cela, on a commencé par 