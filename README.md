# Description
Auto FTP uploader est un petit script réalisé en Python permettant de téléverser vers un endroit précis d'un serveur FTP
de façon semi-automatique tous les fichiers d'un dossier donné respectant des critères spécifiques tels que l'extension
ou si ce dernier commence par un charactère "banni" (ex: `.`, `-`).

Le programme ayant été premièrement conçu pour téléverser des plugins skript de l'ordinateur de l'utilisateur
au SFTP de son serveurs Minecraft il se peut qu'il soit nécésaire de effecturer des modifications.

Ce programme a été testé et ne devrait (sans modification) fonctionner que sur Windows. Vous avez a votre
disposition sa version compilée (.exe) ou non compilée (.py) notez néamoins que pour utiliser la version non
compilée vous aurez besoin d'installer les librairies citées dans la catégorie `Bilbiotèques utilisées`.
Le programme utilise la liscence MIT, réfférez-vous a la partie `Liscence` pour plus d'information.

# Installation & configuration
Dans cette section serra expliqué comment installer et configurer le programme


1. Executez fichier dans le dossier que vous shouaitez (il est recommandé d'utiliser celui ou se trouvent les fichiers a téléverser)
2. Un message devrait apparaitre, appuiez sur OK
3. Patientez quelques secondes puis une fenêtre devrait s'ouvrir (notepad.exe) avec un fichier nommé `appdata.json` et du texte JSON
4. Configurer ce fichier en vous réfférant a la partie `Configuration`
5. Une fois terminé, sauvegardez en via`Ctrl + S` puis fermez notepad.exe
6. Vérifiez que le programme est fermé puis re-lancez le, si vous rencontrez des erreurs vérifiez
le contenu du fichier `appdata.json` en l'ouvrant avec l'éditeur de texte de votre choix, pensez a sauvegarder.

## Configuration de `appdata.json`
Voici comment remplir ce fichier JSON :

Les informations d'identification (S)FTP doivent être fournies dans la section "credentials".
Vous devez remplir les champs "host", "username" et "password" avec les informations d'identification de votre compte FTP.

Les répertoires cibles doivent être définis dans la section "directories".
Vous devez remplir les champs "targetDirectory" et "homeDirectory" avec les chemins d'accès complets
des répertoires cibles sur le serveur FTP et sur votre ordinateur local, respectivement.

Dans la section "misc", vous pouvez spécifier les extensions de fichiers a inclure lors de la copie
en utilisant la liste blanche des extensions de fichiers. Dans le fichier par défaut, seul les fichiers avec l'extension ".sk" sont autorisés.

**N'oubliez pas que les fichiers JSON doivent être bien formatés et doivent contenir des crochets, accolades et virgules dans les endroits appropriés pour être valides.**

# Résolution des problèmes
Si jamais vous rencontrez un problème lors de l'utilisation du programme, voici plusieurs pistes pour tenter de le résoudre:

-Vérifiez si il n'y a pas d'erreurs dans le fichier `appdata.json`, cela peut être une virgule oubliée, un crochet non fermé etc.
-Vérifiez les informations dans le fichier `appdata.json` telles que les innformations de conexion etc.
-Si vous utilisez la version non compilée, vérifiez que tous les dépendances dans la section `Bilbiotèques utilisées` sonts satisfaites.
*Si toute fois, après avoir bien vérifié une erreur survient, rendez-vous dans la catégorie `Issues` de ce repo github.

## Fonctionnement
Voici le fonctionnement simplifié du script:
1. Le script vérifie si le fichier de configuration `appdata.json` existe.
2. S'il n'existe pas, il génère un fichier et ouvre Notepad pour que l'utilisateur entre les informations requises.
3. Si le fichier existe, il charge les informations de connexion et tente de se connecter au serveur (S)FTP.
4. Le script récupère la liste de tous les fichiers du répertoire de travail qui répondent à certaines conditions.
5. Il télécharge chaque fichier vers le répertoire spécifié sur le serveur FTP.


## Bibliothèques utilisées

- `ftplib`: pour gérer la connexion FTP
- `os`: pour accéder au système de fichiers
- `json`: pour gérer le fichier de configuration
- `colorama`: pour fournir une sortie colorée dans la console

# License

MIT License

Copyright (c) 2023 jarvis09

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
