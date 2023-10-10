"""Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.


Exemples d’utilisation :
$> node exo.js “Hello world!”
!dlrow olleH


$> node exo.js “lehciM”
Michel

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.


Fonctions interdites: 
-La fonction reverse"""

import sys 


args = "".join(sys.argv[1:])


def invert():
    inverted_str = ""
    for item in args[::-1]:
        inverted_str = inverted_str + item
    return print(inverted_str)


if len(args) < 1:
    print("Tu ne te moquerais pas de moi ?")
else:
    invert()