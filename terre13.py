"""Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.


Exemples d’utilisation :
$> ruby exo.rb 11 40 34
34

$> ruby exo.rb 2 1 3
2

$> ruby exo.rb 2 2 2
erreur.


Fonctions interdites: 
-La fonction sort
"""

import sys

args = sys.argv[1:]
print(args)




def converter_int():
    a = int(args[0])
    b = int(args[1])
    c = int(args[2])
    args.clear()
    args.append(a)
    args.append(b)
    args.append(c)
    return args

def remove_list():
    converter_int()
    print(args)
    maxi = max(args)
    mini = min(args)
    
    args.remove(maxi)
    args.remove(mini)
    print(args)
    
    suisse = args[0]
    return print(suisse)

if len(args) != 3:
    print("erreur")
else:
    remove_list()