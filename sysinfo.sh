#!/bin/bash
set -euo pipefail
tmp=$(mktemp)
trap 'rm -f "$tmp"; echo "----Nettoyage effectue----"' EXIT

machine=$(hostname); echo "machine = $machine"
kernel=$(uname -r); echo "Kernel = $kernel"
user=$(whoami); echo "User = $user"
if [[ "$user" == "root" ]]; then
    echo "[!] privileges root !"
else
    echo "[ ] utilisateur standard"
fi

nb_users=$(who | wc -l); echo "Nombre de sessions ouvertes = $nb_users"
if (( nb_users > 1 )); then
    echo "[!] Plusieurs sessions activées"
fi

echo "----fichiers sensibles----"
for f in /etc/passwd /etc/shadow /etc/hosts; do
    if [[ -r "$f" ]]; then
        echo "[!] Lisible: $f"
    else 
        echo "[ ] Non lisible: $f"
    fi
done