import tkinter as tk
from tkinter import ttk
from recording import start_recording, stop_recording
from file_operations import select_audio_file, select_output_file
from transcription import handle_transcription
from utils import open_transcription


def create_main_window(root):
    # Variables for storing file paths and model size
    audio_file_path = tk.StringVar(value="saved_audio/recording.wav")  # Default audio file path
    model_size = tk.StringVar(value="base")
    output_file_path = tk.StringVar(value="saved_text/transcription.txt")  # Default text file path

    # Recording state
    recording_state = {"recording": False, "frames": None, "fs": 44100}

    # Main Window Layout
    tk.Label(root, text="Audio Transcription App", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=10)

    # Audio File Selection
    tk.Label(root, text="Audio File:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(root, textvariable=audio_file_path, width=40).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_audio_file(audio_file_path)).grid(row=1, column=2, padx=10, pady=5)

    # Record Section
    tk.Label(root, text="Record Audio:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Button(root, text="Start Recording", command=lambda: start_recording(recording_state, status_label)).grid(row=2, column=1, padx=10, pady=5)
    tk.Button(root, text="Stop Recording", command=lambda: stop_recording(recording_state, status_label, audio_file_path)).grid(row=2, column=2, padx=10, pady=5)
    status_label = tk.Label(root, text="Click 'Start Recording' to begin.", fg="blue")
    status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    # Model Selection
    tk.Label(root, text="Model Size:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    model_options = ["tiny", "base", "small", "medium", "large"]
    ttk.Combobox(root, textvariable=model_size, values=model_options, state="readonly").grid(row=4, column=1, padx=10, pady=5)

    # Output File Selection
    tk.Label(root, text="Output File:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(root, textvariable=output_file_path, width=40).grid(row=5, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_output_file(output_file_path)).grid(row=5, column=2, padx=10, pady=5)

    # Transcription Button
    tk.Button(
        root, text="Transcribe", 
        command=lambda: handle_transcription(audio_file_path.get(), model_size.get(), output_file_path.get())
    ).grid(row=6, column=0, columnspan=3, pady=20)
