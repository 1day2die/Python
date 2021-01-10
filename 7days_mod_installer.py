import os
import sys
import zipfile
import urllib
import urllib.request
import colorama
from colorama import Fore, Back, Style
import pyunpack
import progressbar


def enterpath():
    global home
    print("BITTE 7Days2Die Pfad eingeben!")
    print("z.b C:/Steam/steamapps/common/7 Days To Die")
    home=input("PFAD: ")
    print()

    if os.path.exists(home+"/7DaysToDie.exe"):
        os.system("cls")
        installMods()
    else:
        print("---")
        print("Der Pfad stimmt nicht! // 7Days nicht gefunden!")
        print("---")
        print()
        enterpath()

def installMods():
    global home
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
    print("7Days2Die wurde gefunden!")
    print("---")
    print("Grüße von 1Day2Die")
    input("Drücke -Enter- um das Modpack zu installieren")


    #home = os.path.join("D:\\", "Steam", "steamapps", "common", "7 Days To Die", "")

    n = 0
    old_Mods_folder_name = "old_Mods" + str(n)

    while os.path.exists(os.path.join(home, str(old_Mods_folder_name))):
        n += 1
        old_Mods_folder_name = "old_Mods" + str(n)
        #print(n)

    if os.path.exists(os.path.join(home, "Mods")):
        os.rename(os.path.join(home, "Mods"), os.path.join(home, str(old_Mods_folder_name)))
        os.mkdir(os.path.join(home, "Mods"))
        try:
            print(Fore.MAGENTA + "Downloading Modpack")
            urllib.request.urlretrieve("http://downloads.hafuga.de/7days/Mods.zip", os.path.join(home, "Mods", "") + "Mods.zip", show_progress)
        except Exception as e: print(e)

        try:
            pyunpack.Archive(os.path.join(home, "Mods", "") + "Mods.zip").extractall(os.path.join(home, "Mods"))
        except Exception as e: print(e)

        os.remove(os.path.join(home, "Mods", "") + "Mods.zip")

        print("")
        print(Fore.GREEN + "Mods sind Installiert!")
        print(Fore.CYAN + "Deine alten Mods findest du unter")
        print(home + old_Mods_folder_name)
        print("")
        print("")
        print(Back.GREEN, Fore.BLACK + "Den Server erreichst du unter:")
        print("193.26.159.126:26900")
        print(Style.RESET_ALL)

        input("Das Fenster kann geschlossen werden")



    else:
        os.mkdir(os.path.join(home, "Mods"))
        print(Fore.RED + "7Days2Die Mods Ordner nicht gefunden unter " + home)
        print()
        print(Fore.GREEN + "Mods ordner wurde erstellt. Bitte ENTER drücken oder Programm neustarten")
        installMods()


        print(Style.RESET_ALL)




enterpath()