# modules/ports.py
import subprocess

def show_open_ports():
    try:
        output = subprocess.check_output(["ss", "-tuln"], text=True)
        print(output.strip())
    except subprocess.CalledProcessError:
        print("Erreur lors de l'analyse des ports.")
