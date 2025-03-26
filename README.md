---

# Foremost.py 🚀

## Description 📄
Foremost.py is a Python program designed for file recovery and data extraction. It uses the Foremost tool in a WSL (Windows Subsystem for Linux) environment to analyze disk images or raw data and recover files based on their headers, footers, and internal structures.

## Features ✨
- 🔄 Automatically runs Foremost via WSL to recover files.
- 📂 Supports various file formats (images, documents, videos, etc.).
- 🗂️ Organizes recovered files into structured directories.
- ⚡ Lightweight, automated, and easy to use.

## Prerequisites 🛠️
- 🐍 Python 3.x
- 🖥️ WSL (Windows Subsystem for Linux) installed and configured
- 📦 Foremost installed in the WSL environment

## Installation 🧰
1. Clone the repository:  
    ```bash
    git clone https://github.com/your-repo/foremost.py
    ```
2. Navigate to the project directory:  
    ```bash
    cd foremost.py
    ```
3. Ensure WSL is installed and Foremost is available in the WSL environment:  
    ```bash
    wsl sudo apt update && sudo apt install foremost
    ```

## Usage 🖱️
1. ✏️ Modify the Python script to specify the paths to your `.img` file and the output folder:  
    ```python
    wsl_command = "foremost -i /mnt/../../to your .img file -o /mnt/../../recup_img"
    ```
2. ▶️ Run the Python script:  
    ```bash
    python foremost.py
    ```
3. 📁 The recovered files will be available in the specified output folder.

## Code Example 💻
Here is an excerpt from the main script:  
```python
import subprocess

def open_wsl_and_run_command():
    wsl_command = "foremost -i /mnt/../../to your .img file -o /mnt/../../recup_img"
    try:
        print("Opening WSL and executing the command...")
        subprocess.run(["wsl", "bash", "-c", wsl_command], check=True)
        print("Analysis complete! Files are recovered in the specified folder.")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing the command: {e}")
    except FileNotFoundError:
        print("Error: wsl.exe not found. Ensure WSL is properly installed.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    open_wsl_and_run_command()
```

## Notes 📝
- ✅ Ensure the paths specified in the WSL command are correct and accessible.
- 📚 Refer to the official Foremost documentation for advanced options.

## License 📜
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
