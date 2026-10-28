import sys
import requests
from urllib.parse import urljoin

if len(sys.argv) < 2:
    print("Veullez entrer l'URL de la page cible", file=sys.stderr)
    sys.exit(1)

liste = ["admin", "login", "backup", "images", "test", "robots.txt"]

for lien in liste:
    url = urljoin(sys.argv[1], lien)
    print(f"Essai avec '{lien}':")
    try:
        res = requests.get(url, timeout=1)
        if res.status_code == 404:
            print(f"{res.status_code}: Rien n'a été trouvé !!\n")
        elif res.status_code == 200:
            print(f"{res.status_code}: Page trouvée:")
            print("----------CORPS DE LA REPONSE----------")
            print(f"{res.text[0:300]}\n")
        elif res.status_code in (301, 302):
            redirection = res.headers.get("Location")
            if redirection:
                url_redi = urljoin(sys.argv[1], redirection)
                print(f"{res.status_code}: Redirection vers la page {url_redi}.\n")
            else: 
                print(f"{res.status_code}: Redirection (page de redirection inconnue).\n")
        elif res.status_code == 403:
            print(f"{res.status_code}: Page interdite d'acces !!!\n")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requete: {e}\n", file=sys.stderr)