import socket
import sys

if len(sys.argv) <= 2:
    print("Erreur: Veuillez entrer l'adresse IP et le Port sur lequel vous voulez vous connecter et la requete a envoyer (optionnel).", file=sys.stderr)
    sys.exit(1)

test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
test.settimeout(10)
port = int(sys.argv[2])
addresse = (sys.argv[1], port)

try:
    print(f"Tentative de connexion vers {sys.argv[1]}:{sys.argv[2]}")
    test.connect(addresse)
    print("Connexion Etablie !")
    if len(sys.argv) > 3:
        requete = (sys.argv[3] + "\r\n\r\n").encode('utf-8')
        print("Envoi de la requete !")
        test.sendall(requete)
        print("Requete envoyée !")

    res = (test.recv(1024)).decode()
    if res:
        print(f"Reponse de la cible: {res}")
    sys.exit(0)
except TimeoutError:
    print("Erreur: Temps écoulé !")
    sys.exit(1)
except ConnectionRefusedError:
    print("Erreur: Connexion refusée par la cible !")
    sys.exit(1)
except Exception as e:
    print(f"Erreur: {e}")
    sys.exit(1)
finally:
    test.close()
    print("Fermeture")