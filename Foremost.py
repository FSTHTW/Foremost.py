import subprocess

def open_wsl_and_run_command():
    # The command we want to execute in WSL
    wsl_command = "foremost -i /mnt/../../to your .img file -o /mnt/../../recup_img"
    
    # Open WSL with the Foremost command
    try:
        # Use subprocess to call wsl and execute the command separately
        print("Opening WSL and executing the command...")
        subprocess.run(["wsl", "bash", "-c", wsl_command], check=True)
        print("Analysis completed! The files are recovered in the specified folder.")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing the command: {e}")
    except FileNotFoundError:
        print("Error: wsl.exe not found. Make sure WSL is installed.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    open_wsl_and_run_command()
