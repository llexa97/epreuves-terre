"""Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.


Exemples d’utilisation :
$> python exo.py “Hello world!”
12


$> python exo.py
erreur.


$> python exo.py “Bonjour” “Aurevoir”
erreur.

$> python exo.py 10
erreur.


Fonctions interdites: 
-La fonction length
-La fonction size
"""

import sys 

args = sys.argv[1:]

def numbers_of_letters():
    count = 0
    
    for _ in args[0]:
        count += 1
    return print(count)


if args == []:
    print("erreur.")
else:
    try:
        float(args[0])
        print("erreur.")
    except:
        numbers_of_letters()