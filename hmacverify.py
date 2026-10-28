import sys
import hmac
import hashlib

if len(sys.argv) <= 3:
    print("Erreur: Veuillez entrer la clé, le message et le tag a vérifier.", file=sys.stderr)
    sys.exit(1)

key = sys.argv[1].encode('utf-8')
msg = sys.argv[2].encode('utf-8')

try:
    tag_binaire = bytes.fromhex(sys.argv[3])
except ValueError:
    print("Erreur: Veuillez entrer un tag valide en hexadécimal.", file=sys.stderr)
    sys.exit(1)

tag_verify = hmac.new(key, msg, hashlib.sha256).digest()

if hmac.compare_digest(tag_binaire, tag_verify):
    print("VALIDE")

else:
    print("INVALIDE")