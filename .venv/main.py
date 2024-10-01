from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Chemin vers le fichier de clé JSON du compte de service
SERVICE_ACCOUNT_FILE = './credentials.json'

# Scopes (permissions) nécessaires pour Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authentification via le compte de service
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Créer le service Google Drive
service = build('drive', 'v3', credentials=creds)


def change_permission(file_id, email, role):
    """Change les permissions d'un fichier Google Sheets pour un utilisateur spécifique."""
    try:
        # Définir la permission
        permission = {
            'type': 'user',
            'role': role,
            'emailAddress': email
        }

        # Modifier les permissions avec l'API Google Drive
        service.permissions().create(
            fileId=file_id,
            body=permission,
            fields='id'
        ).execute()

        print(f"Permissions changées pour {email} avec le rôle {role}.")

    except Exception as error:
        print(f"Une erreur est survenue : {error}")


if __name__ == '__main__':
    # ID du fichier Google Sheets
    file_id = '1F_jaqT-_QWyB2EQJ7FAFfiexnHIqznGIpasnQ8hKc5E'

    # Email de l'utilisateur avec qui vous voulez partager le fichier
    email = 'dot.flashbackfa@gmail.com'

    # Rôle : 'reader' pour lecture seule, 'writer' pour lecture/écriture
    role = 'writer'

    change_permission(file_id, email, role)
