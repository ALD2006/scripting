import os
import sys 
import base64

if len(sys.argv) <=1:
    print("Erreur: Veuillez donner un fichier comme argument.", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(f"Erreur: {sys.argv[1]} n'est pas un fichier", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], "rb") as fichier:
    binaire = fichier.read()
    encoded = base64.b64encode(binaire)
    print("Le code en b64 est:", encoded)
    decoded = base64.b64decode(encoded).decode('ascii')
    print("Le fichier d'origine est:", decoded)