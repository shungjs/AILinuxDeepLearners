import subprocess
import os

# Define the paths to the scripts
email_grabber_path = '/home/wa/test/email_grabber.py'
index_path = '/home/wa/test/index.py'
ai_path = '/home/wa/test/ai.py'

# Execute email_grabber.py to download the audio file
subprocess.run(['python', email_grabber_path], check=True)

# Execute index.py to transcribe the audio file
subprocess.run(['python', index_path], check=True)

# Execute ai.py to process the transcript
subprocess.run(['python', ai_path], check=True)

print("Process completed successfully.")
