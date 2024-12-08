import os
from tkinter import messagebox

def open_transcription(output_file):
    if os.path.exists(output_file):
        os.system(f'notepad "{output_file}"')  # Opens the file in Notepad (Windows)
    else:
        messagebox.showerror("Error", f"The file {output_file} does not exist.")


def ensure_directories_exist():
    os.makedirs("saved_audio", exist_ok=True)
    os.makedirs("saved_text", exist_ok=True)