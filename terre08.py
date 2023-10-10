"""Créez un programme qui affiche le résultat d’une puissance.


L’exposant ne pourra pas être négatif.


Exemples d’utilisation :
$> node exo.js 2 3
8

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.


Fonctions interdites: 
-La fonction pow"""

import sys

args = sys.argv[1:]

if len(args) < 2 or args == []:
    print("erreur.")
elif int(args[1]) < 0:
    print("erreur.")
else :
    a = int(args[0])
    b = int(args[1])
    resultat = a ** b 
    print(resultat)