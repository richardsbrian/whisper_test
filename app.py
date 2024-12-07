import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import transcription
import os

def select_audio_file(audio_file_path_var):
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if file_path:
        audio_file_path_var.set(file_path)

def select_output_file(output_file_path_var):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        output_file_path_var.set(file_path)

def open_transcription(output_file):
    if os.path.exists(output_file):
        os.system(f'notepad "{output_file}"')  # Opens the file in Notepad (Windows)
    else:
        messagebox.showerror("Error", f"The file {output_file} does not exist.")

def transcribe_audio(audio_file_path_var, model_size_var, output_file_path_var):
    audio_file = audio_file_path_var.get()
    model_size = model_size_var.get()
    output_file = output_file_path_var.get()

    if not audio_file:
        messagebox.showerror("Error", "Please select an audio file.")
        return

    try:
        transcription_text = transcription.transcribe_audio(audio_file, model_name=model_size)
        transcription.save_transcription(transcription_text, output_file)
        messagebox.showinfo("Success", f"Transcription saved to {output_file}.")
        open_transcription(output_file)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

def main():
    root = tk.Tk()
    root.title("Audio Transcription App")

    # Variables for storing file paths and model size
    audio_file_path = tk.StringVar()
    model_size = tk.StringVar(value="base")
    output_file_path = tk.StringVar(value="transcription.txt")

    # Audio File Selection
    tk.Label(root, text="Audio File:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(root, textvariable=audio_file_path, width=40).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_audio_file(audio_file_path)).grid(row=0, column=2, padx=10, pady=5)

    # Model Selection
    tk.Label(root, text="Model Size:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    model_options = ["tiny", "base", "small", "medium", "large"]
    ttk.Combobox(root, textvariable=model_size, values=model_options, state="readonly").grid(row=1, column=1, padx=10, pady=5)

    # Output File Selection
    tk.Label(root, text="Output File:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(root, textvariable=output_file_path, width=40).grid(row=2, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_output_file(output_file_path)).grid(row=2, column=2, padx=10, pady=5)

    # Transcription Button
    tk.Button(root, text="Transcribe", command=lambda: transcribe_audio(audio_file_path, model_size, output_file_path)).grid(row=3, column=0, columnspan=3, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
