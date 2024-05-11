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

