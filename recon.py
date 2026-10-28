import sys

if len(sys.argv) <= 1:
    print("Veuillez entrer une cible")

else:
    cible = sys.argv[1]
    print(f"Cible: {cible}")

    if len(sys.argv) > 2:
        encoded = sys.argv[2].encode('utf-8')
        hexa = encoded.hex()
        print(f"hexa du 2eme argument: {hexa}")
        print("longueur octets:", len(encoded))
        print("longueur chaine:", len(sys.argv[2]))
