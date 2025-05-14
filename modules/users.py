# modules/users.py
import subprocess

def show_connected_users():
    try:
        output = subprocess.check_output(["w", "-h"], text=True)
        print(output.strip())
    except subprocess.CalledProcessError:
        print("Erreur lors de la récupération des utilisateurs connectés.")
