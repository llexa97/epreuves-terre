"""Créez un programme qui affiche si un nombre est premier ou pas.


Exemples d’utilisation :
$> node exo.js 5
Oui, 5 est un nombre premier.

$> node exo.js 6
Non, 6 n’est pas un nombre premier.

Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.
"""

import sys

args = sys.argv[1:]

if len(args) != 1 or not args[0].isdigit():
    print("erreur d'argument")
elif int(args[0]) < 0:
    print("l'argument doit être positif")
else:
    nb = int(args[0])
    if nb == 0 or nb == 1:
        print("le nombre n'est pas premier")
    else:
        i = 2
        while i < nb:
            if nb % i == 0:
                print("le nombre n'est pas premier")
                break
            i += 1
        else:
            print("le nombre est premier")