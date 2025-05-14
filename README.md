# 🛡️ Linux Security Dashboard (Projet Python)

Ce projet est un mini tableau de bord de sécurité pour les systèmes Linux, développé en Python. Il permet de surveiller en temps réel certains aspects critiques du système.

## 🚀 Fonctionnalités

- 👥 Affichage des utilisateurs connectés
- 🌐 Liste des ports ouverts (TCP/UDP)
- 🗂️ Fichiers récemment modifiés (dans /etc)
- 🔐 Tentatives de connexion échouées (auth.log)
- 📊 Utilisation des ressources (CPU, RAM, Disque)

## 📁 Structure du projet


security_dashboard/
├── dashboard.py # Script principal
├── modules/
│ ├── init.py # Nécessaire pour les imports Python
│ ├── users.py # Affichage des utilisateurs connectés
│ ├── ports.py # Analyse des ports ouverts
│ ├── files.py # Fichiers modifiés récemment
│ ├── logs.py # Tentatives de connexions échouées
│ └── resources.py # Surveillance des ressources système
└── README.md # Ce fichier



## 🛠️ Installation

### Prérequis

- Python 3.7+
- pip

### Dépendances

Installer `psutil` pour surveiller les ressources système :
```bash
pip install psutil
# secuity_dashboard
# dashboard_security
