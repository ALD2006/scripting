import sys
import requests
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from collections import namedtuple

if len(sys.argv) < 2:
    print("Veuillez entrer l'url de la cible.", file=sys.stderr)
    sys.exit(1)

Resultat = namedtuple("Resultat", ["mot", "code", "redirection"])
def check_url(mot):
    cible = urljoin(sys.argv[1], mot)
    try:
        res = requests.get(cible, timeout=3)
        redirection = res.headers.get("Location")
        code = res.status_code

        return Resultat(mot , code, redirection)
    except requests.exceptions.RequestException:
        return Resultat(mot, code=None, redirection=None)

liste = ["admin", "login", "backup", "images", "test", "robots.txt"]

with ThreadPoolExecutor(max_workers=10) as executor:
    req = executor.map(check_url, liste)

for r in req:
    print("Essai avec ",r.mot)
    if r.code == 404:
        print(f"{r.code}: Rien n'a été trouvé !!\n")
    elif r.code == 200:
        print(f"{r.code}: Page trouvée\n")
    elif r.code in (301, 302):
        if r.redirection is not None:
            url_redi = urljoin(sys.argv[1], r.redirection)
            print(f"{r.code}: Redirection vers la page {url_redi}.\n")
        else: 
            print(f"{r.code}: Redirection (page de redirection inconnue).\n")
    elif r.code == 403:
        print(f"{r.code}: Page interdite d'acces !!!\n")
    elif r.code is None:
        print(f"{r.mot}: Erreur -- Pas de réponse (timeout/erreur réseau)")
