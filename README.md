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

Pour faire fonctionner une machine ram complète, on utlise la fonction marche_ram. Cette fonction prend en argument une machine ram ainsi que le mot stocké dans registre['i1'].