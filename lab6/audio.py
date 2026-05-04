import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import os

def record_and_transcribe_lab(duration=5):
    # --- 1. SETTINGS ---
    # 16000 Hz is the native frequency for most Speech-to-Text APIs
    fs = 16000  
    target_folder = r"C:/Users/Antonio/Desktop/lab ecip/lab6"
    filename = "lab6_recording.wav"
    full_path = os.path.join(target_folder, filename)

    print(f"--- Action: Recording for {duration} seconds ---")
    
    try:
        # --- 2. HIGH-QUALITY RECORDING ---
        # We use mono (channels=1) as APIs struggle with stereo
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait() 
        print("Recording finished.")

        # Save the file (Persistence)
        write(full_path, fs, recording)
        print(f"File saved at: {full_path}")

        # --- 3. THE TRANSCRIPTION BRIDGE ---
        recognizer = sr.Recognizer()
        
        # Open the file
        with sr.AudioFile(full_path) as source:
            print("Analyzing audio characteristics...")
            # This is the "Magic" step: It ignores background static in the file
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            # Read the actual speech
            audio_data = recognizer.record(source)
            
            print("Transcribing (sending to Google Cloud)...")
            
            # --- 4. THE API CALL ---
            # Added language='en-US' to be explicit
            text = recognizer.recognize_google(audio_data, language='en-US')
            
            print("\n" + "="*40)
            print(f"TRANSCRIPTION: {text}")
            print("="*40 + "\n")

    except sr.UnknownValueError:
        print("Status: The AI heard the audio but couldn't find recognizable words.")
        print("Tip: Try speaking a bit louder or check if your Windows Mic Gain is too low.")
    except sr.RequestError as e:
        print(f"Status: Network error. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    record_and_transcribe_lab()