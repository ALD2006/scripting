import sys
import hmac
import hashlib

if len(sys.argv) <= 2:
    print("Erreur: Veuillez entrer la clé en premier argument , puis le message.", file=sys.stderr)
    sys.exit(1)

key = sys.argv[1].encode('utf-8')
msg = sys.argv[2].encode('utf-8')
tag = hmac.new(key, msg, hashlib.sha256).hexdigest()
print("Le tag est:", tag)