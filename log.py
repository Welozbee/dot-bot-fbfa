def log_add(mail,fiche_id):
    f = open("log.txt","a")
    f.write(f"Ajouté l'adresse mail {mail} à la fiche {fiche_id} \n")
