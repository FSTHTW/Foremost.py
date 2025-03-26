import subprocess

def open_wsl_and_run_command():
    # La commande que nous voulons exécuter dans WSL
    wsl_command = "foremost -i /mnt/../../to your .img file -o /mnt/../../recup_img"
    
    # Ouvrir WSL avec la commande Foremost
    try:
        # Utiliser subprocess pour appeler wsl et exécuter la commande séparément
        print("Ouverture de WSL et exécution de la commande...")
        subprocess.run(["wsl", "bash", "-c", wsl_command], check=True)
        print("Analyse terminée ! Les fichiers sont récupérés dans le dossier spécifié.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")
    except FileNotFoundError:
        print("Erreur : wsl.exe non trouvé. Assurez-vous que WSL est bien installé.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    open_wsl_and_run_command()