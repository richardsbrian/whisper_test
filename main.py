import tkinter as tk
from gui import create_main_window
from utils import ensure_directories_exist

def main():
    ensure_directories_exist()
    root = tk.Tk()
    root.title("Audio Transcription App")
    create_main_window(root)
    root.mainloop()

if __name__ == "__main__":
    main()
