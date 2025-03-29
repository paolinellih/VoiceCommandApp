import pyaudio
import wave
import speech_recognition as sr
from text_to_speech import speak_text

def play_wake_word_sound():
    speak_text("Oi!")

def record_audio(output_file, duration=10):
    """Records audio only when wake word is detected and processes command immediately."""
    
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    print("Waiting for wake word...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Shorter noise calibration
        recognizer.energy_threshold = 300  # Adjusted threshold for better detection
        audio = recognizer.listen(source, phrase_time_limit=4)  # Quick detection
    
    try:
        recognized_text = recognizer.recognize_google(audio, language="pt-BR").lower()
        print(f"Recognized: {recognized_text}")
        
        if "carol" in recognized_text:
            play_wake_word_sound()  # Play confirmation immediately
            
            print("Recording command...")

            with mic as source:
                audio = recognizer.listen(source, phrase_time_limit=5)  # Record command immediately
            
            # Save the audio command
            with wave.open(output_file, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
                wf.setframerate(44100)
                wf.writeframes(audio.get_wav_data())

            return True  # Recording successful

        else:
            print("No wake word detected.")
            return False  # Wake word not detected

    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return False  # Speech not understood

    except sr.RequestError:
        print("Speech recognition service error.")
        return False  # API issue