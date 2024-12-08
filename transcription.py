import whisper
from tkinter import messagebox
from utils import open_transcription

def transcribe_audio(file_path, model_name="base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(file_path)
    return result["text"]

def save_transcription(transcription, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcription)

def handle_transcription(audio_file_path, model_size, output_file_path):
    try:
        # Perform transcription
        transcription_text = transcribe_audio(audio_file_path, model_size)
        # Save transcription to file
        save_transcription(transcription_text, output_file_path)
        # Notify user of success
        messagebox.showinfo("Success", f"Transcription saved to {output_file_path}.")
        # Open the saved transcription file
        open_transcription(output_file_path)
    except Exception as e:
        # Display error message
        messagebox.showerror("Error", f"An error occurred:\n{e}")
