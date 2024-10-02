# ***********************************
# Fichier pour gerer les logs des logs
# ***********************************
import time


def log_add(email, sheetId):
    f = open("log.txt", "a")
    f.write(f"[{time.time()}] Ajouté l'adresse mail {email} à la fiche {sheetId} \n")
    f.close()


def log_remove(email, sheetId):
    f = open("log.txt", "a")
    f.write(f"[{time.time()}] Supprimé les permission de {email} de la fiche {sheetId} \n")
    f.close()

def log_error_change_permissions(email, sheetId, error):
    f = open("log.txt", "a")
    f.write(f"[{time.time()}] ERROR: Une erreur est survenue en essayant de modifier les permission de {email} dans la feuille {sheetId}: {error} \n")
    f.close()