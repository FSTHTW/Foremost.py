# Foremost.py

## Description
Foremost.py est un programme en Python conçu pour la récupération de fichiers et l'extraction de données. Il utilise l'outil Foremost dans un environnement WSL (Windows Subsystem for Linux) pour analyser les images disque ou les données brutes et récupérer des fichiers en fonction de leurs en-têtes, pieds de page et structures internes.

## Fonctionnalités
- Exécute automatiquement Foremost via WSL pour récupérer des fichiers.
- Prend en charge divers formats de fichiers (images, documents, vidéos, etc.).
- Organise les fichiers récupérés dans des répertoires structurés.
- Léger, automatisé et facile à utiliser.

## Prérequis
- Python 3.x
- WSL (Windows Subsystem for Linux) installé et configuré
- Foremost installé dans l'environnement WSL

## Installation
1. Clonez le dépôt :
    ```bash
    git clone https://github.com/your-repo/foremost.py
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd foremost.py
    ```
3. Assurez-vous que WSL est installé et que Foremost est disponible dans l'environnement WSL :
    ```bash
    wsl sudo apt update && sudo apt install foremost
    ```

## Utilisation
1. Modifiez le script Python pour spécifier les chemins vers votre fichier `.img` et le dossier de sortie.
    ```python
    wsl_command = "foremost -i /mnt/../../to your .img file -o /mnt/../../recup_img"
    ```
2. Exécutez le script Python :
    ```bash
    python foremost.py
    ```
3. Les fichiers récupérés seront disponibles dans le dossier de sortie spécifié.

## Exemple de Code
Voici un extrait du script principal :
```python
import subprocess

def open_wsl_and_run_command():
    wsl_command = "foremost -i /mnt/../../to your .img file -o /mnt/../../recup_img"
    try:
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
```

## Remarques
- Assurez-vous que les chemins spécifiés dans la commande WSL sont corrects et accessibles.
- Consultez la documentation officielle de Foremost pour des options avancées.

## Licence
Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT).
