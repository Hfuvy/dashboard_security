# dashboard.py
from modules import users, ports, files, logs, resources

def main():
    print("=" * 40)
    print("      DASHBOARD DE SÉCURITÉ LINUX")
    print("=" * 40)

    print("\n[1] Utilisateurs connectés :")
    users.show_connected_users()

    print("\n[2] Ports ouverts :")
    ports.show_open_ports()

    print("\n[3] Fichiers modifiés récemment (/etc) :")
    files.show_recent_files("/etc")

    print("\n[4] Événements suspects (auth.log) :")
    logs.show_auth_alerts()

    print("\n[5] Utilisation des ressources :")
    resources.show_system_resources()

    print("=" * 40)

if __name__ == "__main__":
    main()
