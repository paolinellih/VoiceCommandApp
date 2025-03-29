import speech_recognition as sr

class AudioTranscriber:
    def __init__(self, language="pt-BR"):
        """Initialize the AudioTranscriber with a language setting."""
        self.language = language
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self, audio_file):
        """Transcribe the given audio file and return the text."""
        # Load the audio file
        audio_data = self._load_audio(audio_file)
        
        # If the audio was successfully loaded, proceed with recognition
        if audio_data:
            return self._recognize_audio(audio_data)
        else:
            return ""

    def _load_audio(self, audio_file):
        """Load audio from a file."""
        try:
            with sr.AudioFile(audio_file) as source:
                audio_data = self.recognizer.record(source)  # Capture audio data
            return audio_data
        except Exception as e:
            print(f"Error loading audio file: {e}")
            return None

    def _recognize_audio(self, audio_data):
        """Recognize speech from the given audio data."""
        try:
            text = self.recognizer.recognize_google(audio_data, language=self.language)
            print("Transcription:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
