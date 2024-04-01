Project Setup Instructions for Linux
=====================================

This guide details how to set up and run the provided program in a Linux environment.

Prerequisites:
---------------
- Linux operating system
- Visual Studio Code
- Python
- pip (Python package installer)

Installation & Setup:
----------------------

1. Install Visual Studio Code:
   - Download and install Visual Studio Code from the official website: https://code.visualstudio.com/.
   - Alternatively, for distributions like Ubuntu, you can install it using the terminal:
     ```
     sudo snap install code --classic
     ```
     or 
     ```
     sudo apt install code
     ```

2. Install Python:
   - Most Linux distributions come with Python pre-installed. You can check the installed version by typing:
     ```
     python --version
     ```
   - If Python is not installed or you need a different version, you can install it using your distribution's package manager, e.g., for Ubuntu:
     ```
     sudo apt install python python-pip
     ```

3. Install Required Python Libraries:
   - Install the necessary Python packages using pip:
     ```
     pip install torch whisper soundfile openai
     ```

4. Update File and Folder Paths in the Script:
   - Modify the `index.py` script to update the file and folder paths according to where your files are stored on your Linux system. Ensure that the `audio_file` and `parent_folder` variables in `index.py` point to the correct locations.

5. Run the Main Script:
   - Open a terminal, navigate to your project directory, and run:
     ```
     python main.py
     ```

6. Additional Dependencies:
   - If the scripts require specific environment variables or other configurations, make sure they are properly set up in your Linux environment.