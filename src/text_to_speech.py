import pyttsx3

def speak_text(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set properties like volume, rate (speed), and voice (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
    
    # Say the text
    engine.say(text)
    
    # Wait until the speech is finished
    engine.runAndWait()
