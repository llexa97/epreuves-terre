"""Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.


Exemples d’utilisation :
$> python exo.py 5 2
résultat: 2
reste: 1


$> python exo.py 10 0
erreur.


$> python exo.py 3 5
erreur.
"""

import sys

args = sys.argv[1:]
a = int(args[0])
b = int(args[1])


if b == 0: 
    print("erreur on pas diviser par 0 !")

elif b > a: 
    print("erreur !")

else:
    resultat = a//b
    reste = a%b 
    print(f"résultat: {resultat}\nreste: {reste}")