"""Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.


Exemples d’utilisation :
$> python exo.py n
nopqrstuvwxyz
$>


Attention : votre programme devra utiliser une boucle."""


import sys

arg = sys.argv[1:2]
char_arg = "".join(arg)
unicode_value = ord(char_arg)

# print(unicode_value)

z = 123

for i in range(unicode_value, z):
    print(f"{chr(i)}\n")