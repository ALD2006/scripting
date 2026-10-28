import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Veuillez entrer l'url de la page cible.", file=sys.stderr)
    sys.exit(1)

try:
    print("Initalisation de l'extraction de :", sys.argv[1])
    res = requests.get(sys.argv[1], timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")
    if soup.title and soup.title.string:
        print(f"Titre de la page: {soup.title.string.strip()}")
    else:
        print("Aucun titre de page trouvé")

    print("Extraction des liens...")
    liens = soup.find_all("a")
    for a in liens:
        href = a.get("href")
        if href:
            texte_lien = a.text.strip() or "[Aucun texte trouvé]"
            print(f"lien: {texte_lien} --> {href}")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requete de la page: {e}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Erreur: {e}", file=sys.stderr)
    sys.exit(1)