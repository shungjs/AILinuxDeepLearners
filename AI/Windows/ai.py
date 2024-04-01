import openai
import os
from openai import OpenAI

# Set your API key
client = OpenAI(api_key="<insert API Key>")

def get_latest_transcript_folder(base_path):
    # Assumes folders are named in a way that allows lexicographical sorting
    all_folders = [os.path.join(base_path, d) for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    latest_folder = max(all_folders, key=os.path.getmtime)
    return latest_folder

def process_content(content, client):
    notes = ""
    chunk_size = 1000  # Adjust based on your needs
    counter = 1  # Reset counter for each new content processing
    for i in range(0, len(content), chunk_size):
        chunk = content[i:i+chunk_size]
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a notetaker who can take detailed notes that highlights the main topics and gives a summary of the lecture. Also you should give the topics in a bullet point form"},
                {"role": "user", "content": chunk}
            ]
        )
        if response.choices and response.choices[0].message.content:
            chunked_note = response.choices[0].message.content
            notes += chunked_note + "\n\n"
        counter += 1
    return notes

def process_file(input_file_path, output_folder, client):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        notes = process_content(content, client)

        output_file_path = os.path.join(output_folder, 'processed_notes.txt')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(notes)

# Path for the base transcripts directory
base_transcripts_path = '/home/wa/test/transcripts/'

# Get the latest transcript folder
latest_folder = get_latest_transcript_folder(base_transcripts_path)

# Set the input and output paths
input_file_path = os.path.join(latest_folder, 'transcript.txt')
output_file_path = latest_folder  # Output in the same folder

# Process the input file and save the output
process_file(input_file_path, output_file_path, client)
