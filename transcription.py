import whisper

def transcribe_audio(file_path, model_name="base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(file_path)
    return result["text"]

def save_transcription(transcription, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcription)
