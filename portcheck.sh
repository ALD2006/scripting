#!/bin/bash
set -euo pipefail

check_port() {
    local host="$1"
    local port="$2"
    if timeout 1 bash -c "echo > /dev/tcp/$host/$port" 2>/dev/null; then
        echo "[+] $port ouvert"
    else
        echo "[-] $port fermé"
    fi
} 
host=""
ports=""
while getopts "t:p:" opt; do
    case "$opt" in
        t) host="$OPTARG" ;;
        p) ports="$OPTARG" ;;
        *) echo "usage: $0 -t <cible> -p \"<port1 port2 ...>\"" >&2; exit 1 ;;
    esac
done
if [[ -z "$host" || -z "$ports" ]]; then
    echo "usage: $0 -t <cible> -p \"<port1 port2 ...>\"" >&2; exit 1 
fi

for port in $ports; do
    check_port "$host" "$port"
done