import sounddevice as sd
import wave
import numpy as np

# Function to record audio and save it as a WAV file
def record_voice(filename, duration, sample_rate=44100):
    print("Recording... Speak now!")
    # Record audio using sounddevice library
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
    sd.wait()  # Wait until the recording is complete
    
    # Save the recording to a WAV file
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)  # 16 bits per sample (int16)
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())
    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    # Parameters for recording
    output_filename = "my_voice_recording.wav"
    recording_duration = 10  # duration in seconds
    
    # Record and save the voice
    record_voice(output_filename, recording_duration)
