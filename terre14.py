"""Créez un programme qui détermine si une liste d’entiers est triée ou pas.


Exemples d’utilisation :
$> ruby exo.rb 9 8 3
Pas triée !

$> ruby exo.rb 3 8 9 12
Triée !

$> ruby exo.rb “Salut”
erreur.


Fonctions interdites: 
-La fonction sort"""

import sys

args = sys.argv[1:]

def is_sorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

if len(args) == 0:
    print("erreur")
else:
    sort = is_sorted(args)
    if sort == True:
        print("Triée !")
    else:
        print("Pas triée !")