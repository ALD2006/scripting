#!/bin/bash
set -euo pipefail

logfile="${1:-auth.log}"
seuil="${2:-3}"

if [[ ! -r "$logfile" ]]; then
    echo "fichier $logfile illisible" >&2
    exit 1
fi

echo "=== IP suspects (>= $seuil échecs) dans $logfile ==="

grep "Failed password" "$logfile"\
    | grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}'\
    | sort | uniq -c | sort -rn \
    | awk -v s="$seuil" '$1 >= s { printf "[!] %s : %d echecs \n", $2 , $1 }'