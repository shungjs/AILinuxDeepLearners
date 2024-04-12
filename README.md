Assistive Classroom Application
Overview
This project leverages OpenAI's ChatGPT and OpenAI Whisper models to assist visually impaired individuals in classroom settings. The application automates the process of receiving lecture content, transcribing it, and converting it into accessible, detailed notes.

Features
Email Integration: Automatically downloads audio files from emails, allowing for seamless integration with lecturers who can send recorded content directly.
Audio Transcription: Uses Whisper API to transcribe audio content into text, ensuring accurate conversion of spoken words into written form.
Text Processing: Enhances transcriptions with ChatGPT, formatting them into structured notes that highlight main topics and provide summaries in an easy-to-read bullet point format.
How It Works
Email Grabbing: The system starts by checking a designated email for new messages containing audio files and downloads them for processing.
Audio Transcription: Each audio file is processed through the Whisper model to convert speech into text, handling large files by breaking them into chunks.
Note Creation: The transcribed text is then passed through ChatGPT, which refines the content into structured notes, focusing on key information and summaries.

Installation

Install required dependencies:
pip install openai whisper

Set up environment variables for OpenAI API key:
export OPENAI_API_KEY='your-api-key-here'

Usage
To start the application, run the main script:
python main.py
This will execute the process in sequence: downloading, transcribing, and processing text.

Configuration
Email Setup: Configure your email details in email_grabber.py to point to the mailbox where lecture audios are sent.
API Keys: Ensure your OpenAI and other necessary API keys are set correctly in your environment or configuration files.
