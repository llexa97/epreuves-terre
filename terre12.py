"""Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.


Exemples d’utilisation :
$> ruby exo.rb 11:40PM
23:40

Attention : midi et minuit.
"""

import sys

args = sys.argv[1:]

# print(args)

hh = args[0][:2]
mm = args[0][3:5]
ampm = args[0][5:]

if hh.isdigit() and mm.isdigit():
    hh = int(hh)
    mm = int(mm)
    
    if ampm == "AM":
        if hh == 12:
            print(f"{hh - 12}:{mm}")
        else:
            print(f"{hh}:{mm}")
    elif ampm == "PM":
        if hh == 12:
            print(f"{hh}:{mm}")
        else:
            print(f"{hh + 12}:{mm}")
    else:
        print("erreur.")

else: 
    print("erreur.")
    