import os
import sys
import hashlib

if len(sys.argv) <=1:
    print("Erreur: Veuillez entrer un fichier en argument.", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(f"Erreur: {sys.argv[1]} n'est pas un fichier", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    contenu = f.read()
    taille = str(len(contenu)).encode()
    entete = b"blob " + taille + b"\0" + contenu
    signature = hashlib.sha1(entete).hexdigest()
    print("La signature du fichier est :", signature)