#!/bin/bash
set -euo pipefail

usage() {
    echo "usage: enum.sh -s (system) -u (privesc) -t <cible> (ports) ou -a (tout)" >&2; exit 1
}
section() {
    local titre="$1" 
    echo "[======$titre======]"
}
enum_system() {
    local machine=$(hostname)
    local kernel=$(uname -r)
    local user=$(whoami)
    local nb_users=$(who | wc -l)
    section "Informations Systeme"
    echo "Machine: $machine"
    echo "Noyau: $kernel"
    echo "Utilisateur: $user"
    echo "Nombre de sessions ouvertes: $nb_users"
    section "Fichiers sensibles"
    for f in /etc/passwd /etc/shadow /etc/hosts ; do
        if [[ -r "$f" ]]; then
            echo "[!] Lisible: $f"
        else
            echo "[ ] Non lisible: $f"
        fi 
    done
}
enum_privesc() {
    declare -A legit
    legit["/usr/bin/passwd"]=1
    legit["/usr/bin/gpasswd"]=1
    legit["/usr/bin/chfn"]=1
    legit["/usr/bin/chsh"]=1
    legit["/usr/bin/newgrp"]=1
    legit["/usr/bin/sg"]=1
    legit["/bin/mount"]=1
    legit["/bin/umount"]=1
    legit["/usr/bin/su"]=1
    legit["/usr/bin/sudo"]=1
    legit["/usr/bin/pkexec"]=1
    legit["/usr/lib/dbus-1.0/dbus-daemon-launch-helper"]=1

    section "SUID suspects"
    while IFS= read -r ligne; do
        if [[ ! -v legit["$ligne"] ]]; then
            echo "$ligne INCONNU!!!"
        fi
    done < <(find /  -perm -4000 -type f 2>/dev/null)

    section "CRON inscriptibles"
    while IFS= read -r line; do
        local fichier=$(awk '{print $7}' <<< "$line")
        local owner=$(awk '{print $6}' <<< "$line")
        if [[ "$fichier" == /* ]]; then
            echo "fichier:$fichier ---> user:$owner"
            if [[ -w "$fichier" ]]; then
                echo "!!! WRITABLE !!!"
            fi
        fi
    done < <( cat /etc/crontab ; cat /etc/cron.d/* )
}
enum_ports() {
    local host="$1"
    local port="$2"
    if timeout 1 bash -c "echo > /dev/tcp/$host/$port" 2>/dev/null; then
        echo "[+] $port ouvert"
    else
        echo "[-] $port fermé"
    fi

}
main() { 
    a="false"
    s="false"
    u="false"
    target=""
    ports=""
    while getopts "suat:p:" opt; do
        case "$opt" in
            a) a="true" ;;
            s) s="true" ;;
            u) u="true" ;;
            t) target="$OPTARG" ;;
            p) ports="$OPTARG" ;;
            *) usage ;;
        esac
    done
    if [[ "$a" == "true" ]];then
        s="true"
        u="true"
    fi
    if [[ "$u" == "false" && "$s" == "false" && ( -z "$target" || -z "$ports" ) ]]; then
        usage
    fi
    if [[ "$s" == "true" ]];then
        enum_system
    fi
    if [[ "$u" == "true" ]];then
        enum_privesc
    fi
    if [[ ! -z "$target" && ! -z "$ports" ]];then
        for port in $ports; do
            enum_ports "$target" "$port"
        done
    fi
}
main "$@"