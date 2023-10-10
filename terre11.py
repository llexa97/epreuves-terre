"""Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.


Exemples d’utilisation :
$> ruby exo.rb 23:40
11:40PM

Attention : midi et minuit.
"""

import sys

args = sys.argv[1:]

hh = args[0][:2]
mm = args[0][3:]

if hh.isdigit() and mm.isdigit():
    hh = int(hh)
    mm = int(mm)
    if hh < 0 or hh > 23 or mm < 0 or mm > 59:
        print("erreur")
    else:
        if hh == 0:
            print(f"12:{mm}AM")
        elif hh == 12:
            print(f"12:{mm}PM")
        elif hh < 12:
            print(f"{hh}:{mm}AM")
        else:
            print(f"{hh - 12}:{mm}PM")