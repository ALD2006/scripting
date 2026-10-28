import sys 
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Veuillez entrer l'url de la page cible.", file=sys.stderr)
    sys.exit(1)

try:
    print("Initialisation de l'extraction.")
    res = requests.get(sys.argv[1], timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")
    if soup.title and soup.title.string:
        print(f"Titre de la page: {soup.title.string.strip()}\n")
    else:
        print("Aucun titre de page trouvé")
    forms = soup.find_all("form")
    if forms:
        for i, f in enumerate(forms, 1):
            action = f.get("action") or "[Aucune action trouvée]"
            methode = f.get("method") or "[GET par défaut]"
            print(f"Formulaire n*{i}")
            print(f"Action du formulaire: {action}")
            print(f"Méthode du formulaire: {methode}")
            print("Recherche des inputs.")
            inputs = f.find_all("input")
            if inputs:
                for inp in inputs:
                    nom = inp.get("name") or "[Aucun nom trouvé]"
                    type_inp = inp.get("type") or "[Aucun type trouvé]"
                    print("Nom de l'input: ", nom)
                    print("Type de l'input: ", type_inp)
                    print("\n")
            else:
                print("Aucun input trouvé pour ce formulaire.\n")
    else:
        print("Aucun formulaire trouvé")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requete: {e}", file=sys.stderr)
    sys.exit(1)