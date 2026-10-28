import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("127.0.0.1", 4444))
serveur.listen()
print("En attente de connexion !!!")

client, addresse = serveur.accept()
print(f"Connexion établie depuis: {addresse[0]}:{addresse[1]}")
res = (client.recv(1024)).decode('utf-8')
if res:
    print("Message recu: ",res)

client.close()
serveur.close()
print(f"Connexion fermée avec le client {addresse[0]}:{addresse[1]}")


