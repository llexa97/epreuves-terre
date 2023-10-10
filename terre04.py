"""Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..


Exemples d’utilisation :
$> ruby exo.rb 2
pair

$> ruby exo.rb 5
impair


$> ruby exo.rb Bonjour
Tu ne me la mettras pas à l’envers.

$> ruby exo.rb
Tu ne me la mettras pas à l’envers.


Attention : gérez aussi les entiers négatifs.
"""

import sys

arg = sys.argv[1:2]

if arg == []:
    print("Tu ne me la mettras pas à l’envers.")
else:
    arg_value = arg[0]
    # print(arg_value)
    try:
        float(arg_value)
        if int(arg_value) % 2 == 0:
            print("pair")
        else:
            print("impair")
    except:
        print("Tu ne me la mettras pas à l’envers.")
        
        
    # if arg_value.isnumeric():
    #     if int(arg_value) % 2 == 0:
    #         print("pair")
    #     else:
    #         print("impair")
    # else: 
    #     print("Tu ne me la mettras pas à l’envers.")