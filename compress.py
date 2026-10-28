import os
import sys
import zlib

if len(sys.argv) <=1:
    print("Erreur: Veuillez entrer un fichier en argument", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(f"Erreur: {sys.argv[1]} n'est pas un fichier", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], "rb") as f:
    binaire = f.read()
    print("La taille en binaire est:", len(binaire))
    compressed = zlib.compress(binaire)
    print("La taille de la compression est:", len(compressed))
    decompressed = zlib.decompress(compressed)
    if decompressed == binaire:
        print("decompression reussie !")
    else:
        print("Erreur: Decompression echouee !", file=sys.stderr)
        sys.exit(1)
    
