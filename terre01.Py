"""Créez un programme qui affiche son nom de fichier.


Exemples d’utilisation :
$> node exo.js
exo.js

$> node crevette.js
crevette.js"""

import os

file = __file__

file_name = os.path.basename(file)

print(file_name)