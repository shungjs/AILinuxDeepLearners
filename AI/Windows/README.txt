Project Setup Instructions for Windows
======================================

This guide details how to set up and run the provided program in a Windows environment, including the installation of Chocolatey and FFmpeg.

Prerequisites:
---------------
- Windows operating system
- Visual Studio Code
- Python 3
- pip (Python package installer)

Installation & Setup:
----------------------

1. Install Visual Studio Code:
   - Download and install Visual Studio Code from the official website: https://code.visualstudio.com/.
   - You can also find installation instructions there tailored to Windows.

2. Install Python:
   - Go to the official Python website to download Python: https://www.python.org/downloads/
   - During the installation process, ensure you select the "Add Python 3.x to PATH" option to make Python accessible from the command line.

3. Install Chocolatey:
   - Open PowerShell as an administrator. You can do this by searching for PowerShell in the Start menu, right-clicking on it, and selecting "Run as administrator."
   - Execute the following command to install Chocolatey:
     ```
     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
     ```
   - Close and reopen the PowerShell window after the installation is complete.

4. Install FFmpeg Using Chocolatey:
   - In the same PowerShell administrator window, install FFmpeg by running:
     ```
     choco install ffmpeg
     ```
   - This command will download and install the latest version of FFmpeg available in the Chocolatey repository.

5. Install Required Python Libraries:
   - Open a command prompt and install the necessary packages using pip:
     ```
     pip install torch whisper soundfile openai
     ```

6. Update File and Folder Paths in the Script:
   - Modify the `index.py` script to update the file and folder paths according to where your files are stored on your system. For example, change the `audio_file` and `parent_folder` variables to the correct paths.

7. Run the Main Script:
   - Open the command prompt, navigate to your project directory, and execute:
     ```
     python main.py
     ```

8. Additional Dependencies:
   - If the scripts require specific environment variables or other configurations, make sure they are correctly set up in your Windows environment.

Conclusion:
------------
By following these instructions, you should be able to execute the provided program in a Windows environment. Ensure all paths and script configurations are adjusted for Windows compatibility.
