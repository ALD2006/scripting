import sys 
import urllib.parse

if len(sys.argv) <= 1:
    print("Erreur: Veuillez entrer du texte a encoder", file=sys.stderr)
    sys.exit(1)

encoded = urllib.parse.quote(sys.argv[1], safe='')
print(encoded)