import sys 
import socket

if len(sys.argv) <= 1:
    print("Erreur: Veuillez entrer l'adresse IP a scanner.", file=sys.stderr)
    sys.exit(1)

cible = sys.argv[1]

print(f"Début du scan sur la cible: {cible}")

for port in range (20, 101):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        if s.connect_ex((cible, port)) == 0:
            print(f"Port {port} ouvert !")
#        try:
#            s.connect((cible, port))
#            print(f"Port {port} ouvert !")
#        except (TimeoutError , ConnectionRefusedError):
#            pass
#        except Exception as e:
#            pass

print("Scan Términé")

