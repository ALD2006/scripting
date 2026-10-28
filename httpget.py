import requests
import sys

if len(sys.argv) <= 1:
    print("Veuillez entrer une URL.", file=sys.stderr)
    sys.exit(1)

try:
    res = requests.get(sys.argv[1], timeout=10)
    print(f"Status-code: {res.status_code}")
    serveur = res.headers.get("Server")
    type_contenu = res.headers.get("Content-Type")
    print("----------EN-TÊTES----------")
    print(f"Serveur: {serveur}")
    print(f"Type de contenu: {type_contenu}")
    print("----------CORPS DE LA REPONSE(0-300)----------")
    print(f"{res.text[0:300]}")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requete: {e}", file=sys.stderr)
    sys.exit(1)

