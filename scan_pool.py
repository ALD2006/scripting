import sys
import socket
from concurrent.futures import ThreadPoolExecutor

if len(sys.argv) <= 1:
    print("Veuillez entrer une cible a scanner.", file=sys.stderr)
    sys.exit(1)

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        if s.connect_ex((sys.argv[1], port)) == 0:
            return port
        else:
            return None

with ThreadPoolExecutor(max_workers=82) as executor:
    resultats = executor.map(scan_port, range(20, 101))

for r in resultats:
    if r is not None:
        print(f"Port {r} ouvert !!!")