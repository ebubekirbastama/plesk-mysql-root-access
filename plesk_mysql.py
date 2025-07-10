#!/usr/bin/env python3
import subprocess
import sys
import os

PSA_SHADOW = "/etc/psa/.psa.shadow"

def get_psa_password():
    try:
        with open(PSA_SHADOW, "r") as f:
            return f.read().strip()
    except Exception as e:
        print(f"[!] Hata: {PSA_SHADOW} dosyasından şifre okunamadı: {e}")
        sys.exit(1)

def run_mysql_command(command):
    password = get_psa_password()
    mysql_cmd = [
        "mysql",
        "-u", "admin",
        f"-p{password}",
        "-e", command
    ]
    try:
        result = subprocess.run(mysql_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[!] MySQL Hatası:\n{result.stderr}")
            sys.exit(result.returncode)
        print(result.stdout)
    except FileNotFoundError:
        print("[!] MySQL client bulunamadı. Lütfen mysql komut satırı aracının kurulu olduğundan emin olun.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Kullanım: ./plesk_mysql.py \"MYSQL_SORGUSU\"")
        print("Örnek: ./plesk_mysql.py \"SHOW DATABASES;\"")
        sys.exit(0)
    command = sys.argv[1]
    run_mysql_command(command)

if __name__ == "__main__":
    main()
