import whisper
from utils import open_transcription

def transcribe_audio(file_path, model_name="base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(file_path)
    return result["text"]

def save_transcription(transcription, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcription)

def handle_transcription(audio_file_path, model_size, output_file_path, open_on_completion):
    transcription_text = transcribe_audio(audio_file_path, model_size)
    save_transcription(transcription_text, output_file_path)
    if open_on_completion:
        open_transcription(output_file_path)
