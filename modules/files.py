# modules/files.py
import subprocess

def show_recent_files(directory="/etc"):
    try:
        output = subprocess.check_output(["find", directory, "-type", "f", "-mtime", "-1"], text=True)
        print(output.strip() if output.strip() else "Aucun fichier modifié récemment.")
    except subprocess.CalledProcessError:
        print(f"Erreur lors de la vérification des fichiers dans {directory}.")
