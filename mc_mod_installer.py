import os
import sys
import zipfile
import urllib
import urllib.request
import colorama
from colorama import Fore, Back, Style
import pyunpack
import progressbar


def installMods():
    global pbar
    pbar = None
    def show_progress(block_num, block_size, total_size):
        global pbar
        if pbar is None:
            pbar = progressbar.ProgressBar(maxval=total_size)
        total_size = total_size
        downloaded = block_num * block_size
        if downloaded < total_size:
            pbar.update(downloaded)
        else:
            pbar.finish()
            pbar = None


    colorama.init()

    print("Grüße von 1Day2Die")
    input("Drücke -Enter- um das Modpack zu installieren")


    home = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft", "")

    n = 0
    old_mods_folder_name = "old_mods" + str(n)

    while os.path.exists(os.path.join(home, str(old_mods_folder_name))):
        n += 1
        old_mods_folder_name = "old_mods" + str(n)
        #print(n)

    if os.path.exists(os.path.join(home, "mods")):
        os.rename(os.path.join(home, "mods"), os.path.join(home, str(old_mods_folder_name)))
        os.mkdir(os.path.join(home, "mods"))
        try:
            print(Fore.MAGENTA + "Downloading Modpack")
            urllib.request.urlretrieve("http://downloads.hafuga.de/minecraft/mods.zip", os.path.join(home, "mods", "") + "mods.zip", show_progress)
        except Exception as e: print(e)

        try:
            pyunpack.Archive(os.path.join(home, "mods", "") + "mods.zip").extractall(os.path.join(home, "mods"))
        except Exception as e: print(e)

        os.remove(os.path.join(home, "mods", "") + "mods.zip")

        print("")
        print(Fore.GREEN + "Mods sind Installiert!")
        print(Fore.CYAN + "Deine alten Mods findest du unter")
        print(home + old_mods_folder_name)
        print("")
        print("")
        print(Back.GREEN, Fore.BLACK + "Den Server erreichst du unter:")
        print("games.oesterland.de:25595")
        print(Style.RESET_ALL)

        input("Das Fenster kann geschlossen werden")



    else:
        print(Fore.RED + "Spigot Installation nicht gefunden unter " + home)
        print("Kein 'mods' Ordner vorhanden?")
        print(Style.RESET_ALL)



installMods()