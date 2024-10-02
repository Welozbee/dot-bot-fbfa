# ***********************************
# Fichier pour gerer les logs des logs
# ***********************************
import time


def log_add(email, sheetId):
    f = open("log.txt", "a")
    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] Ajouté l'adresse mail {email} à la fiche {sheetId} \n")
    f.close()


def log_remove(email, sheetId):
    f = open("log.txt", "a")
    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] Supprimé les permission de {email} de la fiche {sheetId} \n")
    f.close()

def log_error_change_permissions(email, sheetId, error):
    f = open("log.txt", "a")
    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] ERROR: Une erreur est survenue en essayant de modifier les permission de {email} dans la feuille {sheetId}: {error} \n")
    f.close()