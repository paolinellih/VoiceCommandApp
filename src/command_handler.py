﻿import asyncio
import os
import sys
import time
import webbrowser
from tkinter import messagebox
import winsound
from advice_api import get_advice
from command_file_handler import delete_file, file_exists, file_name
from text_to_speech import speak_text
from translator import translate_to_portuguese
from image_display import show_image  # Import the function from image_display.py
import pyautogui
import screen_brightness_control as sbc

def play_wrong_sound():
    # Play a "wrong" sound (error beep)
    winsound.Beep(500, 500)  # 500Hz for 500ms (you can adjust these values)

def open_program(program_name):
    """Open a program based on its name"""
    programs = {
        "bloco de notas": "notepad",
        "calculadora": "calc",
        "navegador": "start chrome",
        "gerenciador de tarefas": "taskmgr",
    }
    os.system(programs.get(program_name.lower(), ""))  # Open the program if exists in the dictionary

def open_url(url):
    """Open a URL in the browser"""
    webbrowser.open(url)

def show_hidden_image():
    play_melody()
    show_image()

def show_messagebox(title, message):
    messagebox.showinfo(title, message)

def increase_brightness(current_brightness):
    sbc.set_brightness(min(current_brightness + 50, 100))

def decrease_brightness(current_brightness):
    sbc.set_brightness(max(current_brightness - 50, 0))

def close_carol():
    """Close the app"""
    command_file_name = file_name()
    if file_exists(command_file_name):
        print("Deleting file...")
        delete_file(command_file_name)
    print("Fechando Carol...")
    speak_text("Abraços, até logo!")
    sys.exit()  # Exit the program

async def get_adivice():
    advice = get_advice()
    translated_advice = await translate_to_portuguese(advice)
    speak_text(translated_advice)

def take_screenshot():
    """Take a screenshot, save it, and open it"""
    screenshot = pyautogui.screenshot()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)
    print("Captura de tela salva!")

    # Open the saved screenshot with the default image viewer
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(screenshot_path)
        elif os.name == 'posix':  # For macOS or Linux
            subprocess.call(['open', screenshot_path])  # macOS
            # subprocess.call(['xdg-open', screenshot_path])  # Linux
    except Exception as e:
        print(f"Erro ao abrir a captura de tela: {e}")

def play_melody():
    notes = [(1000, 200), (1200, 200), (1400, 200), (1600, 400)]
    for freq, dur in notes:
        winsound.Beep(freq, dur)

def execute_command(command):
    command = command.lower()  # Ensure case-insensitivity
    
    
    # Define command-action mappings
    command_actions = {
        "abrir calculadora": lambda: open_program("calculadora"),
        "abrir navegador": lambda: open_program("navegador"),
        "abrir bloco de notas": lambda: open_program("bloco de notas"),
        "abrir gerenciador de tarefas": lambda: open_program("gerenciador de tarefas"),
        "abrir google": lambda: open_url("https://www.google.com"),
        "abrir youtube": lambda: open_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        "capturar tela": take_screenshot,
        "mostrar foto": show_hidden_image,
        "compartilhar projeto": lambda: open_url("https://www.linkedin.com/in/henriquepaolinelli"),
        "baixar brilho": lambda: decrease_brightness(sbc.get_brightness()[0]),
        "aumentar brilho": lambda: increase_brightness(sbc.get_brightness()[0]),
        "que horas são": lambda: show_messagebox("Hora Atual", time.strftime("%H:%M:%S")),
        "quero um conselho": lambda: asyncio.run(get_adivice()),
        "fechar carol": close_carol,
    }

    # Check if any predefined command **includes** the spoken text
    for full_command in command_actions.keys():
        if command in full_command:  # Allow partial matches
            action = command_actions[full_command]
            action()  # Execute the corresponding function
            return  # Exit after executing a command
        
    play_wrong_sound()  # Play wrong sound if no match is found
    speak_text("Desculpe, não entendi o comando.")
    print("Comando não reconhecido.")
