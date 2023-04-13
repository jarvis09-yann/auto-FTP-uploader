from ftplib import FTP_TLS
import os
from os import listdir
from os.path import isfile, join
import ctypes
from colorama import Fore, Style, Back, just_fix_windows_console
import json
import time
just_fix_windows_console()
 

if not os.path.exists("appdata.json"):
    json_data = {
        "credentials": {
            "host": "HOST HERE (ex: ftp-example.org)",
            "username": "USERNAME_HERE",
            "password": "PASSWORD_HERE"
        },
        "directories": {
            "targetDirectory": "/plugins/Skript/scripts",
            "homeDirectory": "WORKING_DIRECTORY (where your stuff to upload is)"
        },
        "misc": [
            {
                "fileExtensionWhiteList": [
                    "sk"
                ]
            }
        ]
    }
    with open('appdata.json', 'w') as jsonMkFile:
        json.dump(json_data, jsonMkFile, indent=4)
    print(f"{Fore.BLACK}{Back.RED}×→ Un fichier de configuration a été généré, veuillez le configurer. Ce dernier va être généré et ouvert dans les prochaines secondes)", Style.RESET_ALL)
    time.sleep(3)
    os.system(rf"notepad  {os.getcwd()}\\appdata.json")
    input("Appuiez sur entrée pour fermer le programme...")
    exit()


else:
    print(Fore.YELLOW, f"{Style.DIM}→ Fichier de paramétrage détécté (appdata.json)", Style.RESET_ALL)

try:
    with open("appdata.json") as jsonFile:
        data = json.load(jsonFile)


    credentials = data["credentials"]
    directories = data["directories"]
    misc = data["misc"]


    HOST = credentials["host"]
    USERNAME = credentials["username"]
    PASSWORD = credentials["password"]
    TARGETDIR = directories["targetDirectory"]
    HOMEDIR = directories["homeDirectory"]
    FILEEXT = data['misc'][0]['fileExtensionWhiteList']
except Exception as error:
    print(Fore.BLACK, Back.RED,  f"ERREUR: {error}. Veuillez vérifier l'intégrité du fichier appdata.json", Style.RESET_ALL)
except KeyboardInterrupt:
    print(Fore.BLACK, Back.YELLOW,  f"KeyboardInterrupt: fermeture du programme.", Style.RESET_ALL)
    exit()

def connect():
    try:
        global ftp
        ftp = FTP_TLS(HOST)
        ftp.login(USERNAME, PASSWORD)
        ftp.prot_p()          # switch to secure data connection
        ftp.cwd(TARGETDIR)
        print(Fore.YELLOW, f"{Style.BRIGHT}→ Initialisation de la connexion: chemin d'accès défini sur .{TARGETDIR}. Chemin d'accès racine:\n {HOMEDIR}", Style.RESET_ALL)
        ftp.encoding = "utf-8"
    except Exception as error:
        print(Fore.BLACK, Back.RED,  f"ERREUR: {error}. Veuillez vérifier vos identifiants de connexion au serveur SFTP", Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.BLACK, Back.YELLOW,  f"KeyboardInterrupt: fermeture du programme.", Style.RESET_ALL)
        exit()

def getFiles():
    try:
        global activeFilesDir
        global activeFilesName
        activeFilesName = []
        activeFilesDir = []
        for f in listdir(HOMEDIR):
            fileDir = join(HOMEDIR, f)
            if isfile(fileDir):
                if f[0] == "-" or f.split(".")[1] not in FILEEXT:
                    continue
                activeFilesDir.append(fileDir)
                activeFilesName.append(f)
        print(Fore.MAGENTA,f"╔→ Début du Téléversement de {len(activeFilesName)} Fichier(s) en cours...", Style.RESET_ALL)
        print(Fore.GREEN, "║ ", Style.RESET_ALL)
    except Exception as error:
        print(Fore.BLACK, Back.RED,  f"ERREUR: {error}.", Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.BLACK, Back.YELLOW,  f"KeyboardInterrupt: fermeture du programme.", Style.RESET_ALL)
        exit()
def readFiles():
    try:
        for i in range(0, len(activeFilesName)):
            with open(activeFilesDir[i], "rb") as file:
                print(Fore.GREEN, f"╠→ Téléversement du fichier {activeFilesName[i]} terminé...", Style.RESET_ALL)
                uploadFile(f"STOR {activeFilesName[i]}", file)
        print(Fore.GREEN, "║ ", Style.RESET_ALL)
    except Exception as error:
        print(Fore.BLACK, Back.RED,  f"ERREUR: {error}.", Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.BLACK, Back.YELLOW,  f"KeyboardInterrupt: fermeture du programme.", Style.RESET_ALL)
        exit()

def uploadFile(name, content):
    try:
        ftp.storlines(name, content) 
    except Exception as error:
        print(Fore.BLACK, Back.RED,  f"ERREUR: {error}.", Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.BLACK, Back.YELLOW,  f"KeyboardInterrupt: fermeture du programme.", Style.RESET_ALL)
        exit()

if ctypes.windll.user32.MessageBoxW(0, "Voulez-vous téléverser les fichiers actifs ?", "Téléversement FTP", 1) == 1:
    print("""
          _    _ _______ ____     ______ _______ _____     _    _ _____  _      ____          _____  ______ _____  
     /\  | |  | |__   __/ __ \   |  ____|__   __|  __ \   | |  | |  __ \| |    / __ \   /\   |  __ \|  ____|  __ \ 
    /  \ | |  | |  | | | |  | |  | |__     | |  | |__) |  | |  | | |__) | |   | |  | | /  \  | |  | | |__  | |__) |
   / /\ \| |  | |  | | | |  | |  |  __|    | |  |  ___/   | |  | |  ___/| |   | |  | |/ /\ \ | |  | |  __| |  _  / 
  / ____ \ |__| |  | | | |__| |  | |       | |  | |       | |__| | |    | |___| |__| / ____ \| |__| | |____| | \ \ 
 /_/    \_\____/   |_|  \____/   |_|       |_|  |_|        \____/|_|    |______\____/_/    \_\_____/|______|_|  \_\ """,
"\n Par jarvis09\n")
    connect()
    getFiles()
    readFiles()
    print(Fore.CYAN,f"{Style.DIM}╚→ Téléversement terminé.", Style.RESET_ALL)
    input("")
else:
    exit()