# modules/logs.py
import re

def show_auth_alerts(log_path="/var/log/auth.log"):
    try:
        with open(log_path, "r") as file:
            lines = file.readlines()
            failed = [line for line in lines if "Failed password" in line]
            for line in failed[-5:]:  # montrer les 5 dernières
                print(line.strip())
            if not failed:
                print("Aucune tentative échouée détectée.")
    except FileNotFoundError:
        print("Fichier de log non trouvé. (auth.log)")
