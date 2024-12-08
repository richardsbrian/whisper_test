from tkinter import filedialog

def select_audio_file(audio_file_path_var):
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if file_path:
        audio_file_path_var.set(file_path)

def select_output_file(output_file_path_var):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        output_file_path_var.set(file_path)
