import sys
import hashlib
import os

if len(sys.argv) <=1:
    print("Veuillez entrer un fichier en argument.", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(f"{sys.argv[1]} n'est pas un fichier.", file=sys.stderr)
    sys.exit(1)


with open(sys.argv[1], "rb") as fichier:
    binaire = fichier.read()

hasher = hashlib.sha256(binaire)
hexa = hasher.hexdigest()
print(hexa)