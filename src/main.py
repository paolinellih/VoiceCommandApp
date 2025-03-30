import socket
import time
import winsound
import threading
from flask import Flask, request
import tkinter as tk
from tkinter import simpledialog

import requests
from command_handler import execute_command
from command_file_handler import delete_file, file_exists, file_name
from transcriber import AudioTranscriber
from voice_recorder import record_audio

# Initialize Flask App
app = Flask(__name__)

# Ask for the server IP
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
root = tk.Tk()
root.withdraw()  # Hide main window
server_ip = simpledialog.askstring("Configuração Oi Carol", "Endereço IP:", initialvalue="localhost")

# Get local IP
local_ip = socket.gethostbyname(socket.gethostname())
# Auto-set localhost if the user enters their own IP
if server_ip == local_ip:
    server_ip = "localhost"

# Define the base API URL
base_url = f"http://{server_ip}:5000/execute?command="

# Initialize Transcriber
transcriber = AudioTranscriber(language="pt-BR")

print(f"Server IP: {server_ip}")
print(f"Local IP: {local_ip}")

# 🔹 Call API to execute commands
def execute_command_remote(command, base_url):
    """Send command to Flask API to be executed remotely"""
    try:
        response = requests.get(f"{base_url}/execute?command={command}")
        if response.status_code == 200:
            print(f"Executed successfully: {command}")
        else:
            print(f"Failed to execute: {command}, Error: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with server: {e}")

# 🔹 Remote API to execute commands
@app.route('/execute', methods=['GET'])
def remote_execute():
    command = request.args.get("command")
    if command:
        execute_command(command)  # Run the command!
        return f"Executed: {command}", 200
    return "No command provided!", 400

def voice_recognition():
    """ Handles voice command recognition """
    print("Listening for commands...")
    
    while True:
        audio_file = file_name()  # Get the name of the file to be executed
        
        # Record the audio, checking for the wake word
        if record_audio(audio_file):
            if file_exists(audio_file):  # Ensure the file exists before transcribing
                print(f"Audio file '{audio_file}' found. Transcribing...")
                text = transcriber.transcribe_audio(audio_file)
                
                if text:
                    print(f"Recognized text: {text}")

                    # Decide if we should execute the command locally or remotely
                    if server_ip == "localhost":
                        execute_command(text)
                    else:
                        execute_command_remote(text, base_url)
                else:
                    print("Could not understand the audio.")
                
                # Delete the audio file to prevent duplicate processing
                delete_file(audio_file)
                print(f"{audio_file} deleted to avoid re-triggering.")
            else:
                print(f"Error: Audio file '{audio_file}' not found.")
        
        time.sleep(2)

def start_flask():
    """ Starts the Flask server for remote control """
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    # Run Flask API and voice recognition in parallel threads
    threading.Thread(target=start_flask, daemon=True).start()
    voice_recognition()