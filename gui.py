import os
import tkinter as tk
from tkinter import ttk
from recording import start_recording, stop_recording
from file_operations import select_audio_file, select_output_file
from transcription import handle_transcription
from utils import open_transcription

def create_file_window(root):
    """Create the main file management window."""
    # Variables for managing messages and the file list
    message_var = tk.StringVar(value="")  # Variable to store status messages

    # Create a frame for the file window
    main_frame = ttk.Frame(root, padding=(20, 20, 20, 20))
    main_frame.grid(row=0, column=0, sticky="nsew")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Title
    ttk.Label(main_frame, text="Transcription File Manager", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    # File Explorer for Transcription Folder
    ttk.Label(main_frame, text="Transcription Folder Files:").grid(row=1, column=0, columnspan=2, pady=5)
    file_listbox = tk.Listbox(main_frame, height=15, width=60)
    file_listbox.grid(row=2, column=0, columnspan=2, pady=5)

    def update_file_list():
        """Update the file list in the Listbox."""
        transcription_folder = "saved_text"
        file_listbox.delete(0, tk.END)  # Clear the current list
        if os.path.exists(transcription_folder):
            for file_name in os.listdir(transcription_folder):
                file_listbox.insert(tk.END, file_name)

    def open_selected_file(event):
        """Open the selected file from the listbox."""
        try:
            selected_file = file_listbox.get(file_listbox.curselection())
            transcription_folder = "saved_text"
            file_path = os.path.join(transcription_folder, selected_file)
            os.startfile(file_path)  # Open file using the default system application
        except IndexError:
            message_var.set("No file selected.")
        except Exception as e:
            message_var.set(f"Error: {str(e)}")

    # Bind double-click event to open the selected file
    file_listbox.bind("<Double-1>", open_selected_file)

    # Update file list on startup
    update_file_list()

    # Refresh File List Button
    ttk.Button(main_frame, text="Refresh File List", command=update_file_list).grid(row=3, column=0, pady=10)

    # Start New Transcription Button
    def open_transcription_window():
        transcription_window = tk.Toplevel(root)
        create_transcription_window(transcription_window)

    ttk.Button(main_frame, text="Start New Transcription", command=open_transcription_window).grid(row=3, column=1, pady=10)

    # Status Message
    ttk.Label(main_frame, textvariable=message_var, foreground="green").grid(row=4, column=0, columnspan=2, pady=5)

    # Exit Button
    ttk.Button(main_frame, text="Exit", command=root.quit).grid(row=5, column=0, columnspan=2, pady=10)

def create_transcription_window(root):
    """Create the transcription and recording window."""
    # Variables for storing paths and settings
    audio_file_path = tk.StringVar(value="saved_audio/recording.wav")
    model_size = tk.StringVar(value="base")
    output_file_path = tk.StringVar(value="saved_text/transcription.txt")
    open_on_completion = tk.BooleanVar(value=True)
    message_var = tk.StringVar(value="")

    # Recording state
    recording_state = {"recording": False, "frames": None, "fs": 44100}

    # Create a frame for the transcription window
    main_frame = ttk.Frame(root, padding=(20, 20, 20, 20))
    main_frame.grid(row=0, column=0, sticky="nsew")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Title
    ttk.Label(main_frame, text="Transcription and Recording", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=10)

    # Audio File Selection
    ttk.Label(main_frame, text="Audio File:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(main_frame, textvariable=audio_file_path, width=40).grid(row=1, column=1, padx=10, pady=5, sticky="w")
    ttk.Button(main_frame, text="Browse", command=lambda: select_audio_file(audio_file_path)).grid(row=1, column=2, padx=10, pady=5)

    # Record Section
    ttk.Label(main_frame, text="Record Audio:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    ttk.Button(main_frame, text="Start Recording", command=lambda: start_recording(recording_state, status_label)).grid(row=2, column=1, padx=10, pady=5)
    ttk.Button(main_frame, text="Stop Recording", command=lambda: stop_recording(recording_state, status_label, audio_file_path)).grid(row=2, column=2, padx=10, pady=5)
    status_label = ttk.Label(main_frame, text="Click 'Start Recording' to begin.", foreground="blue")
    status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    # Model Selection
    ttk.Label(main_frame, text="Model Size:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    model_options = ["tiny", "base", "small", "medium", "large"]
    ttk.Combobox(main_frame, textvariable=model_size, values=model_options, state="readonly").grid(row=4, column=1, padx=10, pady=5, sticky="w")

    # Output File Selection
    ttk.Label(main_frame, text="Output File:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(main_frame, textvariable=output_file_path, width=40).grid(row=5, column=1, padx=10, pady=5, sticky="w")
    ttk.Button(main_frame, text="Browse", command=lambda: select_output_file(output_file_path)).grid(row=5, column=2, padx=10, pady=5)

    # Open-on-Completion Checkbox
    ttk.Checkbutton(main_frame, text="Open file on completion", variable=open_on_completion).grid(row=6, column=0, columnspan=3, pady=5)

    # Transcription Button
    def transcribe_and_update_message():
        try:
            message_var.set("Processing... Please wait.")
            root.update_idletasks()
            handle_transcription(
                audio_file_path.get(), model_size.get(), output_file_path.get(), open_on_completion.get()
            )
            message_var.set(f"Success: Transcription saved to {output_file_path.get()}.")
        except Exception as e:
            message_var.set(f"Error: {str(e)}")

    ttk.Button(main_frame, text="Transcribe", command=transcribe_and_update_message).grid(row=7, column=0, columnspan=3, pady=20)

    # Message Label
    ttk.Label(main_frame, textvariable=message_var, foreground="green").grid(row=8, column=0, columnspan=3, pady=5)

    # Close Button
    ttk.Button(main_frame, text="Close", command=root.destroy).grid(row=9, column=0, columnspan=3, pady=10)

# Main Application Setup
root = tk.Tk()
root.title("Audio Transcription Manager")
create_file_window(root)
root.mainloop()
