# modules/resources.py
import psutil

def show_system_resources():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    print(f"CPU: {cpu}% | RAM: {ram}% | Disque: {disk}%")
