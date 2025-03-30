import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed (default ~200)
    engine.setProperty('volume', 1.0)  # Set volume (0.0 to 1.0)

    # Set voice to Portuguese (pt-BR or pt-PT)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "portuguese" in voice.name.lower():  # Try finding a Portuguese voice
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()