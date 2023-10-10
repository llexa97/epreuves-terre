"""Créez un programme qui affiche la racine carrée d’un entier positif.


Exemples d’utilisation :
$> node exo.js 9
3

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.


Fonctions interdites: 
-La fonction sqrt"""

import sys

args = sys.argv[1:]

if len(args) != 1 or not args[0].isdigit():
    print("erreur")
elif int(args[0]) < 0:
    print("erreur")
else:
    print(int(args[0]) ** 0.5)
