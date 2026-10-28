import sys
import subprocess
import re

if len(sys.argv) <= 1:
    print("Erreur: Veuillez entrer une cible !!", file=sys.stderr)
    sys.exit(1)

res = subprocess.run(["ping", "-n", "1", sys.argv[1]], capture_output=True, text=True)

#if res.returncode == 0:
#    print(f"{res.stdout}")
#else:
#    output = res.stderr or res.stdout
#    print(f"{output}")

if "Reply from" in res.stdout:
    m = re.search(r"time=(\d+)ms", res.stdout)
    if m:
        latence = m.group(1)
        print(f"CIBLE: UP ({latence}ms)")
        sys.exit(0)
    else:
        print("CIBLE: UP (durée indéterminée)")
        sys.exit(0)
else:
    print("CIBLE: DOWN", file=sys.stderr)
    sys.exit(1)
