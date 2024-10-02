from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import log

creds = Credentials.from_service_account_file("credentials.json", scopes=['https://www.googleapis.com/auth/drive']) # Authentification via le compte de service
service = build('drive', 'v3', credentials=creds) # Cr�er le service Google Drive

def addPermission(sheet_id, email, role):
    try:
        # D�finir la permission
        permission = {
            'type': 'user',
            'role': role,
            'emailAddress': email
        }

        # Modifier les permissions avec l'API Google Drive
        service.permissions().create(
            fileId=sheet_id,
            body=permission,
            fields='id'
        ).execute()

        log.log_add(email, sheet_id)
        print(f"Permissions chang�es pour {email} avec le r�le {role}.")

    except Exception as error:
        log.log_error_change_permissions(email, sheet_id, error)
        print(f"Une erreur est survenue : {error}")

def removePermission(sheet_id, email):
    try:
        # R�cup�rer les permissions du fichier
        permissions = service.permissions().list(fileId=sheet_id, fields='permissions').execute()

        # Trouver la permission associ�e � l'email
        permission_id = None
        for permission in permissions.get('permissions', []):
            if permission.get('emailAddress') == email:
                permission_id = permission.get('id')
                break

        if permission_id:
            # Supprimer la permission
            service.permissions().delete(
                fileId=sheet_id,
                permissionId=permission_id
            ).execute()

            log.log_add(email, sheet_id)
            print(f"Permissions supprim�es pour {email}.")
        else:
            print(f"Aucune permission trouv�e pour l'utilisateur {email}.")

    except Exception as error:
        log.log_error_change_permissions(email, sheet_id, error)
        print(f"Une erreur est survenue : {error}")
