import sounddevice as sd
from scipy.io.wavfile import write

def start_recording(recording_state, status_label):
    if recording_state["recording"]:
        status_label.config(text="Recording is already in progress.")
        return

    try:
        status_label.config(text="Recording started... Click 'Stop Recording' to save.")
        recording_state["frames"] = []
        recording_state["recording"] = True
        recording_state["frames"] = sd.rec(
            int(recording_state["fs"] * 60), samplerate=recording_state["fs"], channels=2, dtype="int16"
        )
    except Exception as e:
        status_label.config(text=f"Error while starting the recording: {e}")
        recording_state["recording"] = False

def stop_recording(recording_state, status_label, audio_file_path_var):
    if not recording_state["recording"]:
        status_label.config(text="No recording is in progress.")
        return

    try:
        sd.stop()
        write(audio_file_path_var.get(), recording_state["fs"], recording_state["frames"])
        recording_state["recording"] = False
        status_label.config(text=f"Recording stopped. File saved as: {audio_file_path_var.get()}")
    except Exception as e:
        status_label.config(text=f"Error while stopping the recording: {e}")
        recording_state["recording"] = False
