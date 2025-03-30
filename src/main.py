﻿import time
from command_handler import execute_command
from handle_command_file import delete_file, file_exists, file_name
from transcriber import AudioTranscriber
from voice_recorder import record_audio

def main():
    print("Listening for commands...")
    transcriber = AudioTranscriber(language="pt-BR")  # Initialize with Portuguese (Brazil)
    
    while True:
        audio_file = file_name()  # Get the name of the file to be executed
        
        # Record the audio, checking for the wake word
        if record_audio(audio_file):
            # Check if the audio file exists before trying to transcribe
            if file_exists(audio_file):
                print(f"Audio file '{audio_file}' found. Transcribing...")
                text = transcriber.transcribe_audio(audio_file)
                
                if text:
                    print(f"Recognized text: {text}")
                    execute_command(text)
                else:
                    print("Could not understand the audio.")
                
                # Delete the audio file after processing to prevent it from being used again
                delete_file(audio_file)
                print(f"{audio_file} deleted to avoid re-triggering.")
            else:
                print(f"Error: Audio file '{audio_file}' not found.")
        
        # Wait a bit before the next command
        time.sleep(2)

if __name__ == "__main__":
    main()
