from PIL import Image, ImageFile
import os
import shutil
from colorama import Fore, Style
ImageFile.LOAD_TRUNCATED_IMAGES = True

def conversion(directory, format_entree, format_sortie, politique_backup):

    liste_conversion=[]
    nombre_convertit=0
    choix_backup=politique_backup
    if not(choix_backup == "K") and not(choix_backup == "R") and not(choix_backup == "C") :
        print(Fore.RED + "Merci de choisir une option valide concernant la politique de backup", "\n K : Always Keep \n R : Always Remove \n C : Custom")
        quit()
    backup=True

    for filename in os.listdir(directory): 
        extension=os.path.splitext(filename)
        if format_entree in extension[1]:
            liste_conversion.append(filename)

    if not(liste_conversion):
        print(Fore.YELLOW + f"Aucun fichier trouvé dans {directory} avec l'extension : {format_entree}")
    else:
        print(Fore.YELLOW + "Conversion en cours de", len(liste_conversion), f"fichiers dans {directory} dans le format {format_sortie}.")
        print(Style.RESET_ALL + "========================")
        try:
            os.makedirs(directory + "backup-conversion-image")
        except FileExistsError:
            print(Fore.RED + "Un dossier backup existe déjà.")
            confirmation = input("Voulez-vous le supprimer pour créer une nouvelle backup ? [Y/N] : ")
            if confirmation == "Y":
                backup = True
                pass
            elif confirmation == "N":
                backup = False
                pass
            else:
                print(Fore.RED + "Merci de choisir une réponse valide.")
                quit()
        except Exception:
            print(Fore.RED + "Impossible de créer un dossier backup.")
            confirmation = input("Voulez-vous continuer malgré tout ? [Y/N] ")
            if confirmation == "Y":
                backup = False
                pass
            else :
                print("Arrêt du programme et annulation de la conversion.")
                print(Style.RESET_ALL)
                quit()

        if backup == True:
            for filename in os.listdir(directory + "backup-conversion-image"):
                try:
                    os.remove(directory + "backup-conversion-image" + "/" + filename)
                except FileNotFoundError:
                    pass
            for filename in liste_conversion:
                shutil.copy2((directory + filename), (directory + "backup-conversion-image"))
            print(Fore.GREEN + "Backup créée avec succès.")


        for fichier in liste_conversion:
            nouveau_fichier = fichier
            nouveau_fichier = nouveau_fichier.replace(format_entree,format_sortie)

            im = Image.open(directory + fichier).convert("RGB")
            format_img = format_sortie
            format_img = format_sortie.replace(".", "")
            im.save(directory + nouveau_fichier, format_img)

            os.remove(directory + fichier)

            print(Fore.CYAN + f"Conversion de {fichier} en {nouveau_fichier} [{liste_conversion.index(fichier)+1}/{len(liste_conversion)}]")
            nombre_convertit = nombre_convertit + 1

        print(Style.RESET_ALL + "========================")
        print(Fore.YELLOW + "Conversion terminée de", nombre_convertit, "fichiers.")
        if nombre_convertit == len(liste_conversion):
            print(Fore.GREEN + "Aucun problème à signaler.")
            if backup == True:
                if choix_backup == "R":
                    destruction_backup = "Y"
                elif choix_backup == "C":
                    destruction_backup = input("Voulez-vous le supprimer la backup ? [Y/N] : ")  
                elif choix_backup == "K":
                    destruction_backup = ""
                if destruction_backup == "Y":
                    for filename in os.listdir(directory + "backup-conversion-image"):
                        try:
                            os.remove(directory + "backup-conversion-image" + "/" + filename)
                        except FileNotFoundError:
                            pass
                    os.rmdir(directory + "backup-conversion-image")
                    print(Fore.RED + "Backup supprimé.")
                else:
                    print(Fore.GREEN + "Backup préservé.")
        else:
            print(Fore.RED + "Une erreur à été détectée, merci de restaurer la backup et de faire un nouvel essai.")
        print(Style.RESET_ALL)

##########################################################

if __name__ == '__main__':
    maindirectory="D:/Images"
    format_entree=[".jpg", ".webp", ".jpeg"]
    format_sortie=".png"
    choix_backup="R"

    if maindirectory[-1] != "/":
        maindirectory = maindirectory + "/"

    for i in format_entree:
        conversion(maindirectory,i, format_sortie, choix_backup)

    subdirectory = [f.path for f in os.scandir(maindirectory) if f.is_dir()]
    for directory in subdirectory:
        directory = directory + "/"
        for i in format_entree:
            conversion(directory,i, format_sortie, choix_backup)

