import torch
import whisper
import os
import torchaudio
from datetime import datetime

# Load the Whisper model
model = whisper.load_model("tiny")

# Define the audio file
audio_file = "/home/wa/test/recording.wav"

# Define the parent folder
parent_folder = "/home/wa/test/transcripts"

# Generate a unique folder name using the current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
unique_folder_name = f"transcript_{timestamp}"
unique_folder_path = os.path.join(parent_folder, unique_folder_name)

# Create the parent folder, unique folder, and 'dump' subfolder
os.makedirs(unique_folder_path, exist_ok=True)
dump_folder_path = os.path.join(unique_folder_path, 'dump')
os.makedirs(dump_folder_path, exist_ok=True)

def chunk_audio(file_path, chunk_size_mb, output_folder):
    if not file_path.lower().endswith('.wav'):
        raise ValueError("Unsupported file format. Only WAV files are allowed.")
    
    try:
        waveform, sample_rate = torchaudio.load(file_path)
    except Exception as e:
        raise ValueError(f"Error loading audio file: {e}")
    
    bytes_per_sample = waveform.element_size() * waveform.size(0)
    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    chunk_length_samples = int(chunk_size_bytes / bytes_per_sample)
    full_transcript = ""

    print("Starting chunking process")
    for i in range(0, waveform.size(1), chunk_length_samples):
        chunk = waveform[:, i:i + chunk_length_samples]
        chunk_file_path = os.path.join(output_folder, f"chunk_{i//chunk_length_samples}.wav")
        torchaudio.save(chunk_file_path, chunk, sample_rate)
        print(f"Exported {chunk_file_path}")

        print(f"Starting Transcription of {chunk_file_path}")
        transcription_result = model.transcribe(chunk_file_path)
        full_transcript += transcription_result['text'] + " "
        print(transcription_result['text'])

    print("Stopping chunking process")
    return full_transcript

# Transcribe and get the full transcript
transcript = chunk_audio(audio_file, 30, dump_folder_path)

# Save the transcript in a text file inside the unique folder
transcript_file_path = os.path.join(unique_folder_path, 'transcript.txt')
with open(transcript_file_path, 'w') as file:
    file.write(transcript)

print(f"Transcript saved in {transcript_file_path}")
